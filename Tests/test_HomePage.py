from Config.config import testData
from Tests.test_base import BaseTest
from Pages.homePage import HomePage
import pytest

class   Test_Homepage(BaseTest):

    def test_maquinaria_search_visible(self):
        self.homePage = HomePage(self.driver)
        flag = self.homePage.is_buscar_maquinaria_existe()
        assert flag


    def test_home_page_title(self):
        self.homePage = HomePage(self.driver)
        title = self.homePage.get_title(testData.WEBSITE_TITLE)
        assert title ==  testData.WEBSITE_TITLE

    #def test_buecar_maquinaria(self):
        #self.homePage = HomePage(self.driver)
        #self.homePage.is_buscar_maquinaria_existe()
        #lista_encontrada = self.homePage.get_list_of_values(testData.HTML_H_REF)
        # (Check the list before the search phrase for correct implicit waiting)

        #assert lista_encontrada