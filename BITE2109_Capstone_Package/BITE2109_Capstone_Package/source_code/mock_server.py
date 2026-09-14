"""
mock_server.py
---------------
The assignment says to use "dummy/fake URLs ... or create simple mock
servers". Since we don't have a real market-research API to call, this
file IS that mock server. It runs locally on your machine and pretends
to be both:

  1. The product API      -> GET /api/products
                              GET /api/products/<id>
  2. The review website    -> GET /reviews/<id>   (returns HTML to scrape)

Run this in its own terminal window BEFORE running main.py:

    python mock_server.py

It will keep running (serving requests) until you press Ctrl+C.
"""

from flask import Flask, jsonify
import random

app = Flask(__name__)

# A small fake "database" of products.
PRODUCTS = [
    {"id": 1, "name": "Wireless Mouse",       "price": 19.99, "category": "Electronics"},
    {"id": 2, "name": "Mechanical Keyboard",  "price": 89.50, "category": "Electronics"},
    {"id": 3, "name": "Standing Desk",        "price": 249.00, "category": "Furniture"},
    {"id": 4, "name": "Office Chair",         "price": 175.25, "category": "Furniture"},
    {"id": 5, "name": "USB-C Hub",            "price": 34.99, "category": "Electronics"},
    {"id": 6, "name": "Desk Lamp",            "price": 22.40, "category": "Furniture"},
    {"id": 7, "name": "Noise-Cancelling Headphones", "price": 199.99, "category": "Electronics"},
    {"id": 8, "name": "Bookshelf",            "price": 89.00, "category": "Furniture"},
    # Product 9 deliberately has NO review page, to test error handling
    {"id": 9, "name": "Mystery Gadget",       "price": 9.99, "category": "Electronics"},
    {"id": 10, "name": "Ergonomic Footrest",  "price": 29.99, "category": "Furniture"},
]

# Deterministic fake reviews so results are reproducible while you test.
random.seed(42)
REVIEWS = {
    p["id"]: {
        "avg_score": round(random.uniform(2.5, 5.0), 1),
        "review_count": random.randint(0, 500),
    }
    for p in PRODUCTS if p["id"] != 9  # product 9 has no reviews on purpose
}


@app.route("/api/products", methods=["GET"])
def get_all_products():
    """Returns the full product list as JSON (simulates the real API)."""
    return jsonify(PRODUCTS)


@app.route("/api/products/<int:product_id>", methods=["GET"])
def get_product(product_id):
    """Returns a single product, or a 404 if it doesn't exist."""
    for p in PRODUCTS:
        if p["id"] == product_id:
            return jsonify(p)
    return jsonify({"error": "Product not found"}), 404


@app.route("/reviews/<int:product_id>", methods=["GET"])
def get_review_page(product_id):
    """
    Returns a small HTML page containing review info, mimicking a real
    website that scraper.py will parse with BeautifulSoup.
    """
    if product_id not in REVIEWS:
        # No review page exists for this product -> simulate a 404
        return "<html><body><h1>404 - Not Found</h1></body></html>", 404

    data = REVIEWS[product_id]
    html = f"""
    <html>
      <body>
        <div class="review-summary">
          <span class="average-score">{data['avg_score']}</span>
          <span class="review-count">{data['review_count']} reviews</span>
        </div>
      </body>
    </html>
    """
    return html


if __name__ == "__main__":
    print("Mock server running at http://127.0.0.1:5000")
    print("  Product list:  http://127.0.0.1:5000/api/products")
    print("  Example review: http://127.0.0.1:5000/reviews/1")
    app.run(port=5000, debug=False)
