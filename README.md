# Best-Buy

# Best Buy Store Management

This project implements a store management system for Best Buy, allowing you to manage products, apply promotions, and process orders. The project demonstrates the use of Object-Oriented Programming (OOP) principles including inheritance, polymorphism, and encapsulation in Python.

## Features

- **Product Management**: Create and manage different types of products (physical, non-stocked, limited).
- **Promotions**: Apply various promotions to products (percentage discount, second item at half price, buy 2 get 1 free).
- **Store Operations**: List products, show total quantity, make orders, and combine stores.
- **Magic Methods and Properties**: Use of Python properties, comparison operators, and other magic methods for enhanced functionality.

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/best-buy-store-management.git
    cd best-buy-store-management
    ```

2. **Install dependencies**:
    The project uses `pytest` for testing. You can install it using:
    ```bash
    pip install pytest
    ```

### Running the Application

To start the store management application, run the `main.py` file:
```bash
python main.py
Testing
To run the tests for the Product class, execute:

bash
pytest test_product.py
Project Structure
products.py: Contains the Product class and its subclasses (NonStockedProduct, LimitedProduct).
promotions.py: Contains the Promotion abstract class and its subclasses (PercentDiscount, SecondHalfPrice, ThirdOneFree).
store.py: Contains the Store class for managing products and processing orders.
main.py: Entry point for the application. Sets up initial products, promotions, and starts the user interface.
test_product.py: Contains unit tests for the Product class.

License
This project is licensed under the MIT License.

