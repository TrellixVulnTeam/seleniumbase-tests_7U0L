from seleniumbase import BaseCase


class HomePage(BaseCase):
    logo = "//img[@class='logo']"
    installation_button = "//a[@class='reference internal' and contains(text(),'1. Installation')][1]"
    footer = "//div[@class='footer']"
    list_of_navigation = "//div[@class='sphinxsidebarwrapper']/ul/li"

    def open_page(self):
        self.open('https://selenium-python.readthedocs.io/index.html')