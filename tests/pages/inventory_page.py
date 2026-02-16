from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage:
    '''
    Page Object Model لصفحة المنتجات
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
        '''الحصول على عنوان الصفحة'''
        return self.driver.find_element(*self.PRODUCTS_TITLE).text

    def add_product_to_cart(self):
        '''إضافة منتج للسلة'''
        add_button = self.wait.until(
            EC.element_to_be_clickable(self.ADD_TO_CART_BUTTON)
        )
        add_button.click()
        
        # انتظر حتى يظهر شارة السلة برقم 1
        self.wait.until(
            EC.text_to_be_present_in_element(self.CART_BADGE, '1')
        )

    def get_cart_count(self):
        '''الحصول على عدد المنتجات في السلة'''
        try:
            element = self.wait.until(
                EC.visibility_of_element_located(self.CART_BADGE)
            )
            return element.text
        except:
            return '0'

    def click_cart(self):
        '''النقر على زر السلة'''
        self.driver.find_element(*self.CART_BUTTON).click()
