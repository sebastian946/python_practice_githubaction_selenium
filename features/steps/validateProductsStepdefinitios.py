
from behave import *
from stepsdefinition.validateProductsSteps import *

validate = ValidateProducts()
@when('get all products')
def step_impl(context):
    validate.get_all_products()