
# 基礎篇 ----------------------------------------------------------------

from selenium import webdriver


driver = webdriver.Chrome()
driver.get('https://www.python.org/')
driver.maximize_window()
driver.implicitly_wait(30)

driver.find_element_by_xpath('//*[@id="id-search-field"]').send_keys('Hello')
driver.find_element_by_xpath('//*[@id="submit"]').click()

#driver.quit()


# NeePageElement --------------------------------------------------------

from selenium.webdriver import Chrome
from poium import NewPageElement,Page
import time


driver = Chrome()
driver.get('https://www.python.org/')
time.sleep(3)


class test (Page):
    inp = NewPageElement(xpath='//*[@id="id-search-field"]',describe='輸入視窗')
    search = NewPageElement(xpath='//*[@id="submit"]',describe='點選搜尋')


def abc ( a ):
    t = test(driver) # 必須帶上 driver
    t.inp = a
    t.search.click()

abc ( 'hello python' )