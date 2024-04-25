from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException

class WebDriverUtils:
    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--headless')
        self.driver = webdriver.Chrome(options=self.options)
        self.locator = {
            'id': By.ID,
            'css': By.CSS_SELECTOR,
            'linktext': By.LINK_TEXT,
            'xpath': By.XPATH,
            'classname': By.CLASS_NAME
        }

    def open_browser(self, url):
        try:
            self.driver.get(url)
            self.driver.maximize_window()
        except Exception as e:
            print(f'Something gone wrong: {e}')

    def click_element(self, typelocator, path_locator):
        try:
            find_locator = self.locator.get(typelocator)
            self.driver.find_element(find_locator, path_locator).click()
        except ElementClickInterceptedException as e:
            print(f'This is the error: {e}')

    def wait(self, time):
        self.driver.implicitly_wait(time)

    def get_elements(self, typelocator, path_locator):
        try:
            find_locator = self.locator.get(typelocator)
            elements = self.driver.find_elements(find_locator, path_locator)
            for element in elements:
                print(element.text)
            return elements
        except InterruptedError as e:
            print(f'This is the error: {e}')

    def get_text_element(self, typelocator, path_locator):
        try:
            find_locator = self.locator.get(typelocator)
            text = self.driver.find_element(find_locator, path_locator).text
            print(f'This is text: {text}')
            return text
        except NoSuchElementException as e:
            print(f'Don´t found element: {e}')

    def send_text_element(self, typelocator, path_locator, text_to_send):
        try:
            find_locator = self.locator.get(typelocator)
            self.driver.find_element(find_locator, path_locator).send_keys(text_to_send)
        except NoSuchElementException as e:
            print(f'Can´t send the key: {e}')

    @staticmethod
    def assert_elements(text_get, text_to_compare):
        return text_get == text_to_compare

