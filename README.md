# Online Store (OOP Version with Encapsulation)

A Python implementation of basic online store logic using an object-oriented approach. This version adds encapsulation of key attributes, getters and setters, a class method for creating products from dictionaries, abstract classes, mixins, and full test coverage.

## Classes

### Product

Stores product information:

- `name` — product name
- `description` — product description
- `__price` — price (private attribute)
- `quantity` — stock quantity

Features:

- Private price (`__price`) with `@property` access
- Setter with validation:
  - Price cannot be ≤ 0 (message displayed)
  - When lowering the price, user confirmation is requested (y/n)
- Class method `new_product`:
  - Creates a product from a dictionary
  - If a product with the same name exists, quantities are summed and the highest price is kept
- `__str__`: returns `Product name, 80 rub. Stock: 15 pcs.`
- `__add__`: adds two products by multiplying price × quantity for each and returning the sum

### Category

Stores category information:

- `name` — category name
- `description` — category description
- `__products` — private list of products

Features:

- Private product list (`__products`)
- Method `add_product` for adding a product
- Getter `products` that returns a list of formatted strings
- `__str__`: returns `Category name, product count: 30 pcs.`

## Inheritance

### Smartphone (inherits from Product)

Additional attributes:

- `efficiency` — performance
- `model` — model
- `memory` — internal memory
- `color` — color

### LawnGrass (inherits from Product)

Additional attributes:

- `country` — country of origin
- `germination_period` — germination period (days)
- `color` — color

### Type-safe addition

Products can only be added to products of the same class:

```python
phone1 + phone2   # ✅ works
grass1 + grass2   # ✅ works
phone + grass     # ❌ TypeError

Abstract Class and Mixin

BaseProduct (abstract class)

Parent class for all products. Defines required methods:

__str__ — string representation
__add__ — product addition
price — price getter (property)

LogMixin

Automatically logs object creation for Product, Smartphone, and LawnGrass:

text
Created Product object with parameters: ('Apple', 'Sweet', 80, 15)
Tech Stack

Python 3.x
pytest + pytest-cov (testing and coverage)
flake8 (code style)
isort (import ordering)
mypy (type checking)
coverage (coverage reports)
Running Tests and Linters

Run all commands from the project root.

Linters

bash
# Check import order
python3 -m isort --check-only .

# Auto-fix imports
python3 -m isort .

# Check code style
python3 -m flake8 .

# Type checking
python3 -m mypy .
Tests

bash
# Run tests
python3 -m pytest

# Run tests with coverage report
python3 -m pytest --cov=src --cov-report=term-missing
Project Structure

text
online_store/
│
├── src/
│   ├── __init__.py
│   ├── base_product.py
│   ├── product.py
│   ├── smartphone.py
│   ├── lawn_grass.py
│   ├── category.py
│   └── log_mixin.py
│
├── tests/
│   ├── __init__.py
│   ├── test_product.py
│   ├── test_smartphone.py
│   ├── test_lawn_grass.py
│   └── test_category.py
│
├── .flake8
├── .gitignore
├── requirements.txt
└── README.md
