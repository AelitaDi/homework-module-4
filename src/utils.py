import json
import os

from src.category import Category
from src.product import Product


def read_json(path: str) -> dict:
    """Read data from JSON-file."""

    full_path = os.path.abspath(path)
    with open(full_path, "r", encoding="UTF-8") as file:
        data = json.load(file)
    return data


def create_objects_from_json(data):
    """Create class objects from dict."""

    categories = []
    for category in data:
        products = []
        for product in category["products"]:
            products.append(Product(**product))
        category["products"] = products
        categories.append(Category(**category))
    return categories


if __name__ == "__main__":
    cat_data = read_json("../data/products.json")
    cats = create_objects_from_json(cat_data)
    print(cats[0].description)
