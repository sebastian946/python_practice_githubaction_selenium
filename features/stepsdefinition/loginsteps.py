from utils.const import *
class Login:
    url = "https://www.saucedemo.com/"
    dictionary_user = {
        1: "",
        2: "",
        3: "",
        4: "",
        5: "",
        6: "",
        7: "error"
    }
    password = ""
    
    def __init__(self):
        self.password = ""
        self.input_username_id = "user-name"
        self.input_password_id = "password"
        self.button_login_id = "login-button"
        self.text_usercredentials_id = "login_credentials"
        self.text_password_credentials_classname = "login_password"
        self.text_title_classname = "app_logo"
        self.message_validate_xpath = "//h3[@data-test='error']"
        self.const = WebDriverUtils()
    
    def open_url(self):
        self.const.open_browser(self.url)
        self.const.wait(10)
    
    def get_text_user_credentials(self):
        texto = self.const.get_text_element('id',self.text_usercredentials_id)
        words = texto.split()
        usernames = [word for word in words if word.endswith("_user")]
        for i, username in enumerate(usernames, start=1):
            self.dictionary_user[i] = username
        print(self.dictionary_user)
            
    def get_text_password_credentials(self):
        texto = self.const.get_text_element('classname',self.text_password_credentials_classname)
        words = texto.splitlines()
        print(f'This is words: {words[1]}')
        self.password = words[1]
        
    
    def send_user(self, id):
        print('This is id:', id)
        user_id = int(id) 
        print(f'User:', self.dictionary_user.get(user_id))
        print(f'Password: {self.password}')
        self.const.send_text_element('id', self.input_username_id, self.dictionary_user.get(user_id))
        self.const.send_text_element('id', self.input_password_id, self.password)
        self.const.click_element('id', self.button_login_id)
        
    
    def validate_login(self):
        self.const.wait(10)
        title = self.const.get_text_element('classname',self.text_title_classname)
        return title
    
    def validate_message_error(self):
        self.const.wait(5)
        message = self.const.get_text_element('xpath', self.message_validate_xpath)
        return message

        