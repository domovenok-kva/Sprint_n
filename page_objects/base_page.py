from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException 
import re

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    #Клик по элементу
    def click_element(self, locator):
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(locator)).click()

    #Ввод значения в инпут
    def fill_inpt(self, locator, data_in):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(locator)).send_keys(data_in)
    
    #Видимость элемента
    def element_visability(self, locator):
        self.driver.implicitly_wait(40)
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
    
    #Получить значение элемента
    def get_element_value(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).text
    
    #Поиск элемента
    def find_element(self, locator):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)
    
    #Ховер
    def hover_on_elem(self, locator):
        try:
            element = self.find_element(locator) 
            is_visible = element.is_displayed()
            if is_visible:
                self.driver.implicitly_wait(10)
                element  = self.driver.find_element(*locator)
                action = ActionChains(self.driver).move_to_element(element)
                action.perform()
            return is_visible
        except NoSuchElementException:
            return False
        

    #Элемент кликабелен
    def element_is_clickable(self, locator):
        return  WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(locator))
    
    #Проверка активности 
    def element_is_acive(self, locator):
        try:
            element = self.find_element(locator) 
            is_visible = element.is_displayed()
            if is_visible:
                self.element_visability(locator)
            return is_visible
        except NoSuchElementException:
            return False
        
    #Получаем цену
    def get_the_price(self, locator, patternn):
        try:
            element = self.find_element(locator)
            text = element.text.strip()
            match = re.search(patternn, text, re.IGNORECASE)
            if match:
                return int(match.group(1))
            else:
                return None
        except NoSuchElementException:
            return None


