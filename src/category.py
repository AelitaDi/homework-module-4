from src.product import Product


class Category:
    name: str
    description: str
    products: list
    categories_count = 0
    products_count = 0

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.products = products if products else []
        Category.categories_count += 1
        Category.products_count += len(products) if products else 0


if __name__ == "__main__":
    product1 = Product("лук", "лук свежий зеленый", 37.5, 20)
    product2 = Product("хлеб", "хлеб белый", 20.0, 10)
    product3 = Product("молоко", "молоко ультрапастеризованное 1л", 40.0, 100)
    product4 = Product("помидоры", "помидоры сливовидные 1кг", 100, 20)
    category1 = Category("овощи", "свежие овощи, зелень", [product1, product4])
    category2 = Category("хлеб", "хлебобулочные изделия", [product2])
    category3 = Category("одежда", "одежда", [])

    print(product1.name)
    print(product1.description)
    print(product2.price)
    print(product3.quantity)
    print(Category.products_count)
