from page_objects.cart_page import CartPage
from selenium.webdriver.common.keys import Keys
import time

class CartTest(CartPage):
    def setUp(self):
        super().setUp()
        self.open('https://practice.automationbro.com/shop/')

    def test_add_to_cart(self):
        # add item to the cart
        self.click(self.add_to_cart)

        # assert product is in the cart
        self.assert_text('1', self.check_cart)

        # open Cart page
        self.open_cart_page()

        # get current subtotal
        price = self.get_text(self.get_subtotal)

        # add one more product and update cart
        self.set_value(self.product_quantity_input, '3')
        self.send_keys(self.product_quantity_input, Keys.RETURN)
        self.click(self.update_cart)

        # wait few seconds
        time.sleep(7)
        # self.wait_for_element_visible(self.loading_overlay)
        # self.wait_for_element_not_visible(self.loading_overlay)

        # assert price changed
        updated_price = self.get_text(self.get_subtotal)
        print(updated_price)
        self.assertNotEqual(price, updated_price)




