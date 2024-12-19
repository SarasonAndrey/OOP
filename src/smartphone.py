from src.product import Product


class Smartphone(Product):  # Смартфон

    def __init__(
        self, name, discription, price, quantity, efficiency, model, memory, color
    ):
        super().__init__(name, discription, price, quantity)
        self.efficiency = efficiency  # производительность
        self.model = model  # модель
        self.memory = memory  # объем встроенной памяти
        self.color = color  # цвет

    def __add__(self, other):
        if type(other) is Smartphone:
            return self.price * self.quantity + other.price * other.quantity
        raise TypeError
