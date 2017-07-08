import functools
from src.cart.product import Product

class Cart:
    products = []

    def get_total_price(self):
        add = lambda a,b : Product(f"adding ${a.name} ${b.name}", a.price + b.price)
        return functools.reduce(add, self.products, Product("Total", 0)).price

    def add(self, product, quantity=1):
        self.products = [product] * quantity        