from seleniumbase import BaseCase


class UploadTest(BaseCase):
    def test_visible_upload(self):
        self.open('https://the-internet.herokuapp.com/upload')
        file_path = './data/test.png'
        self.choose_file('//input[@id="file-upload"]', file_path)
        self.click("//input[@id='file-submit']")
        self.assert_text('File Uploaded', 'h3')

    def test_hidden_upload(self):
        self.open('https://practice.automationbro.com/cart/')
        file_path = './data/test.png'
        remove_hidden_class = 'document.getElementById("upfile_1").classList.remove("file_input_hidden")'
        self.add_js_code(remove_hidden_class)
        self.choose_file("//input[@name='uploadedfile_1']", file_path)
        self.click('#upload_1')
        self.assert_text('uploaded successfully', "//label[@id='wfu_messageblock_header_1_label_1']")




