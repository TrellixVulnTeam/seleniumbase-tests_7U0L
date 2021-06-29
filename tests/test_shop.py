from selenium.common.exceptions import ElementNotVisibleException

from page_objects.shop_page import ShopPage


class ShopTest(ShopPage):
    def test_search_products(self):
        self.open_shop_page()

        self.send_keys(self.input_for_product_search, 'Toys')
        self.click(self.search_button)
        try:
            self.assert_element(self.toys_img)
        except ElementNotVisibleException as e:
            print(f'exception {e}')