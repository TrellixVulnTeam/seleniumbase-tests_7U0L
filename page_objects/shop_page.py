from seleniumbase import BaseCase


class ShopPage(BaseCase):
    input_for_product_search = "//input[@id='woocommerce-product-search-field-0']"
    search_button = "//button[@value='Search']"
    toys_img = "//img[@class='zoomImg']"

    def open_shop_page(self):
        self.open('https://practice.automationbro.com/shop/')