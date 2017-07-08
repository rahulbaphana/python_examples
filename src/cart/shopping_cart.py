class Cart:
    products = []

    def get_total_price(self):
        add = lambda a,b : a + b
        sum = 0
        for product in self.products:
            sum = sum + product.price 
        return sum

    def add(self, product, quantity=1):
        self.products = [product] * quantity        