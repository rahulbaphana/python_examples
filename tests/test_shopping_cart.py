from src.cart.shopping_cart import Cart
from src.cart.product import Product

class TestShoppingCart:
    def test_empty_shopping_cart(self):
        # Given().When() == Then(Condition)
        assert Cart().get_total_price() == 0

    def test_product_added_to_cart(self):
        #  Given
        cart = Cart();
        dove = Product("Dove", 30)

        # When
        cart.add(dove)

        #Then
        assert cart.get_total_price()  == 30

    def test_product_added_to_cart_with_quantity(self):
        # Given
        cart = Cart();
        dove = Product("Dove", 30)

        # When
        cart.add(dove, 3)

        #Then
        assert cart.get_total_price() == 90    