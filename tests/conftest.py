import pytest

from src.category import Category
from src.lawngrass import LawnGrass
from src.product import Product
from src.product_iterator import ProductIterator
from src.smartphone import Smartphone


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


@pytest.fixture
def smartphone1():
    return Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")


@pytest.fixture
def smartphone2():
    return Smartphone("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14, 90.3, "Note 11", 1024, "Синий")


@pytest.fixture
def grass1():
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")


@pytest.fixture
def grass2():
    return LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")


@pytest.fixture
def no_products_category():
    return Category(name="овощи", description="свежие овощи", products=[])
