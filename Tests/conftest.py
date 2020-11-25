import pytest
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.firefox.firefox_profile import WEBDRIVER_EXT
from Pages.config import testData
from selenium import webdriver


@pytest.fixture(params=["chrome"], scope='class')
def init_driver(request):
    #web_driver = webdriver
    #if request.param == "chrome":
    web_driver = webdriver.Chrome()
    #if request.param == "firefox":
    #    web_driver = webdriver.Firefox()
    request.cls.driver = web_driver
    yield
    web_driver.quit()

#def browser():
    #b = webdriver.Firefox()
    #b.implicitly_wait(10)
    #yield b
    #b.quit()