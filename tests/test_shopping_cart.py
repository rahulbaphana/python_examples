from cart.shopping_cart import Cart
from cart.product import Product

class TestShoppingCart:
    def test_empty_shopping_cart(self):
        assert Cart().display_all_items() == []

    def test_product_added_to_cart(self):
        cart = Cart();
        dove = Product("Dove", 30)
        cart.add(dove)
        assert cart.display_all_items()  == [dove]    