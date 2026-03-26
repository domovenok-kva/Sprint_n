import allure
from page_objects.route_page import RoutePage
from data.data_adress import Adresses

class TestBlockChooseRouteType:
   @allure.title("Отрисовка блока с выбором маршрута:")

   @allure.step("При вводе двух разных предустановленных адресов в поля " \
    "Откуда и Куда под выбором адресов отображается блок с выбором маршрута;")
   def test_block_with_route_types_is_visible_when_two_different_adress(self, driver):
    route_pg = RoutePage(driver)
    route_pg.fillin_from_adress_inpt(Adresses.adress_1)
    route_pg.fillin_where_adress_inpt(Adresses.adress_2)
    assert route_pg.block_with_route_types_is_visible()
 
   @allure.step("При вводе одинакового адреса в поля " \
   "Откуда и Куда под выбором адресов отображается блок с выбором маршрута с текстом Авто Бесплатно В пути 0 мин.")
   def test_block_with_route_types_is_visible_when_one_adress(self, driver):
    route_pg = RoutePage(driver)
    route_pg.fillin_from_adress_inpt(Adresses.adress_1)
    route_pg.fillin_where_adress_inpt(Adresses.adress_1)
    assert route_pg.block_with_route_types_is_visible()
    assert route_pg.text_car_is_free_0_min_in_route_is_visible()
