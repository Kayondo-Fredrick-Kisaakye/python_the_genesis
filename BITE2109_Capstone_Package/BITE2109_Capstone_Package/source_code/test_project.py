"""
test_project.py
----------------
Unit tests for the core logic. Run with:

    pytest test_project.py -v

Includes at least one test that uses unittest.mock to patch a network
call, as required — see test_fetch_product_uses_mocked_network.
"""

from unittest.mock import patch, Mock

from data_models import Product
from analyzer import filter_products_with_reviews, average_price_per_category, top_rated_products
import api_fetcher


def make_product(id, name, price, category, avg_score=None, review_count=None):
    return Product(id, name, price, category, avg_score, review_count)


# ------------------------------------------------------------------
# data_models tests
# ------------------------------------------------------------------
def test_product_has_reviews_true():
    p = make_product(1, "Mouse", 19.99, "Electronics", avg_score=4.5, review_count=10)
    assert p.has_reviews() is True


def test_product_has_reviews_false_when_zero():
    p = make_product(1, "Mouse", 19.99, "Electronics", avg_score=None, review_count=0)
    assert p.has_reviews() is False


def test_product_slots_prevents_new_attribute():
    """__slots__ should stop you from adding attributes that don't exist."""
    p = make_product(1, "Mouse", 19.99, "Electronics")
    try:
        p.some_new_field = "oops"
        assert False, "Expected AttributeError due to __slots__"
    except AttributeError:
        pass


# ------------------------------------------------------------------
# analyzer tests
# ------------------------------------------------------------------
def test_filter_products_with_reviews():
    products = [
        make_product(1, "A", 10, "Cat1", avg_score=4.0, review_count=5),
        make_product(2, "B", 20, "Cat1", avg_score=None, review_count=0),
    ]
    result = filter_products_with_reviews(products)
    assert len(result) == 1
    assert result[0].id == 1


def test_average_price_per_category():
    products = [
        make_product(1, "A", 10, "Electronics"),
        make_product(2, "B", 30, "Electronics"),
        make_product(3, "C", 100, "Furniture"),
    ]
    result = average_price_per_category(products)
    assert result["Electronics"] == 20.0
    assert result["Furniture"] == 100.0


def test_top_rated_products_orders_correctly():
    products = [
        make_product(1, "A", 10, "Cat", avg_score=3.0, review_count=5),
        make_product(2, "B", 10, "Cat", avg_score=4.9, review_count=5),
        make_product(3, "C", 10, "Cat", avg_score=4.0, review_count=5),
    ]
    top = top_rated_products(products, n=2)
    assert [p.id for p in top] == [2, 3]


# ------------------------------------------------------------------
# Mocked network test (required by the assignment)
# ------------------------------------------------------------------
def test_fetch_product_uses_mocked_network():
    """
    Uses unittest.mock.patch to replace requests.get with a fake object,
    so this test runs instantly and never touches the real network.
    """
    api_fetcher.fetch_product.cache_clear()  # reset lru_cache between test runs

    fake_response = Mock()
    fake_response.json.return_value = {"id": 1, "name": "Mouse", "price": 19.99}
    fake_response.raise_for_status.return_value = None

    with patch("api_fetcher.requests.get", return_value=fake_response) as mock_get:
        result = api_fetcher.fetch_product(1)

        mock_get.assert_called_once()
        assert result == {"id": 1, "name": "Mouse", "price": 19.99}
