from typing import List, Tuple
from products import Product

class Store:
    def __init__(self, products: List[Product]):
        self.products = products

    def add_product(self, product: Product):
        self.products.append(product)

    def remove_product(self, product: Product):
        self.products.remove(product)

    def get_total_quantity(self) -> int:
        return sum(product.get_quantity() for product in self.products if product.is_active())

    def get_all_products(self) -> List[Product]:
        return [product for product in self.products if product.is_active()]

    def order(self, shopping_list: List[Tuple[Product, int]]) -> float:
        total_price = 0.0
        for product, quantity in shopping_list:
            if product.is_active() and quantity <= product.get_quantity():
                total_price += product.buy(quantity)
            else:
                raise ValueError(f"Cannot fulfill the order for {product.name}. Not enough quantity or product is inactive.")
        return total_price
