"""
reporter.py
-----------
Takes the analysis results and presents them:
  1. Printed nicely to the console.
  2. Written to a JSON file (report.json) for machine-readable output.
"""

import json
from config import REPORT_OUTPUT_FILE


def print_report(top_products, avg_price_per_category, total_analyzed):
    print("\n" + "=" * 50)
    print("PRODUCT SENTIMENT & AVAILABILITY REPORT")
    print("=" * 50)

    print(f"\nTotal products analyzed: {total_analyzed}")

    print("\nAverage price per category:")
    for category, avg_price in avg_price_per_category.items():
        print(f"  {category:<15} ${avg_price:>8.2f}")

    print("\nTop rated products:")
    for i, product in enumerate(top_products, start=1):
        print(f"  {i}. {product.name:<30} score={product.avg_score} "
              f"({product.review_count} reviews)")

    print("=" * 50 + "\n")


def write_json_report(top_products, avg_price_per_category, total_analyzed, filename=None):
    filename = filename or REPORT_OUTPUT_FILE

    report_data = {
        "total_products_analyzed": total_analyzed,
        "average_price_per_category": avg_price_per_category,
        "top_rated_products": [p.to_dict() for p in top_products],
    }

    with open(filename, "w") as f:
        json.dump(report_data, f, indent=2)

    print(f"[reporter] Report written to {filename}")
