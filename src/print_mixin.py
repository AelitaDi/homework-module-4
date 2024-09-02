class PrintMixin:

    def __init__(self):
        print(repr(self))

    def __repr__(self):
        return f"{self.name}, {self.description}, {self.price}, {self.quantity}"
