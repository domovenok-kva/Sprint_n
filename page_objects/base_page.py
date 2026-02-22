from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains 

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    #Клик по элементу
    def click_element(self, locator):
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(locator)).click()

    #Ввод значения в инпут
    def fill_inpt(self, locator, data_in):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(locator)).send_keys(data_in)

    #Получить URL
    def page_url(self):
        return self.driver.current_url
    
    #Видимость элемента
    def element_visability(self, locator):
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
        self.driver.implicitly_wait(10)
        element  = self.driver.find_element(*locator)
        action = ActionChains(self.driver).move_to_element(element)
        action.perform()

    #Элемент кликабелен
    def element_is_clickable(self, locator):
        return  WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(locator))


