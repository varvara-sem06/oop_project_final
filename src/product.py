class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

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
