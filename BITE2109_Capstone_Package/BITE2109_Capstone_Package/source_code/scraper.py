"""
scraper.py
----------
Responsible for ONE job: given a product ID, fetch its review page (HTML)
and extract the average score and review count using BeautifulSoup.

Key concepts demonstrated here:
  - requests to download raw HTML
  - BeautifulSoup to parse HTML and find specific elements by CSS class
  - Graceful handling of missing pages (product has no reviews / 404)
"""

import requests
from bs4 import BeautifulSoup
from config import SCRAPER_BASE_URL, REQUEST_TIMEOUT


def scrape_review_page(product_id):
    """
    Scrapes the review page for a single product.

    Returns a dict: {"avg_score": float, "review_count": int}
    Returns None if the page doesn't exist or has no review data,
    so the caller can filter these products out later.
    """
    url = f"{SCRAPER_BASE_URL}/{product_id}"

    try:
        response = requests.get(url, timeout=REQUEST_TIMEOUT)

        if response.status_code == 404:
            # This product simply has no review page - not a crash,
            # just a normal "no data" case.
            return None

        response.raise_for_status()

    except requests.exceptions.RequestException as e:
        print(f"[scraper] Failed to reach review page for product {product_id}: {e}")
        return None

    # "html.parser" is Python's built-in parser - no extra install needed.
    soup = BeautifulSoup(response.text, "html.parser")

    score_tag = soup.find(class_="average-score")
    count_tag = soup.find(class_="review-count")

    if score_tag is None or count_tag is None:
        # The page loaded, but didn't have the elements we expected.
        return None

    try:
        avg_score = float(score_tag.text.strip())
        # count_tag.text looks like "123 reviews" -> pull out the number
        review_count = int(count_tag.text.strip().split()[0])
    except (ValueError, IndexError):
        print(f"[scraper] Could not parse review numbers for product {product_id}")
        return None

    return {"avg_score": avg_score, "review_count": review_count}
