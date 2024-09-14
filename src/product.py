from src.base_product import BaseProduct
from src.print_mixin import PrintMixin


class Product(BaseProduct, PrintMixin):
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        if quantity > 0:
            self.quantity = quantity
            super().__init__()
        else:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")

    def __str__(self):
        return f"{self.name.title()}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if type(other) is Product:
            return (self.__price * self.quantity) + (other.__price * other.quantity)
        raise TypeError

    @classmethod
    def new_product(cls, new_product_dict: dict):
        """Инициализация нового товара."""
        name = new_product_dict["name"]
        description = new_product_dict["description"]
        price = new_product_dict["price"]
        quantity = new_product_dict["quantity"]
        return cls(name, description, price, quantity)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price: float):
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        if new_price < self.__price:
            answer = input("Подтвердите снижение стоимости товара (введите Y): ")
            if answer.upper() == "Y":
                self.__price = new_price
            else:
                return
        self.__price = new_price
