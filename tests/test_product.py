def test_product_init(product_1):
    assert product_1.name == "Патифон"
    assert product_1.description == "старый"
    assert product_1.price == "123.3"
    assert product_1.quantity == "3"


def test_product2(product_2):
    assert product_2.name == "777"
    assert product_2.description == ""
    assert product_2.price == "123.3"
    assert product_2.quantity == ""


def test_product3(product_3):
    assert product_3.name == ""
    assert product_3.description == ""
    assert product_3.price == ""
    assert product_3.quantity == ""
