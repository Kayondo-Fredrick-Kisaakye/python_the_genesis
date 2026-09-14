"""
api_fetcher.py
--------------
Responsible for ONE job: talking to the product API and turning its
JSON responses into plain Python dictionaries the rest of the app can use.

Key concepts demonstrated here:
  - requests library for HTTP calls
  - JSON parsing
  - Error handling (timeouts, bad status codes, connection errors)
  - functools.lru_cache to avoid re-fetching the same product twice
"""

import requests
from functools import lru_cache
from config import API_BASE_URL, REQUEST_TIMEOUT


def fetch_all_products():
    """
    Fetches the full product list from the API.
    Returns a list of dicts, e.g. [{"id": 1, "name": ..., "price": ...}, ...]
    Returns an empty list if the request fails, so callers don't crash.
    """
    try:
        response = requests.get(API_BASE_URL, timeout=REQUEST_TIMEOUT)
        response.raise_for_status()  # raises an exception for 4xx/5xx codes
        return response.json()
    except requests.exceptions.Timeout:
        print(f"[api_fetcher] Timed out after {REQUEST_TIMEOUT}s contacting {API_BASE_URL}")
        return []
    except requests.exceptions.ConnectionError:
        print(f"[api_fetcher] Could not connect to {API_BASE_URL}. Is the mock server running?")
        return []
    except requests.exceptions.HTTPError as e:
        print(f"[api_fetcher] API returned an error status: {e}")
        return []
    except ValueError:
        # response.json() failed to parse -> not valid JSON
        print("[api_fetcher] API response was not valid JSON.")
        return []


@lru_cache(maxsize=128)
def fetch_product(product_id):
    """
    Fetches a SINGLE product by ID.

    @lru_cache means: if this function is called twice with the same
    product_id, the second call returns the cached result instantly
    instead of hitting the network again. This directly satisfies the
    assignment's "cache API responses for products requested multiple
    times" requirement.

    NOTE: lru_cache requires arguments to be hashable, which a plain
    int (product_id) already is, so no extra work is needed here.
    """
    url = f"{API_BASE_URL}/{product_id}"
    try:
        response = requests.get(url, timeout=REQUEST_TIMEOUT)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"[api_fetcher] Failed to fetch product {product_id}: {e}")
        return None
