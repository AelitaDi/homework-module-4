def test_product(product):
    assert product.name == "молоко"
    assert product.description == "молоко ультрапастеризованное 1л"
    assert product.price == 40.0
    assert product.quantity == 100
