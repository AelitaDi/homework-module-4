import pytest

from src.category import Category
from src.product import Product
from src.product_iterator import ProductIterator


@pytest.fixture
def first_product():
    return Product(name="Product", description="some kind of description", price=10.0, quantity=10)


@pytest.fixture
def first_category():
    return Category(
        name="овощи",
        description="свежие овощи",
        products=[Product("лук", "лук зеленый", 10.0, 10), Product("морковь", "морковь мытая", 20.0, 20)],
    )


@pytest.fixture
def second_category():
    return Category(
        name="хлеб",
        description="хлебобулочные изделия",
        products=[
            Product("батон", "батон нарезной", 10.0, 10),
            Product("хлеб", "хлеб бородинский", 20.0, 20),
            Product("хлеб", "хлеб дарницкий", 30.0, 30),
        ],
    )


@pytest.fixture
def product():
    return Product("молоко", "молоко ультрапастеризованное 1л", 40.0, 100)


@pytest.fixture
def product_iterator(first_category):
    return ProductIterator(first_category)
