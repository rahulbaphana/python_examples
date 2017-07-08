import functools

class Cart:
    products = []

    def get_total_price(self):
        add = lambda a,b : a + b
        return functools.reduce(add, [product.price for product in self.products], 0)

    def add(self, product, quantity=1):
        self.products = [product] * quantity        