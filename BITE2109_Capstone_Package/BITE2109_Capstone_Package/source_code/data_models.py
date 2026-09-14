"""
data_models.py
--------------
Defines the Product class - the custom data structure this project
uses to represent one product with all its combined data (from the
API AND the scraper).

Key concept: __slots__

Normally, every Python object stores its attributes in a hidden
dictionary (__dict__), which is flexible but uses extra memory per
object. If you're creating THOUSANDS of Product objects (like a real
market-research firm would), that overhead adds up.

__slots__ tells Python: "this class will ONLY ever have these exact
attributes - don't bother creating a __dict__ for it." This:
  - reduces memory usage per instance (often 30-50% less)
  - prevents typos like product.pric = 10 (raises AttributeError
    instead of silently creating a new, wrong attribute)

The trade-off: you can't add new attributes on the fly, which is fine
here because we know exactly what a Product looks like.
"""


class Product:
    __slots__ = ("id", "name", "price", "category", "avg_score", "review_count")

    def __init__(self, id, name, price, category, avg_score=None, review_count=None):
        self.id = id
        self.name = name
        self.price = price
        self.category = category
        self.avg_score = avg_score        # None until scraper.py fills it in
        self.review_count = review_count  # None until scraper.py fills it in

    def has_reviews(self):
        """True if this product has at least one review."""
        return self.review_count is not None and self.review_count > 0

    def __repr__(self):
        return (f"Product(id={self.id}, name={self.name!r}, price={self.price}, "
                f"category={self.category!r}, avg_score={self.avg_score}, "
                f"review_count={self.review_count})")

    def to_dict(self):
        """Convert back to a plain dict - useful for JSON output."""
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "category": self.category,
            "avg_score": self.avg_score,
            "review_count": self.review_count,
        }
