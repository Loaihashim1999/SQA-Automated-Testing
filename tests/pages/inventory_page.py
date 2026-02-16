from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

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
        try:
            add_button = self.wait.until(
                EC.element_to_be_clickable(self.ADD_TO_CART_BUTTON)
            )
            add_button.click()
            # انتظر قليلاً حتى يتم تحديث واجهة المستخدم
            time.sleep(1)
        except Exception as e:
            raise Exception(f'Failed to add product to cart: {str(e)}')

    def get_cart_count(self):
        '''الحصول على عدد المنتجات في السلة'''
        try:
            element = self.wait.until(
                EC.visibility_of_element_located(self.CART_BADGE)
            )
            count = element.text
            return count if count else '0'
        except:
            return '0'

    def click_cart(self):
        '''النقر على زر السلة'''
        self.driver.find_element(*self.CART_BUTTON).click()
