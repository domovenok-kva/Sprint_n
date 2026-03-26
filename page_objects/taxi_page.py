import allure
from locators.locators_taxi import LocatorsTaxi
from page_objects.base_page import BasePage
from data.pattern import Pattern

class TaxiPage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)

    def wait_element(self):
        return self.element_visability(LocatorsTaxi.fin_order_wndw_title)

    @allure.step("Отобразились карточки тарифов")
    def tariff_picker_is_visible(self):
        return self.find_element(LocatorsTaxi.tariff_picker)
    
    @allure.step("Одна карточка активна")
    def card_is_active(self):
        return self.element_is_clickable(LocatorsTaxi.work_taxi)
    
    @allure.step("Ховер на i тарифа Рабочий")
    def hover_on_info_icon_work(self):
        self.hover_on_elem(LocatorsTaxi.tcard_i_work)
        
    @allure.step("Ховер на i тарифа сонный")
    def hover_on_info_icon_sleepy(self):
        self.hover_on_elem(LocatorsTaxi.tcard_i_sleepy)
        
    @allure.step("Ховер на i тарифа Отпускной")
    def hover_on_info_icon_vacation(self):
        self.hover_on_elem(LocatorsTaxi.tcard_i_vacation)
       
    @allure.step("Ховер на i тарифа Разговорчивый")
    def hover_on_info_icon_talkative(self):
        self.hover_on_elem(LocatorsTaxi.tcard_i_talkative)
       
    @allure.step("Ховер на i тарифа Утешительный")
    def hover_on_info_icon_comforting(self):
        self.hover_on_elem(LocatorsTaxi.tcard_i_comforting)
        
    @allure.step("Ховер на i тарифа Глянцевый")
    def hover_on_info_icon_glossy(self):
        self.hover_on_elem(LocatorsTaxi.tcard_i_glossy)
        
    @allure.step("получить заголовок карточки тарифа Рабочий")
    def get_info_work_taxi_name(self):
        return self.get_element_value(LocatorsTaxi.work_taxi_info_name)
    
    @allure.step("получить информацию  о тарифе Рабочий")
    def get_info_work_taxi_descrip(self):
        return self.get_element_value(LocatorsTaxi.work_taxi_info_discrip)
    
    @allure.step("получить заголовок карточки тарифа Сонный")
    def get_info_sleepy_taxi_name(self):
        return self.get_element_value(LocatorsTaxi.sleepy_taxi_info_name)
    
    @allure.step("получить информацию  о тарифе Сонный")
    def get_info_sleepy_taxi_descrip(self):
        return self.get_element_value(LocatorsTaxi.sleepy_taxi_info_discrip)
    
    @allure.step("получить заголовок карточки тарифа Отпускной")
    def get_info_vacation_taxi_name(self):
        return self.get_element_value(LocatorsTaxi.vacation_taxi_info_name)
    
    @allure.step("получить информацию  о тарифе Отпускной")
    def get_info_vacation_taxi_descrip(self):
        return self.get_element_value(LocatorsTaxi.vacation_taxi_info_discrip)
    
    @allure.step("получить заголовок карточки тарифа Разговорчивый")
    def get_info_talkative_taxi_name(self):
        return self.get_element_value(LocatorsTaxi.talkative_taxi_info_name)
    
    @allure.step("получить информацию  о тарифе Разговорчивый")
    def get_info_talkative_taxi_descrip(self):
        return self.get_element_value(LocatorsTaxi.talkative_taxi_info_discrip)
    
    @allure.step("получить заголовок карточки тарифа Утешительный")
    def get_info_comforting_taxi_name(self):
        return self.get_element_value(LocatorsTaxi.comforting_taxi_info_name)
    
    @allure.step("получить информацию  о тарифе Утешительный")
    def get_info_comforting_taxi_descrip(self):
        return self.get_element_value(LocatorsTaxi.comforting_taxi_info_discrip)
    
    @allure.step("получить заголовок карточки тарифа Глянцевый")
    def get_info_glossy_taxi_name(self):
        return self.get_element_value(LocatorsTaxi.glossy_taxi_info_name)
    
    @allure.step("получить информацию  о тарифе Глянцевый")
    def get_info_glossy_taxi_descrip(self):
        return self.get_element_value(LocatorsTaxi.glossy_taxi_info_discrip)
    
    @allure.step("Клик на иконку тарифа сонный")
    def click_sleepy_tariff(self):
        self.click_element(LocatorsTaxi.sleepy_taxi)

    @allure.step("Клик на иконку тарифа Отпускной")
    def click_vacation_tariff(self):
        self.click_element(LocatorsTaxi.vacation_taxi)

    @allure.step("Клик на иконку тарифа Утешительный")
    def click_comforting_tariff(self):
        self.click_element(LocatorsTaxi.comforting_taxi)

    @allure.step("Клик на иконку тарифа Разговорчивый")
    def click_talkative_tariff(self):
        self.click_element(LocatorsTaxi.talkative_taxi)

    @allure.step("Клик на иконку тарифа Глянцевый")
    def click_glossy_tariff(self):
        self.click_element(LocatorsTaxi.glossy_taxi)

    @allure.step("Поиск поля Телефон")
    def phone_number_is_visible(self):
        return self.find_element(LocatorsTaxi.phone_number_bttn)
    
    @allure.step("Поиск поля Способ оплаты")
    def payment_method_bttn_is_visible(self):
        return self.find_element(LocatorsTaxi.payment_method_bttn)
    
    @allure.step("Поиск поля Комментарий")
    def comment_inpt_is_visible(self):
        return self.find_element(LocatorsTaxi.comment_inpt)
    
    @allure.step("Поиск поля Требования к заказу")
    def requirements_bttn_is_visible(self):
        return self.find_element(LocatorsTaxi.requirements_bttn)

    @allure.step("Поиск кнопки оформления заказа")
    def make_order_bttn_is_visible(self):
        return self.find_element(LocatorsTaxi.make_order_bttn)  
    
    @allure.step("Жмяк на кнопку твребования к заказу")
    def click_on_requirements_bttn(self):
        self.click_element(LocatorsTaxi.requirements_bttn)
    
    @allure.step("Жмяк на кнопку столик для ноутбука")
    def click_on_switcher_bttn(self):
        self.click_element(LocatorsTaxi.switcher_bttn)
    
    @allure.step("Жмяк на кнопку оформления заказа")
    def click_on_order_bttn(self):
        self.click_element(LocatorsTaxi.make_order_bttn)

    @allure.step("Поиск кнопки отмены заказа на окне Поиск машины")
    def make_cancel_bttn_is_visible(self):
        return self.find_element(LocatorsTaxi.cancel_bttn) 
    
    @allure.step("Поиск кнопки детали заказа на окне Поиск машины")
    def details_bttn_is_visible(self):
        return self.find_element(LocatorsTaxi.details_burger) 
    
    @allure.step("получить заголовок окна Поиск машины")
    def get_order_window_title(self):
        return self.get_element_value(LocatorsTaxi.order_wndw_title) 
    
    @allure.step("Поиск таймера")
    def taimer_is_visible(self):
        return self.find_element(LocatorsTaxi.timer_in_window) 
    
    @allure.step("Получить заголовок окна ожидания")
    def check_title_in_fin_order_wndw(self):
        return self.find_element(LocatorsTaxi.fin_order_wndw_title)    
        
    @allure.step("Новмер машины виден")
    def car_nuber_is_visible(self):
        return self.find_element(LocatorsTaxi.car_number)
    
    @allure.step("Картинка тарифа видна")
    def tariff_img_is_visible(self):
        return self.find_element(LocatorsTaxi.tariff_img)
    
    @allure.step("Водитель виден")
    def find_driver_info(self):
        return self.find_element(LocatorsTaxi.driver_name)
    
    @allure.step("Рейтинг водителя виден")
    def driver_rating_visible(self):
        return self.find_element(LocatorsTaxi.driver_raiting)
    
    @allure.step("Кнопка отмены видна")
    def fin_cancel_is_visible(self):
        return self.find_element(LocatorsTaxi.fin_cancel_bttn)

    @allure.step("Кнопка бургер видна")
    def fin_descrip_is_visible(self):
        return self.find_element(LocatorsTaxi.fin_details_burger)
    
    @allure.step("Нажать на бургер")
    def click_on_fin_details_burger(self):
        self.click_element(LocatorsTaxi.fin_details_burger)

    @allure.step("Нажать на отмену")
    def click_on_fin_cancel_bttn(self):
        self.click_element(LocatorsTaxi.fin_cancel_bttn)

    @allure.step("получить стоимость поездки")
    def get_fin_price(self):
        return self.get_the_price(LocatorsTaxi.final_sum, Pattern.price_pattern_for_taxi_pg)
    
    @allure.step("Цена на табе Быстрый")
    def price_for_work_tariff(self):
        return self.get_the_price(LocatorsTaxi.work_taxi_sum, Pattern.price_pattern_for_taxi_pg)