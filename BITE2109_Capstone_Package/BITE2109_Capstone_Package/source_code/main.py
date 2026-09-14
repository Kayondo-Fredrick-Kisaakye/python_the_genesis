"""
main.py
-------
The entry point that ties everything together. Run it with either:

    python main.py --mode threads
    python main.py --mode async

Both modes do the SAME job (fetch all products, scrape all their
review pages, analyze, report) but use different concurrency
strategies, so you can compare their performance.

------------------------------------------------------------------
WHY CONCURRENCY AT ALL?
------------------------------------------------------------------
If we scraped each product's review page one after another (a plain
for-loop), the total time = (time per request) x (number of products).
Network requests spend most of their time WAITING for a response, not
doing CPU work. Concurrency lets us have many requests "in flight" at
once, so the total time is closer to (time per request) x 1.

MODE 1 - ThreadPoolExecutor (concurrent.futures)
  Runs multiple threads, each doing a normal blocking `requests.get()`.
  Simple to write. Great fit for I/O-bound work like this.

MODE 2 - asyncio + aiohttp
  Runs everything on ONE thread, but uses `await` to pause a task
  while it's waiting on the network and let another task run instead.
  More efficient at very large scale, but requires `async def` /
  `await` syntax throughout, and a different HTTP library (aiohttp)
  because plain `requests` doesn't support async.
------------------------------------------------------------------
"""

import argparse
import asyncio
import cProfile
import pstats
import io

from concurrent.futures import ThreadPoolExecutor

from api_fetcher import fetch_all_products
from scraper import scrape_review_page
from data_models import Product
from analyzer import filter_products_with_reviews, average_price_per_category, top_rated_products
from reporter import print_report, write_json_report
from config import SCRAPER_BASE_URL, REQUEST_TIMEOUT


# ------------------------------------------------------------------
# MODE 1: ThreadPoolExecutor
# ------------------------------------------------------------------
def run_with_threads(raw_products):
    """
    Scrapes every product's review page concurrently using a pool of
    worker threads.

    ThreadPoolExecutor.map() applies scrape_review_page to every
    product id, distributing the calls across `max_workers` threads,
    and returns the results IN ORDER (matching the input order).
    """
    product_ids = [p["id"] for p in raw_products]

    with ThreadPoolExecutor(max_workers=8) as executor:
        review_results = list(executor.map(scrape_review_page, product_ids))

    return _build_products(raw_products, review_results)


# ------------------------------------------------------------------
# MODE 2: asyncio + aiohttp
# ------------------------------------------------------------------
async def _scrape_one_async(session, product_id):
    """Async version of scrape_review_page, using aiohttp instead of requests."""
    import aiohttp  # imported here so `--mode threads` works even without aiohttp installed
    url = f"{SCRAPER_BASE_URL}/{product_id}"
    try:
        async with session.get(url, timeout=aiohttp.ClientTimeout(total=REQUEST_TIMEOUT)) as resp:
            if resp.status == 404:
                return None
            resp.raise_for_status()
            html = await resp.text()
    except (aiohttp.ClientError, asyncio.TimeoutError):
        return None

    # Re-use the same parsing logic as scraper.py by parsing here with
    # BeautifulSoup (kept local to avoid importing requests-based code
    # into the async path).
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html, "html.parser")
    score_tag = soup.find(class_="average-score")
    count_tag = soup.find(class_="review-count")
    if score_tag is None or count_tag is None:
        return None

    try:
        return {
            "avg_score": float(score_tag.text.strip()),
            "review_count": int(count_tag.text.strip().split()[0]),
        }
    except (ValueError, IndexError):
        return None


async def _run_with_async_inner(raw_products):
    import aiohttp
    product_ids = [p["id"] for p in raw_products]

    async with aiohttp.ClientSession() as session:
        # asyncio.gather runs all these coroutines concurrently and
        # waits for all of them to finish, returning results in order.
        tasks = [_scrape_one_async(session, pid) for pid in product_ids]
        review_results = await asyncio.gather(*tasks)

    return _build_products(raw_products, review_results)


def run_with_async(raw_products):
    """Synchronous wrapper so main() can call this the same way as run_with_threads."""
    return asyncio.run(_run_with_async_inner(raw_products))


# ------------------------------------------------------------------
# Shared helper
# ------------------------------------------------------------------
def _build_products(raw_products, review_results):
    """Combines raw API product dicts with their scraped review data into Product objects."""
    products = []
    for raw, review in zip(raw_products, review_results):
        review = review or {}
        products.append(Product(
            id=raw["id"],
            name=raw["name"],
            price=raw["price"],
            category=raw["category"],
            avg_score=review.get("avg_score"),
            review_count=review.get("review_count"),
        ))
    return products


# ------------------------------------------------------------------
# Orchestration
# ------------------------------------------------------------------
def run_pipeline(mode):
    raw_products = fetch_all_products()
    if not raw_products:
        print("No products fetched - is mock_server.py running?")
        return

    if mode == "threads":
        products = run_with_threads(raw_products)
    else:
        products = run_with_async(raw_products)

    with_reviews = filter_products_with_reviews(products)
    avg_prices = average_price_per_category(products)
    top5 = top_rated_products(with_reviews, n=5)

    print_report(top5, avg_prices, total_analyzed=len(products))
    write_json_report(top5, avg_prices, total_analyzed=len(products))


def main():
    parser = argparse.ArgumentParser(description="Multi-threaded / async data aggregator")
    parser.add_argument("--mode", choices=["threads", "async"], default="threads",
                         help="Concurrency strategy to use")
    parser.add_argument("--profile", action="store_true",
                         help="Run with cProfile and print the top time-consuming calls")
    args = parser.parse_args()

    if args.profile:
        profiler = cProfile.Profile()
        profiler.enable()
        run_pipeline(args.mode)
        profiler.disable()

        stats_stream = io.StringIO()
        stats = pstats.Stats(profiler, stream=stats_stream).sort_stats("cumulative")
        stats.print_stats(15)  # top 15 slowest calls
        print("\n--- cProfile output (top 15 by cumulative time) ---")
        print(stats_stream.getvalue())
    else:
        run_pipeline(args.mode)


if __name__ == "__main__":
    main()
