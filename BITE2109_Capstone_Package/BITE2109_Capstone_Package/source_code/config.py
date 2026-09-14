"""
config.py
---------
Central place for constants. Keeping URLs and settings here (instead of
scattered through the code) means if the API address changes, you only
edit it in ONE place.

NOTE: These are dummy/mock URLs. Replace them with real ones, or point
them at the mock server included in this project (see mock_server.py).
"""

# Base URL of the product API (mocked locally by mock_server.py)
API_BASE_URL = "http://127.0.0.1:5000/api/products"

# Base URL of the "review site" we scrape (also mocked locally)
SCRAPER_BASE_URL = "http://127.0.0.1:5000/reviews"

# How long (seconds) we wait for a network response before giving up
REQUEST_TIMEOUT = 5

# Where the final report gets written
REPORT_OUTPUT_FILE = "report.json"
