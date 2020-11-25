from Config.config import testData
from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage

class   LoginPage(BasePage):

    EMAIL = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login")
    OLVIDASTE_PASSWORD = (By.LINK_TEXT, "¿Olvidaste la contraseña?")
    CREAR_CUENTA_LINK = (By.LINK_TEXT, "Crear Cuenta") 

    def __init__(self, driver):
        super().__init__(driver)
        #self.driver = driver
        self.driver.get(testData.BASE_URL)
        

    def load_page(self):
        self.driver.get(testData.BASE_URL)
    
    def get_login_page_title(self, title):
        self.get_title(title)


    def is_crearcuenta_link_exist(self):
        self.is_visible(self.CREAR_CUENTA_LINK)


    def do_login(self, username, password):
        self.do_send_keys(self.EMAIL, username)
        self.do_send_keys(self.PASSWORD, password)
        self.do_click(self.LOGIN_BUTTON)

        