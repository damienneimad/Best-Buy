# Best Buy Store Management

This project is a simple command line application that demonstrates basic store
management concepts such as products, promotions and order processing.  It is an
educational example of applying object oriented programming in Python.

## Features

- **Products** – Regular items, non‑stocked items and limited products.
- **Promotions** – Percentage discounts, second item at half price and "buy 2
  get 1" deals.
- **Store Operations** – List products, show total quantity, place orders and
  combine stores using Python magic methods.
- **Tests** – Minimal tests for product behaviour using `pytest`.

## Installation

```bash
pip install -r requirements.txt  # only pytest is required
```

## Usage

Run the interactive store application:

```bash
python main.py
```

Run the tests:

```bash
pytest
```

## Project Structure

- `products.py` – Product classes and subclasses.
- `promotions.py` – Promotion classes.
- `store.py` – Store container and order logic.
- `main.py` – Example command line interface.
- `test_product.py` – Unit tests.

## License

MIT
