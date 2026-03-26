import allure
import pytest
import time
from page_objects.route_page import RoutePage
from page_objects.taxi_page import TaxiPage
from data.data_adress import Adresses
from data.data_order_window import DataOrderWindow


class TestScenary:
    @allure.title("Сценарий. Ввести два разных предустановленных адреса в поля Откуда и Куда," \
    " выбрать вид маршрута Быстрый, нажать кнопку Вызвать такси")
    @allure.step("Выбираем тариф Рабочий, включаем чекбокс Столик для ноутбука, нажимаем кнопку Ввести номер и заказать"
    " - Появляется окно ожидания машины (проверить элементы по ТЗ);")
    def test_work_tariff_checkbox_laptop_table_active_make_order(self, driver):
        route_pg = RoutePage(driver)
        taxi_pg  = TaxiPage(driver)
        route_pg.fillin_from_adress_inpt(Adresses.adress_1)
        route_pg.fillin_where_adress_inpt(Adresses.adress_2)
        route_pg.fast_tab_is_active()
        route_pg.click_on_call_taxi_bttn()
        taxi_pg.click_on_requirements_bttn()
        taxi_pg.click_on_switcher_bttn()
        taxi_pg.click_on_order_bttn()
        window_title = taxi_pg.get_order_window_title()
        assert taxi_pg.make_cancel_bttn_is_visible()
        assert taxi_pg.details_bttn_is_visible()
        assert taxi_pg.taimer_is_visible()
        assert window_title == DataOrderWindow.title_window

    @allure.step("Дождаться окончания таймера поиска машины -" \
    " Отображается окно совершенного заказа (проверить элементы по ТЗ);")
    def test_window_of_finished_order_is_visible(self, driver):
        route_pg = RoutePage(driver)
        taxi_pg  = TaxiPage(driver)
        route_pg.fillin_from_adress_inpt(Adresses.adress_1)
        route_pg.fillin_where_adress_inpt(Adresses.adress_2)
        route_pg.fast_tab_is_active()
        route_pg.click_on_call_taxi_bttn()
        taxi_pg.click_on_requirements_bttn()
        taxi_pg.click_on_switcher_bttn()
        taxi_pg.click_on_order_bttn()
        taxi_pg.wait_element()
        assert taxi_pg.check_title_in_fin_order_wndw()
        assert taxi_pg.car_nuber_is_visible()
        assert taxi_pg.tariff_img_is_visible()
        assert taxi_pg.find_driver_info()
        assert taxi_pg.driver_rating_visible()
        assert taxi_pg.fin_cancel_is_visible()
        assert taxi_pg.fin_descrip_is_visible()

    @allure.step("Нажать кнопку Детали в блоке Еще про поездку - Указана стоимость, которая была при выборе тарифа;")
    def test_click_on_details_bttn_in_finwindow(self, driver):
        route_pg = RoutePage(driver)
        taxi_pg  = TaxiPage(driver)
        route_pg.fillin_from_adress_inpt(Adresses.adress_1)
        route_pg.fillin_where_adress_inpt(Adresses.adress_2)
        route_pg.fast_tab_is_active()
        route_pg.click_on_call_taxi_bttn()
        price = taxi_pg.price_for_work_tariff()
        taxi_pg.click_on_requirements_bttn()
        taxi_pg.click_on_switcher_bttn()
        taxi_pg.click_on_order_bttn()
        taxi_pg.wait_element()
        taxi_pg.click_on_fin_details_burger()
        fin_price = taxi_pg.get_fin_price()
        assert fin_price == price

    @pytest.mark.xfail(reason = "Этот тест должен падать, пока не исправят баг - Не работает кнопка отмены")
    @allure.step("Нажать кнопку Отмена - Окно закрывается.")
    def test_window_closed_after_click_on_cancel_bttn(self, driver):
        route_pg = RoutePage(driver)
        taxi_pg  = TaxiPage(driver)
        route_pg.fillin_from_adress_inpt(Adresses.adress_1)
        route_pg.fillin_where_adress_inpt(Adresses.adress_2)
        route_pg.fast_tab_is_active()
        route_pg.click_on_call_taxi_bttn()
        taxi_pg.click_on_requirements_bttn()
        taxi_pg.click_on_switcher_bttn()
        taxi_pg.click_on_order_bttn()
        taxi_pg.wait_element()
        taxi_pg.click_on_fin_cancel_bttn()
        assert route_pg.the_start_point_is_visible()






