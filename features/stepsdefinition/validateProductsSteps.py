from utils.const import *
class ValidateProducts:
    
    dictionary_products =[{
        "title": "",
        "description": "",
        "price": "",
    }]
    
    def __init__(self):
        self.list_products_class = "//div[@class='inventory_item']"
        self.const = WebDriverUtils()
        
        
    def get_all_products(self):
        self.const.wait(10)
        elements = self.const.get_elements('xpath',self.list_products_class)
        print(elements)