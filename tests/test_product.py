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


    def test_product_str(self):
        product = Product("Ноутбук", "Игровой ноутбук", 50000, 10)
        expected = "Ноутбук, 50000 руб. Остаток: 10 шт."
        assert str(product) == expected

    def test_product_add_two_products(self):
        p1 = Product("Товар A", "Описание A", 100, 10)
        p2 = Product("Товар B", "Описание B", 200, 2)
        result = p1 + p2
        assert result == 1400

    def test_product_add_different_values(self):
        p1 = Product("Телефон", "Смартфон", 50000, 3)
        p2 = Product("Чехол", "Силиконовый", 1000, 10)
        result = p1 + p2
        assert result == 160000

    def test_product_add_with_non_product_raises_error(self):
        product = Product("Ноутбук", "Игровой", 50000, 5)

        with pytest.raises(TypeError, match="Нельзя сложить Product и int"):
            result = product + 100

        with pytest.raises(TypeError, match="Нельзя сложить Product и str"):
            result = product + "строка"

        with pytest.raises(TypeError, match="Нельзя сложить Product и NoneType"):
            result = product + None
