from seleniumbase import BaseCase


class CartPage(BaseCase):
    add_to_cart = "//a[@href='?add-to-cart=374']"
    check_cart = "//a[@class='cart-page-link']/span[1]"
    get_subtotal = "//td[@class='product-subtotal']"
    product_quantity_input = "//input[@class='input-text qty text']"
    update_cart = "//button[@name='update_cart']"
    loading_overlay = ".woocommerce-cart-form div[@class*='blockOverlay']"

    def open_cart_page(self):
        self.open('https://practice.automationbro.com/cart/')