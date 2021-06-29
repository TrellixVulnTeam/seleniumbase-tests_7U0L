from seleniumbase import BaseCase
import time


class TestContact(BaseCase):
    def test_contact_page(self):
        self.open('https://practice.automationbro.com/contact/')

        self.scroll_to("//input[@id='evf-277-field_ys0GeZISRs-1']")
        self.save_screenshot('test', 'my_screenshots')

        self.send_keys("//input[@type='text'][1]", 'Anatol')
        self.send_keys("//input[@type='email']", 'test@gmail.com')
        self.send_keys(".contact-phone input", '0990890099')
        self.send_keys("//textarea[@id='evf-277-field_yhGx3FOwr2-4']", 'Hello from Ukraine')

        self.save_screenshot('test1', 'my_screenshots')
        self.click("//button[@type='submit']")
        self.assert_text('Thanks for contacting us! We will be in touch with you shortly', "//div[@role='alert']")
