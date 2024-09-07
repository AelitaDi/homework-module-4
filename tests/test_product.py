from src.product import Product


def test_product(product):
    assert product.name == "молоко"
    assert product.description == "молоко ультрапастеризованное 1л"
    assert product.price == 40.0
    assert product.quantity == 100


def test_new_prod():
    prod = Product.new_product({"name": "соль", "description": "соль морская", "price": 11.1, "quantity": 22})
    assert prod.name == "соль"
    assert prod.description == "соль морская"
    assert prod.price == 11.1
    assert prod.quantity == 22


def test_price_update(capsys, first_product):
    assert first_product.price == 10.0
    first_product.price = 12.0
    assert first_product.price == 12.0
    first_product.price = -3
    message = capsys.readouterr()
    assert message.out.strip().split("\n")[-1] == "Цена не должна быть нулевая или отрицательная"
    assert first_product.price == 12.0


def test_product_str(first_product):
    assert str(first_product) == "Product, 10.0 руб. Остаток: 10 шт."


def test_product_add(first_product, product):
    assert first_product + product == 4100.0
