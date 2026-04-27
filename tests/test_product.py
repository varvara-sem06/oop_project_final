import pytest

from src.product import Product


class TestProduct:
    def test_private_price_attribute(self):
        product = Product("Laptop", "Gaming laptop", 50000, 10)
        with pytest.raises(AttributeError):
            product.__price
        assert product.price == 50000

    def test_price_getter(self):
        product = Product("Phone", "Smartphone", 30000, 5)
        assert product.price == 30000

    def test_price_setter_zero(self, capsys):
        product = Product("Laptop", "Gaming laptop", 50000, 10)
        product.price = 0
        captured = capsys.readouterr()
        assert "Цена не должна быть нулевая или отрицательная" in captured.out
        assert product.price == 50000

    def test_price_setter_negative(self, capsys):
        product = Product("Laptop", "Gaming laptop", 50000, 10)
        product.price = -100
        captured = capsys.readouterr()
        assert "Цена не должна быть нулевая или отрицательная" in captured.out
        assert product.price == 50000

    def test_classmethod_new_product_basic(self):
        product_data = {
            "name": "Phone",
            "description": "Smartphone",
            "price": 30000,
            "quantity": 5
        }
        product = Product.new_product(product_data)
        assert product.name == "Phone"
        assert product.description == "Smartphone"
        assert product.price == 30000
        assert product.quantity == 5

    def test_classmethod_new_product_no_duplicate(self):
        existing = Product("Phone", "Smartphone", 30000, 5)
        product_data = {
            "name": "Laptop",
            "description": "Gaming laptop",
            "price": 50000,
            "quantity": 3
        }
        result = Product.new_product(product_data, [existing])
        assert result is not existing
        assert result.name == "Laptop"
        assert result.price == 50000
        assert result.quantity == 3
