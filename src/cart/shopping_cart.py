class Cart:
    products = []

    def display_all_items(self):
        return self.products

    def add(self, product):
        self.products.append(product)    