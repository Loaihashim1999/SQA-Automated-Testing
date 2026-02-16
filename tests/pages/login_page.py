from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    '''
    Page Object Model لصفحة تسجيل الدخول
    '''
    
    # Locators
    USERNAME_FIELD = (By.ID, 'user-name')
    PASSWORD_FIELD = (By.ID, 'password')
    LOGIN_BUTTON = (By.ID, 'login-button')
    ERROR_MESSAGE = (By.CSS_SELECTOR, '[data-test="error"]')
    PRODUCTS_CONTAINER = (By.ID, 'inventory_container')
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def open(self, base_url):
        '''فتح صفحة تسجيل الدخول'''
        self.driver.get(base_url)
    
    def enter_username(self, username):
        '''إدخال اسم المستخدم'''
        self.driver.find_element(*self.USERNAME_FIELD).send_keys(username)
    
    def enter_password(self, password):
        '''إدخال كلمة المرور'''
        self.driver.find_element(*self.PASSWORD_FIELD).send_keys(password)
    
    def click_login(self):
        '''النقر على زر تسجيل الدخول'''
        self.driver.find_element(*self.LOGIN_BUTTON).click()
    
    def get_error_message(self):
        '''الحصول على رسالة الخطأ'''
        try:
            return self.driver.find_element(*self.ERROR_MESSAGE).text
        except:
            return ''
    
    def is_logged_in(self):
        '''التحقق من نجاح تسجيل الدخول'''
        try:
            element = self.wait.until(
                EC.visibility_of_element_located(self.PRODUCTS_CONTAINER)
            )
            return element.is_displayed()
        except:
            return False