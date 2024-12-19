from src.product import Product


class Category:
    product_count = None
    name: str  # Название
    description: str  # Описание
    products: list  # Список товаров по категориям

    number_of_categories = 0  # Количество категорий
    number_of_products = 0  # Количество товаров

    def __init__(self, name, description, products):
        self.product_count = None
        self.name = name
        self.description = description
        self.__products = products

        Category.number_of_categories += 1
        Category.number_of_products += len(self.__products)

    def __str__(self):
        total_products = 0
        for product in self.__products:
            total_products += product.quantity
        return f"{self.name}, количество продуктов: {total_products} шт."

    @property
    def products(self):
        return self.__products

    @products.setter
    def products(self, products_new: Product):
        if isinstance(products_new, Product):
            self.__products.append(products_new)
            Category.product_count += 1
        else:
            raise TypeError

    def add_product(self, new_products: Product):
        self.__products.append(new_products)
        Category.number_of_products += 1

    @property
    def products_list(self):
        products_list = ""
        for product in self.__products:
            products_list += (
                f"{product.name}, {product.price} руб. Остаток: "
                f"{product.quantity} шт.\n"
            )
        return products_list
