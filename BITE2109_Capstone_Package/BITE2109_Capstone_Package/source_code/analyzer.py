"""
analyzer.py
-----------
Takes a list of Product objects and analyzes them using functional
programming tools: map, filter, and functools.reduce.

WHY these instead of a for-loop? A for-loop works fine too — but the
assignment specifically wants you to practice the functional style,
which is common in data-processing code because it expresses
"transform this whole collection" more declaratively than a loop with
manual accumulator variables.
"""

from functools import reduce


def filter_products_with_reviews(products):
    """
    Keep only products that HAVE reviews.
    filter(function, iterable) keeps items where function(item) is True.
    """
    return list(filter(lambda p: p.has_reviews(), products))


def average_price_per_category(products):
    """
    Returns a dict like {"Electronics": 85.4, "Furniture": 130.2}

    Approach:
      1. Get the unique categories (a set comprehension).
      2. For each category, use `filter` + `map` to get just the prices
         of products in that category.
      3. Use `reduce` to sum those prices, then divide by count.
    """
    categories = {p.category for p in products}
    result = {}

    for category in categories:
        # filter: only products in this category
        in_category = filter(lambda p, c=category: p.category == c, products)
        # map: pull out just the price from each product
        prices = list(map(lambda p: p.price, in_category))

        if not prices:
            continue

        # reduce: combine all prices into a single sum
        total = reduce(lambda acc, price: acc + price, prices, 0)
        result[category] = round(total / len(prices), 2)

    return result


def top_rated_products(products, n=5):
    """
    Returns the top `n` products sorted by avg_score, highest first.
    Products with no score (None) are excluded first via filter.
    """
    scored = filter(lambda p: p.avg_score is not None, products)
    return sorted(scored, key=lambda p: p.avg_score, reverse=True)[:n]
