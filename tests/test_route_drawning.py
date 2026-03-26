import allure
from page_objects.route_page import RoutePage
from data.data_adress import Adresses

class TestRouteDrowning:

    @allure.title("Отрисовка маршрута")
    @allure.step("При вводе двух разных предустановленных адресов в поля " \
    "Откуда и Куда на карте отображаются две точки начала и конца маршрута.")
    def test_fillin_from_and_to_inpts_begin_finish_points_drowing(self, driver):
        route_pg = RoutePage(driver)
        route_pg.fillin_from_adress_inpt(Adresses.adress_1)
        route_pg.fillin_where_adress_inpt(Adresses.adress_2)
        assert route_pg.the_start_point_is_visible()
        assert route_pg.the_end_point_is_visible()