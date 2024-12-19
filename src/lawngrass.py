from src.product import Product


class LawnGrass(Product):  # Трава газонная
    def __init__(
        self, name, discription, price, quantity, country, germination_period, color
    ):
        super().__init__(name, discription, price, quantity)
        self.discription = None
        self.country = country  # страна-производитель
        self.germination_period = germination_period  # срок прорастания
        self.color = color  # цвет

    def __add__(self, other):
        if type(other) is LawnGrass:
            return self.price * self.quantity + other.price * other.quantity
        raise TypeError
