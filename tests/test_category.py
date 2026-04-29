import pytest

from src.category import Category
from src.product import LawnGrass, Product, Smartphone


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

    def test_category_str_with_products(self):
        """Проверка строкового отображения категории с продуктами"""
        p1 = Product("Яблоко", "Сочное", 80, 15)
        p2 = Product("Банан", "Сладкий", 120, 10)
        p3 = Product("Апельсин", "Солнечный", 100, 5)
        category = Category("Фрукты", "Вкусные фрукты", [p1, p2, p3])

        expected = "Фрукты, количество продуктов: 30 шт."
        assert str(category) == expected

    def test_category_str_empty(self):
        """Проверка строкового отображения пустой категории"""
        category = Category("Пустая", "Ничего нет", [])
        expected = "Пустая, количество продуктов: 0 шт."
        assert str(category) == expected

    def test_category_str_after_adding_product(self):
        """Проверка, что __str__ обновляется после добавления продукта"""
        category = Category("Электроника", "Гаджеты", [])
        assert str(category) == "Электроника, количество продуктов: 0 шт."

        product = Product("Ноутбук", "Игровой", 50000, 3)
        category.add_product(product)
        assert str(category) == "Электроника, количество продуктов: 3 шт."


class TestCategoryAddProductInheritance:
    def test_add_product_works(self):
        category = Category("Техника", "Разная", [])
        phone = Smartphone(
            "iPhone", "", 80000, 10, "A17", "15", "256", "черный"
        )
        category.add_product(phone)
        assert len(category.products) == 1

    def test_add_smartphone_to_category(self):
        category = Category("Смартфоны", "Мобильные устройства", [])
        phone = Smartphone(
            "iPhone", "", 80000, 10, "A17", "15", "256", "черный"
        )
        category.add_product(phone)
        assert "iPhone" in category.products[0]

    def test_add_lawn_grass_to_category(self):
        category = Category("Садовые товары", "Для сада", [])
        grass = LawnGrass(
            "Трава", "", 500, 100, "Россия", 14, "зеленый"
        )
        category.add_product(grass)
        assert "Трава" in category.products[0]

    def test_add_non_product_raises_error(self):
        category = Category("Техника", "Разная", [])
        with pytest.raises(TypeError, match="Можно добавить только объекты Product или его наследников"):
            category.add_product("не продукт")

    def test_add_int_raises_error(self):
        category = Category("Техника", "Разная", [])
        with pytest.raises(TypeError, match="Можно добавить только объекты Product или его наследников"):
            category.add_product(123)

    def test_add_list_raises_error(self):
        category = Category("Техника", "Разная", [])
        with pytest.raises(TypeError, match="Можно добавить только объекты Product или его наследников"):
            category.add_product([1, 2, 3])


class TestCategoryMiddlePrice:
    def test_middle_price_with_products(self):
        category = Category("Тест", "Описание", [])
        category.add_product(Product("Товар1", "", 100, 5))
        category.add_product(Product("Товар2", "", 200, 10))
        assert category.middle_price() == 150

    def test_middle_price_empty_category(self):
        category = Category("Пустая", "Нет товаров", [])
        assert category.middle_price() == 0

    def test_middle_price_one_product(self):
        category = Category("Один товар", "Тест", [])
        category.add_product(Product("Товар", "", 300, 5))
        assert category.middle_price() == 300
