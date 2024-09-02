from src.lawngrass import LawnGrass
from src.product import Product
from src.smartphone import Smartphone


def test_print_mixin(capsys):
    Product("молоко", "молоко ультрапастеризованное 1л", 40.0, 100)
    assert capsys.readouterr().out.strip() == "Product(молоко, молоко ультрапастеризованное 1л, 40.0, 100)"

    Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")
    assert capsys.readouterr().out.strip() == "Smartphone(Iphone 15, 512GB, Gray space, 210000.0, 8)"

    LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
    assert capsys.readouterr().out.strip() == "LawnGrass(Газонная трава, Элитная трава для газона, 500.0, 20)"
