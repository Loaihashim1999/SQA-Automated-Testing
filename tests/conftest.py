import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver():
    '''
    إعداد المتصفح قبل كل اختبار وإغلاقه بعد الانتهاء
    '''
    options = Options()
    
    # تفعيل وضع Headless للـ CI
    if os.getenv('CI'):
        options.add_argument('--headless=new')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--disable-gpu')
        options.add_argument('--window-size=1920,1080')
    else:
        options.add_argument('--start-maximized')
    
    # استخدام Selenium Manager المدمج (لا يحتاج webdriver-manager)
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    
    yield driver
    
    driver.quit()

@pytest.fixture
def base_url():
    '''
    رابط الموقع الأساسي
    '''
    return 'https://www.saucedemo.com/'