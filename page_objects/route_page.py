import allure
from locators.locators_route import LocatorsRoute
from page_objects.base_page import BasePage
from data.pattern import Pattern

class RoutePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Заполнить поле Откуда")
    def fillin_from_adress_inpt(self, from_adress):
        self.fill_inpt(LocatorsRoute.from_inpt, from_adress)

    @allure.step("Заполнить поле Куда")
    def fillin_where_adress_inpt(self, where_adress):
        self.fill_inpt(LocatorsRoute.to_inpt, where_adress)

    @allure.step("Видимость начальной точки маршрута")
    def the_start_point_is_visible(self):
        return self.element_is_acive(LocatorsRoute.pin_a) 
    
    @allure.step("Видимость конечной точки маршрута")
    def the_end_point_is_visible(self):
        return self.element_is_acive(LocatorsRoute.pin_b) 
        
    @allure.step("Видимость блока с выбором маршрута")
    def block_with_route_types_is_visible(self):
        return self.find_element(LocatorsRoute.picker_of_types)
    
    @allure.step("Видимость текста Авто Бесплатно В пути 0 мин")
    def text_car_is_free_0_min_in_route_is_visible(self):
        return self.find_element(LocatorsRoute.start_and_fin_points_are_same_mess)
    
    @allure.step("Жмяк на таб Оптимальный")
    def click_on_optimal_tab(self):
        self.click_element(LocatorsRoute.optimal_type)

    @allure.step("Цена на табе Оптимальный")
    def price_for_optimal_type(self):
        return self.get_the_price(LocatorsRoute.my_car_price, Pattern.price_pattern_for_route_pg)
        
    @allure.step("Время на табе  Оптимальный")
    def time_for_optimal_type(self):
        return self.get_the_price(LocatorsRoute.my_car_time, Pattern.time_pattern_for_route_pg)
    
    @allure.step("Цена на табе Быстрый")
    def price_for_fast_type(self):
        return self.get_the_price(LocatorsRoute.taxi_price, Pattern.price_pattern_for_route_pg)
        
    @allure.step("Время на табе Быстрый")
    def time_for_fast_type(self):
        return self.get_the_price(LocatorsRoute.taxi_time, Pattern.time_pattern_for_route_pg)
    
    @allure.step("Таб Оптимальный активный")
    def optimal_tab_is_active(self):
        return self.element_is_acive(LocatorsRoute.optimal_type_active) 

    @allure.step("Таб Оптимальный не активный")
    def optimal_tab_is_not_active(self):
       return self.element_is_acive(LocatorsRoute.optimal_type) 
        
    @allure.step("Таб Быстрый активный")
    def fast_tab_is_active(self):
        return self.element_is_acive(LocatorsRoute.the_fastest_type_active)         

    @allure.step("Таб Быстрый не активный")
    def fast_tab_is_not_active(self):
        return self.element_is_acive(LocatorsRoute.the_fastest_type) 
        
    @allure.step("Жмяк на таб Свой")
    def click_on_my_tab(self):
        return self.click_element(LocatorsRoute.my_type)

    @allure.step("Свой таб не активен")
    def my_tab_is_not_active(self):
        return self.element_is_acive(LocatorsRoute.my_type)

    @allure.step("Свой таб активен")
    def my_tab_is_active(self):
        return self.element_is_acive(LocatorsRoute.my_type_active)
        
    @allure.step("Иконка авто кликабельна")
    def icon_car_is_active(self):
       return self.element_is_clickable(LocatorsRoute.by_my_car_icon)
    
    @allure.step("Иконка пешком кликабельна")
    def icon_walk_is_active(self):
       return self.element_is_clickable(LocatorsRoute.walk_icon)
    
    @allure.step("Иконка такси кликабельна")
    def icon_taxi_is_active(self):
       return self.element_is_clickable(LocatorsRoute.taxi_icon)
    
    @allure.step("Иконка на велосипеде кликабельна")
    def icon_bike_is_active(self):
       return self.element_is_clickable(LocatorsRoute.bike_icon)
    
    @allure.step("Иконка на самокате кликабельна")
    def icon_scooter_is_active(self):
       return self.element_is_clickable(LocatorsRoute.scooter_icon)
    
    @allure.step("Иконка драйв кликабельна")
    def icon_drive_is_active(self):
       return self.element_is_clickable(LocatorsRoute.drive_icon)

    @allure.step("Кнопка Вызвать такси активна")
    def call_taxi_bttn_is_active(self):
        return self.element_is_clickable(LocatorsRoute.call_taxi_bttn)  
    
    @allure.step("Кнопка забронировать активна")
    def book_bttn_is_active(self):
        return self.element_is_clickable(LocatorsRoute.book_bttn)
    
    @allure.step("Жмяк на иконку Драйв")
    def click_on_drive(self):
        self.click_element(LocatorsRoute.drive_icon)

    @allure.step("Жмяк на кнопку Вызвать такси")
    def click_on_call_taxi_bttn(self):
        self.click_element(LocatorsRoute.call_taxi_bttn)

            

