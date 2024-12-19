import pytest

from src.category import Category
from src.product import Product


def test_category_init(category_1):
    assert category_1.name == "оборудование"
    assert category_1.description == "музыкальный"
    assert category_1.products == ["магнитола", "плеер"]


def test_category2(category_2):
    assert category_2.name == "мебель"
    assert category_2.description == "для спальни"
    assert category_2.products == ["кровать", "диван"]

    assert category_2.number_of_categories == 2
    assert category_2.number_of_products == 4


def test_category3(category_3):
    assert category_3.name == ""
    assert category_3.description == ""
    assert category_3.products == [""]


def test_category_property(category_1):
    assert category_1.name == "оборудование"
    assert category_1.description == "музыкальный"
    assert category_1.products == ["магнитола", "плеер"]


def test_add_product(category_add, product_1):
    category_add.add_product(product_1)
    assert Category.number_of_products == 4


def test_products_list(product_1):
    assert product_1.name == "Патифон"
    assert product_1.description == "старый"
    assert product_1.price == "123.3"
    assert product_1.quantity == "3"


def test_products_list_(products_list):
    assert Product(name="Патифон", description="старый", price="123.3", quantity="3")


def test__str__(category_01_):
    assert str(category_01_) == "оборудование, количество продуктов: 7 шт."
