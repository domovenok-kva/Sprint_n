import allure
import re
from selenium.common.exceptions import NoSuchElementException
from locators.locators import Locators
from page_objects.base_page import BasePage

class RoutePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Заполнить поле Откуда")
    def fillin_from_adress_inpt(self, from_adress):
        self.fill_inpt(Locators.from_inpt, from_adress)

    @allure.step("Заполнить поле Куда")
    def fillin_where_adress_inpt(self, where_adress):
        self.fill_inpt(Locators.to_inpt, where_adress)

    @allure.step("Видимость начальной точки маршрута")
    def the_start_point_is_visible(self):
        try:
            element = self.find_element(Locators.pin_a) 
            is_visible = element.is_displayed()
            if is_visible:
                self.hover_on_elem(Locators.pin_a)
            return is_visible
        except NoSuchElementException:
            return False
    
    @allure.step("Видимость конечной точки маршрута")
    def the_end_point_is_visible(self):
        try:
            element = self.find_element(Locators.pin_b) 
            is_visible = element.is_displayed()
            if is_visible:
                self.hover_on_elem(Locators.pin_b)
            return is_visible
        except NoSuchElementException:
            return False
        
    @allure.step("Видимость блока с выбором маршрута")
    def block_with_route_types_is_visible(self):
        return self.find_element(Locators.picker_of_types)
    
    @allure.step("Видимость текста Авто Бесплатно В пути 0 мин")
    def text_car_is_free_0_min_in_route_is_visible(self):
        return self.find_element(Locators.start_and_fin_points_are_same_mess)
    
    @allure.step("Жмяк на таб Оптимальный")
    def click_on_optimal_tab(self):
        self.click_element(Locators.optimal_type)

    @allure.step("Цена на табе Оптимальный")
    def price_for_optimal_type(self):
        try:
            element = self.driver.find_element(*Locators.my_car_price)
            text = element.text.strip()
            match = re.search(r'~\s*(\d+)\s*руб\.', text, re.IGNORECASE)
            if match:
                return int(match.group(1))
            else:
                return None
        except NoSuchElementException:
            return None
        
    @allure.step("Время на табе  Оптимальный")
    def time_for_optimal_type(self):
        try:
            element = self.driver.find_element(*Locators.my_car_time)
            text = element.text.strip()
            match = re.search(r'в пути\s*(\d+)\s*мин\.?', text, re.IGNORECASE)
            if match:
                return int(match.group(1))
            else:
                return None
        except NoSuchElementException:
            return None
    
    @allure.step("Цена на табе Быстрый")
    def price_for_fast_type(self):
        try:
            element = self.driver.find_element(*Locators.taxi_price)
            text = element.text.strip()
            match = re.search(r'~\s*(\d+)\s*руб\.', text, re.IGNORECASE)
            if match:
                return int(match.group(1))
            else:
                return None
        except NoSuchElementException:
            return None
        
    @allure.step("Время на табе Быстрый")
    def time_for_fast_type(self):
        try:
            element = self.driver.find_element(*Locators.taxi_time)
            text = element.text.strip()
            match = re.search(r'в пути\s*(\d+)\s*мин\.?', text, re.IGNORECASE)
            if match:
                return int(match.group(1))
            else:
                return None
        except NoSuchElementException:
            return None
    
    @allure.step("Таб Оптимальный активный")
    def optimal_tab_is_active(self):
        try:
            element = self.find_element(Locators.optimal_type_active) 
            is_visible = element.is_displayed()
            if is_visible:
                self.element_visability(Locators.optimal_type_active)
            return is_visible
        except NoSuchElementException:
            return False


    @allure.step("Таб Оптимальный не активный")
    def optimal_tab_is_not_active(self):
        try:
            element = self.find_element(Locators.optimal_type) 
            is_not_visible = element.is_displayed()
            if is_not_visible:
                self.element_visability(Locators.optimal_type)
            return is_not_visible
        except NoSuchElementException:
            return False
        
    @allure.step("Таб Быстрый активный")
    def fast_tab_is_active(self):
        try:
            element = self.find_element(Locators.the_fastest_type_active) 
            is_visible = element.is_displayed()
            if is_visible:
                self.element_visability(Locators.the_fastest_type_active)
            return is_visible
        except NoSuchElementException:
            return False
        

    @allure.step("Таб Быстрый не активный")
    def fast_tab_is_not_active(self):
        try:
            element = self.find_element(Locators.the_fastest_type) 
            is_not_visible = element.is_displayed()
            if is_not_visible:
                self.element_visability(Locators.the_fastest_type)
            return is_not_visible
        except NoSuchElementException:
            return False       
        
    @allure.step("Жмяк на таб Свой")
    def click_on_my_tab(self):
        self.click_element(Locators.my_type)

    @allure.step("Свой таб не активен")
    def my_tab_is_not_active(self):
        try:
            element = self.find_element(Locators.my_type) 
            is_visible = element.is_displayed()
            if is_visible:
                self.element_visability(Locators.my_type)
            return is_visible
        except NoSuchElementException:
            return False

    @allure.step("Свой таб активен")
    def my_tab_is_active(self):
        try:
            element = self.find_element(Locators.my_type_active) 
            is_visible = element.is_displayed()
            if is_visible:
                self.element_visability(Locators.my_type_active)
            return is_visible
        except NoSuchElementException:
            return False
        
    @allure.step("Иконка авто кликабельна")
    def icon_car_is_active(self):
       return self.element_is_clickable(Locators.by_my_car_icon)
    
    @allure.step("Иконка пешком кликабельна")
    def icon_walk_is_active(self):
       return self.element_is_clickable(Locators.walk_icon)
    
    @allure.step("Иконка такси кликабельна")
    def icon_taxi_is_active(self):
       return self.element_is_clickable(Locators.taxi_icon)
    
    @allure.step("Иконка на велосипеде кликабельна")
    def icon_bike_is_active(self):
       return self.element_is_clickable(Locators.bike_icon)
    
    @allure.step("Иконка на самокате кликабельна")
    def icon_scooter_is_active(self):
       return self.element_is_clickable(Locators.scooter_icon)
    
    @allure.step("Иконка драйв кликабельна")
    def icon_drive_is_active(self):
       return self.element_is_clickable(Locators.drive_icon)

    @allure.step("Кнопка Вызвать такси активна")
    def call_taxi_bttn_is_active(self):
        return self.element_is_clickable(Locators.call_taxi_bttn)  
    
    @allure.step("Кнопка забронировать активна")
    def book_bttn_is_active(self):
        return self.element_is_clickable(Locators.book_bttn)
    
    @allure.step("Жмяк на иконку Драйв")
    def click_on_drive(self):
        self.click_element(Locators.drive_icon)

    @allure.step("Жмяк на кнопку Вызвать такси")
    def click_on_call_taxi_bttn(self):
        self.click_element(Locators.call_taxi_bttn)

            

