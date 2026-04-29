import pytest

from src.base_product import BaseProduct
from src.product import LawnGrass, Product, Smartphone


class TestBaseProduct:
    def test_cannot_instantiate_abstract_class(self):
        """Проверка, что нельзя создать экземпляр абстрактного класса"""
        with pytest.raises(TypeError):
            BaseProduct()  # Должна быть ошибка

    def test_product_is_instance_of_base_product(self):
        """Проверка, что Product является наследником BaseProduct"""
        product = Product("Товар", "Описание", 100, 5)
        assert isinstance(product, BaseProduct)

    def test_smartphone_is_instance_of_base_product(self):
        """Проверка, что Smartphone является наследником BaseProduct"""
        phone = Smartphone(
            "iPhone", "Флагман", 80000, 10,
            "A17", "15", "256GB", "черный"
        )
        assert isinstance(phone, BaseProduct)

    def test_lawn_grass_is_instance_of_base_product(self):
        """Проверка, что LawnGrass является наследником BaseProduct"""
        grass = LawnGrass(
            "Трава", "Для газона", 500, 100,
            "Россия", 14, "зеленый"
        )
        assert isinstance(grass, BaseProduct)
import pytest

from src.base_product import BaseProduct
from src.product import LawnGrass, Product, Smartphone


class TestBaseProduct:
    def test_cannot_instantiate_abstract_class(self):
        """Проверка, что нельзя создать экземпляр абстрактного класса"""
        with pytest.raises(TypeError):
            BaseProduct()  # Должна быть ошибка

    def test_product_is_instance_of_base_product(self):
        """Проверка, что Product является наследником BaseProduct"""
        product = Product("Товар", "Описание", 100, 5)
        assert isinstance(product, BaseProduct)

    def test_smartphone_is_instance_of_base_product(self):
        """Проверка, что Smartphone является наследником BaseProduct"""
        phone = Smartphone(
            "iPhone", "Флагман", 80000, 10,
            "A17", "15", "256GB", "черный"
        )
        assert isinstance(phone, BaseProduct)

    def test_lawn_grass_is_instance_of_base_product(self):
        """Проверка, что LawnGrass является наследником BaseProduct"""
        grass = LawnGrass(
            "Трава", "Для газона", 500, 100,
            "Россия", 14, "зеленый"
        )
        assert isinstance(grass, BaseProduct)
