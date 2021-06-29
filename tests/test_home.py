from page_objects.home_page import HomePage


class HomeTest(HomePage):
    def test_home_page(self):
        # go to page
        self.open_page()
        # self.go_to('https://selenium-python.readthedocs.io/index.html')
        # assert title
        self.assert_title('Selenium with Python — Selenium Python Bindings 2 documentation')

        # assert logo
        self.assert_element(HomePage.logo)

        # click button  and assert url
        self.click(HomePage.installation_button)
        install_url = self.get_current_url()
        self.assert_equal(install_url, 'https://selenium-python.readthedocs.io/installation.html')

        # get text
        self.assert_text('1.1. Introduction', 'h2')

        # ex
        self.scroll_to_bottom()
        self.assert_text('©2011-2018, Baiju Muthukadan. | Powered by Sphinx 1.8.5 & Alabaster 0.7.12 | Page source',
                         HomePage.footer)

    def test_menu_links(self):
        expected_links = ['1. Installation', '2. Getting Started', '3. Navigating', '4. Locating Elements',
                          '5. Waits', '6. Page Objects', '7. WebDriver API',
                          '8. Appendix: Frequently Asked Questions']
        self.open_page()
        # self.open('https://selenium-python.readthedocs.io/index.html')

        el = self.find_elements(HomePage.list_of_navigation)

        for inx, link in enumerate(el):
            self.assertEqual(expected_links[inx], link.text)
            print(inx, link.text)











