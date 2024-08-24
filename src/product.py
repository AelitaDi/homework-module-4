class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

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
