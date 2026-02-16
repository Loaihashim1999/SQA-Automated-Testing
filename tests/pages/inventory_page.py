from selenium.webdriver.common.by import By

class InventoryPage:
    '''
    Page Object Model ????? ????????
    '''
    
    # Locators
    PRODUCTS_TITLE = (By.CLASS_NAME, 'title')
    ADD_TO_CART_BUTTON = (By.ID, 'add-to-cart-sauce-labs-backpack')
    CART_BADGE = (By.CLASS_NAME, 'shopping_cart_badge')
    
    def __init__(self, driver):
        self.driver = driver
    
    def get_title(self):
        '''?????? ??? ????? ??????'''
        return self.driver.find_element(*self.PRODUCTS_TITLE).text
    
    def add_product_to_cart(self):
        '''????? ???? ?????'''
        self.driver.find_element(*self.ADD_TO_CART_BUTTON).click()
    
    def get_cart_count(self):
        '''?????? ??? ??? ???????? ?? ?????'''
        return self.driver.find_element(*self.CART_BADGE).text

