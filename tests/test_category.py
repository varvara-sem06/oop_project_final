import pytest

from src.category import Category
from src.product import Product


class TestCategory:
    def test_private_products_attribute(self):
        category = Category("Electronics", "Devices", [])
        with pytest.raises(AttributeError):
            category.__products
        assert category.products == []

    def test_add_product_single(self):
        category = Category("Electronics", "Devices", [])
        product = Product("Laptop", "Gaming laptop", 50000, 10)
        category.add_product(product)
        assert len(category.products) == 1
        assert "Laptop" in category.products[0]
        assert "50000" in category.products[0]
        assert "10" in category.products[0]

    def test_add_product_multiple(self):
        category = Category("Electronics", "Devices", [])
        product1 = Product("Laptop", "Gaming laptop", 50000, 10)
        product2 = Product("Mouse", "Wireless mouse", 800, 25)
        product3 = Product("Keyboard", "Mechanical keyboard", 2000, 15)
        category.add_product(product1)
        category.add_product(product2)
        category.add_product(product3)
        assert len(category.products) == 3

    def test_products_getter_format(self):
        category = Category("Electronics", "Devices", [])
        product = Product("Laptop", "Gaming laptop", 50000, 10)
        category.add_product(product)
        expected = "Laptop, 50000 руб. Остаток: 10 шт."
        assert category.products[0] == expected
