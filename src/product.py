from src.base_product import BaseProduct


class LogMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print(f"Создан объект {self.__class__.__name__} с параметрами: {args}")

class Product(BaseProduct, LogMixin):
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        LogMixin.__init__(self)
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if not isinstance(other, Product):
            raise TypeError(f"Нельзя сложить Product и {type(other).__name__}")

        if type(self) != type(other):
            raise TypeError(f"Нельзя сложить {type(self).__name__} и {type(other).__name__}")
        total_self = self.price * self.quantity
        total_other = other.price * other.quantity
        return total_self + total_other

    @property
    def price(self):
        """ Геттер для цены """
        return self.__price

    @price.setter
    def price(self, new_price):
        """ Сеттер для цены с проверкой и подтверждением"""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return

        if new_price < self.__price:
            answer = input(f"Цена понижается с {self.__price} до {new_price}. Вы согласны? (y/n): ")
            if answer.lower() != "y":
                print("Изменение цены отменено")
                return

            self.__price = new_price
            


    @classmethod
    def new_product(cls, product_dict, existing_products=None):
        if existing_products is None:
            existing_products = []

        for product in existing_products:
            if product.name.lower() == product_dict["name"].lower():
                new_quantity = product.quantity + product_dict["quantity"]
                new_price = max(product.price, product_dict["price"])

                product.quantity = new_quantity
                product.price = new_price
                return product

        return cls(
            name=product_dict["name"],
            description=product_dict["description"],
            price=product_dict["price"],
            quantity=product_dict["quantity"]
        )


class Smartphone(Product):
    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

class LawnGrass(Product):
    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
