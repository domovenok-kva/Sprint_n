import allure
import pytest
from page_objects.route_page import RoutePage
from page_objects.taxi_page import TaxiPage
from data.data_adress import Adresses
from data.data_info_tariff import DataInfoTariff

class TestTaxiTariff:

    @allure.title("Заказ тарифа Такси. Ввести два разных предустановленных адреса" \
    " в поля Откуда и Куда, выбрать вид маршрута Быстрый, нажать кнопку Вызвать такси")
    @allure.step(" Открывается форма заказа со всеми 6 тарифами по ТЗ, один из них активный")
    def test_order_form_is_open(self, driver):
        route_pg = RoutePage(driver)
        taxi_pg  = TaxiPage(driver)
        route_pg.fillin_from_adress_inpt(Adresses.adress_1)
        route_pg.fillin_where_adress_inpt(Adresses.adress_2)
        route_pg.fast_tab_is_active()
        route_pg.click_on_call_taxi_bttn()
        assert taxi_pg.tariff_picker_is_visible()
        assert taxi_pg.card_is_active()

    @allure.step("При наведении на иконку i в правом верхнем углу каждого тарифа отображается всплывающее окно " \
    "с описанием тарифа, описание тарифа соответствует ТЗ;")
    def test_floating_window_is_visible_after_hover_work(self, driver):
        route_pg = RoutePage(driver)
        taxi_pg  = TaxiPage(driver)
        route_pg.fillin_from_adress_inpt(Adresses.adress_1)
        route_pg.fillin_where_adress_inpt(Adresses.adress_2)
        route_pg.fast_tab_is_active()
        route_pg.click_on_call_taxi_bttn()

        taxi_pg.hover_on_info_icon_work()
        info_get_name_work = taxi_pg.get_info_work_taxi_name()
        info_get_descrip_work = taxi_pg.get_info_work_taxi_descrip()

        assert info_get_name_work == DataInfoTariff.work_tariff_title and info_get_descrip_work == DataInfoTariff.work_tariff_descrip
        

    def test_floating_window_is_visible_after_hover_vacation(self, driver):
        route_pg = RoutePage(driver)
        taxi_pg  = TaxiPage(driver)
        route_pg.fillin_from_adress_inpt(Adresses.adress_1)
        route_pg.fillin_where_adress_inpt(Adresses.adress_2)
        route_pg.fast_tab_is_active()
        route_pg.click_on_call_taxi_bttn()

        taxi_pg.click_vacation_tariff()
        taxi_pg.hover_on_info_icon_vacation()
        info_get_name_vctn = taxi_pg.get_info_vacation_taxi_name()
        info_get_descrip_vctn = taxi_pg.get_info_vacation_taxi_descrip()

        assert info_get_name_vctn == DataInfoTariff.vacation_tariff_title and info_get_descrip_vctn == DataInfoTariff.vacation_tariff_descrip
        
    def test_floating_window_is_visible_after_hover_comforting(self, driver):
        route_pg = RoutePage(driver)
        taxi_pg  = TaxiPage(driver)
        route_pg.fillin_from_adress_inpt(Adresses.adress_1)
        route_pg.fillin_where_adress_inpt(Adresses.adress_2)
        route_pg.fast_tab_is_active()
        route_pg.click_on_call_taxi_bttn()

        taxi_pg.click_comforting_tariff()
        taxi_pg.hover_on_info_icon_comforting()
        info_get_name_cmfrt = taxi_pg.get_info_comforting_taxi_name()
        info_get_descrip_cmfrt = taxi_pg.get_info_comforting_taxi_descrip()
      
        assert info_get_name_cmfrt == DataInfoTariff.comforting_tariff_title and info_get_descrip_cmfrt == DataInfoTariff.comforting_tariff_descrip
        
    def test_floating_window_is_visible_after_hover_glossy(self, driver):
        route_pg = RoutePage(driver)
        taxi_pg  = TaxiPage(driver)
        route_pg.fillin_from_adress_inpt(Adresses.adress_1)
        route_pg.fillin_where_adress_inpt(Adresses.adress_2)
        route_pg.fast_tab_is_active()
        route_pg.click_on_call_taxi_bttn()

        taxi_pg.click_glossy_tariff()
        taxi_pg.hover_on_info_icon_glossy()
        info_get_name_glss= taxi_pg.get_info_glossy_taxi_name()
        info_get_descrip_glss = taxi_pg.get_info_glossy_taxi_descrip()

        assert info_get_name_glss == DataInfoTariff.glossy_tariff_title and info_get_descrip_glss == DataInfoTariff.glossy_tariff_descrip

    @pytest.mark.xfail(reason = "Этот тест должен падать, пока не исправят баг - перепутанное описание с тарифом Разговорчивый")
    def test_floating_window_is_visible_after_hover_sleepy(self, driver):
        route_pg = RoutePage(driver)
        taxi_pg  = TaxiPage(driver)
        route_pg.fillin_from_adress_inpt(Adresses.adress_1)
        route_pg.fillin_where_adress_inpt(Adresses.adress_2)
        route_pg.fast_tab_is_active()
        route_pg.click_on_call_taxi_bttn()

        taxi_pg.click_sleepy_tariff()
        taxi_pg.hover_on_info_icon_sleepy()

        info_get_name_slp = taxi_pg.get_info_sleepy_taxi_name()
        info_get_descrip_slp = taxi_pg.get_info_sleepy_taxi_descrip()

        assert info_get_name_slp == DataInfoTariff.sleepy_tariff_title and info_get_descrip_slp == DataInfoTariff.sleepy_tariff_descrip

    @pytest.mark.xfail(reason = "Этот тест должен падать, пока не исправят баг - перепутанное описание с тарифом Сонный")
    def test_floating_window_is_visible_after_hover_talkative(self, driver):
        route_pg = RoutePage(driver)
        taxi_pg  = TaxiPage(driver)
        route_pg.fillin_from_adress_inpt(Adresses.adress_1)
        route_pg.fillin_where_adress_inpt(Adresses.adress_2)
        route_pg.fast_tab_is_active()
        route_pg.click_on_call_taxi_bttn()

        taxi_pg.click_talkative_tariff()
        taxi_pg.hover_on_info_icon_talkative()

        info_get_name_tlktv = taxi_pg.get_info_talkative_taxi_name()
        info_get_descrip_tlktv = taxi_pg.get_info_talkative_taxi_descrip()

        assert info_get_name_tlktv == DataInfoTariff.talkative_tariff_title and info_get_descrip_tlktv == DataInfoTariff.talkative_tariff_descrip


    @allure.step("Под тарифами отображается блок с полями Телефон, Способ оплаты, Комментарий водителю, " \
    "Требования к заказу Заказ тарифа Такси.")
    def test_block_with_fields_is_visible(self, driver):
        route_pg = RoutePage(driver)
        taxi_pg  = TaxiPage(driver)
        route_pg.fillin_from_adress_inpt(Adresses.adress_1)
        route_pg.fillin_where_adress_inpt(Adresses.adress_2)
        route_pg.fast_tab_is_active()
        route_pg.click_on_call_taxi_bttn()
        assert taxi_pg.phone_number_is_visible()
        assert taxi_pg.payment_method_bttn_is_visible()
        assert taxi_pg.comment_inpt_is_visible()
        assert taxi_pg.requirements_bttn_is_visible()
        assert taxi_pg.make_order_bttn_is_visible()