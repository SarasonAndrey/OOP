import pytest

from src.lawngrass import LawnGrass
from src.smartphone import Smartphone
from src.category import Category
from src.product import Product


@pytest.fixture
def product_1():
    return Product(name="Патифон", description="старый", price="123.3", quantity="3")


@pytest.fixture
def product_2():
    return Product(name="777", description="", price="123.3", quantity="")


@pytest.fixture
def product_3():
    return Product(name="", description="", price="", quantity="")


@pytest.fixture
def category_1():
    return Category(
        name="оборудование", description="музыкальный", products=["магнитола", "плеер"]
    )


@pytest.fixture
def category_2():
    category_2.number_of_categories = 0
    category_2.number_of_products = 0
    return Category(
        name="мебель", description="для спальни", products=["кровать", "диван"]
    )


@pytest.fixture
def category_3():
    return Category(name="", description="", products=[""])


@pytest.fixture
def product_data():
    return Product(name="Патифон", description="старый", price="123.3", quantity=3)


@pytest.fixture
def new_product():
    return Product(name="Гусли", description="старый", price="777777", quantity=1)


@pytest.fixture
def add_product_1(self, new_products: Product):
    self.__products.append(new_products)
    return Category.number_of_products == 1


@pytest.fixture
def products_list():
    return Product(name="Патифон", description="старый", price="123.3", quantity=3)


@pytest.fixture
def category_add(product_1, product_2, product_3):
    return Category(
        "оборудование",
        "музыкальный",
        [product_1, product_2, product_3],
    )


@pytest.fixture
def product__str__():
    return ("Барабан", "200 руб." "Остаток: 2 шт.")


@pytest.fixture
def category_01_(product_data, new_product, products_list):
    return Category(
        "оборудование",
        "музыкальный",
        [product_data, new_product, products_list],
    )


@pytest.fixture
def smartphone1():
    return Smartphone(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0,
        5,
        95.5,
        "S23 Ultra",
        256,
        "Серый",
    )


@pytest.fixture
def smartphone2():
    return Smartphone(
        "Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space"
    )


@pytest.fixture
def smartphone3():
    return Smartphone(
        "Xiaomi Redmi Note 11",
        "1024GB, Синий",
        31000.0,
        14,
        90.3,
        "Note 11",
        1024,
        "Синий",
    )


@pytest.fixture
def grass1():
    return LawnGrass(
        "Газонная трава",
        "Элитная трава для газона",
        500.0,
        20,
        "Россия",
        "7 дней",
        "Зеленый",
    )


@pytest.fixture
def grass2():
    return LawnGrass(
        "Газонная трава 2",
        "Выносливая трава",
        450.0,
        15,
        "США",
        "5 дней",
        "Темно-зеленый",
    )
