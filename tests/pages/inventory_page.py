from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage:
    '''
    Page Object Model ????? ????????
    '''
    
    # Locators
    PRODUCTS_TITLE = (By.CLASS_NAME, 'title')
    ADD_TO_CART_BUTTON = (By.ID, 'add-to-cart-sauce-labs-backpack')
    CART_BADGE = (By.CSS_SELECTOR, 'span.shopping_cart_badge')
    CART_BUTTON = (By.CLASS_NAME, 'shopping_cart_link')
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def get_title(self):
        '''?????? ??? ????? ??????'''
        return self.driver.find_element(*self.PRODUCTS_TITLE).text
    
    def add_product_to_cart(self):
        '''????? ???? ?????'''
        self.driver.find_element(*self.ADD_TO_CART_BUTTON).click()
    
    def get_cart_count(self):
        '''?????? ??? ??? ???????? ?? ????? ?? ??????'''
        try:
            # ?????? ???? ?????? ????????
            element = self.wait.until(
                EC.visibility_of_element_located(self.CART_BADGE)
            )
            return element.text
        except:
            return '0'
    
    def click_cart(self):
        '''????? ??? ?? ?????'''
        self.driver.find_element(*self.CART_BUTTON).click()
