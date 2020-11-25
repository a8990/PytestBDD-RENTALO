from Config.config import testData
from selenium.webdriver import ActionChains
from selenium.webdriver.support.expected_conditions import element_to_be_clickable, element_to_be_selected
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 

"""This Class is the PArent of all pages"""
"""It contains all the generic methods and utilities for all the pages"""

class      BasePage():

    
    def __init__(self, driver):
        self.driver = driver


    def do_click(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

    
    def do_send_keys(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).do_send_keys(text)


    def get_element_text(self, by_locator):
        element =  WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element.text


    def is_visible(self, by_locator):
        element =  WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return bool(element)


    def get_title(self, title):
        element =  WebDriverWait(self.driver, 10).until(EC.title_is(title))
        return self.driver.title 


    def get_list_of_values(self, by_locator):
        #element_to_be_selected = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(by_locator))
        links_div = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        #browser.find_element_by_id('links')
        return bool(links_div)