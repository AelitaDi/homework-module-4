from src.product import Product
from src.product_iterator import ProductIterator


class Category:
    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.category_count += 1
        Category.product_count += len(products) if products else 0

    def __str__(self):
        count = 0
        for product in self.products_list:
            count += product.quantity
        return f"{self.name.title()}, количество продуктов: {count} шт."

    def add_product(self, new_product: Product):
        """Добавление нового товара в список."""
        self.__products.append(new_product)
        Category.product_count += 1

    @property
    def products(self):
        product_str = ""
        for product in self.__products:
            product_str += f"{str(product)}\n"
        return product_str

    # @add_product.setter
    # def add_product(self, new_product: Product):
    #     self.__products.append(new_product)

    @property
    def products_list(self):
        return self.__products


if __name__ == "__main__":
    product1 = Product("огурец", "256GB, Серый цвет, 200MP камера", 1.0, 5)
    product2 = Product("морковь", "512GB, Gray space", 2.0, 8)
    product3 = Product("лук", "1024GB, Синий", 31000.0, 14)
    product4 = Product.new_product({"name": "молоко", "description": "молочные продукты", "price": 6, "quantity": 8})
    cat1 = Category("овощи", "любые овощи", [product1, product2])
    cat1.add_product(product4)
    # print(cat1.products)
    # cat1.add_product(product1)
    # print(cat1.products)
    # product4.price = 10
    # print(cat1.products)
    # print(cat1)
    # print(product1 + product2)

    iterator = ProductIterator(cat1)
    for prod in iterator:
        print(prod)
