from Config.config import testData
from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage

class   HomePage(BasePage):

    EMAIL = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login")
    OLVIDASTE_PASSWORD = (By.LINK_TEXT, "¿Olvidaste la contraseña?")
    CREAR_CUENTA_LINK = (By.LINK_TEXT, "Crear Cuenta") 
    BUSCAR_MAQUINARIA_INPUT = (By.ID, "equipment-query") 
    MAQUINARIA_ENCONTRADA = (By.LINK_TEXT, testData.MAQUINARIA_VALIDA) 


    def __init__(self, driver):
        super().__init__(driver)
        #self.driver = driver
        self.driver.get(testData.BASE_URL)
        

    def load_page(self):
        self.driver.get(testData.BASE_URL)


    def get_home_page_title(self, title):
        return self.get_title(title)


    def is_buscar_maquinaria_existe(self):
        return self.is_visible(self.BUSCAR_MAQUINARIA_INPUT)


    def buscar_maquinaria_valida(self):
        self.do_send_keys(testData.MAQUINARIA_VALIDA)
        self.get_list_of_values()