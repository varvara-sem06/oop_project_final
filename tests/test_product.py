import pytest

from src.product import LawnGrass, Product, Smartphone


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

class TestSmartphone:
    def test_smartphone_creation(self):
        phone = Smartphone(
            "iPhone 15", "Флагман", 80000, 10,
            "A17 Pro", "15 Pro", "256GB", "черный"
        )
        assert phone.name == "iPhone 15"
        assert phone.description == "Флагман"
        assert phone.price == 80000
        assert phone.quantity == 10
        assert phone.efficiency == "A17 Pro"
        assert phone.model == "15 Pro"
        assert phone.memory == "256GB"
        assert phone.color == "черный"


class TestLawnGrass:
    def test_lawn_grass_creation(self):
        grass = LawnGrass(
            "Газонная трава", "Для газона", 500, 100,
            "Россия", 14, "зеленый"
        )
        assert grass.name == "Газонная трава"
        assert grass.description == "Для газона"
        assert grass.price == 500
        assert grass.quantity == 100
        assert grass.country == "Россия"
        assert grass.germination_period == 14
        assert grass.color == "зеленый"


class TestProductAddInheritance:
    def test_add_same_class_smartphone(self):
        phone1 = Smartphone(
            "iPhone", "", 80000, 10, "A17", "15", "256", "черный"
        )
        phone2 = Smartphone(
            "Samsung", "", 70000, 5, "Exynos", "S23", "128", "белый"
        )
        result = phone1 + phone2
        assert result == 80000 * 10 + 70000 * 5

    def test_add_same_class_lawn_grass(self):
        grass1 = LawnGrass(
            "Трава А", "", 500, 100, "Россия", 14, "зеленый"
        )
        grass2 = LawnGrass(
            "Трава Б", "", 600, 50, "Россия", 14, "зеленый"
        )
        result = grass1 + grass2
        assert result == 500 * 100 + 600 * 50

    def test_add_different_classes_raises_error(self):
        phone = Smartphone(
            "iPhone", "", 80000, 10, "A17", "15", "256", "черный"
        )
        grass = LawnGrass(
            "Трава", "", 500, 100, "Россия", 14, "зеленый"
        )
        with pytest.raises(TypeError, match="Нельзя сложить Smartphone и LawnGrass"):
            phone + grass
