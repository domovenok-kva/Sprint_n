import allure
from page_objects.route_page import RoutePage
from data.data_adress import Adresses

class TestPreparingForTaxiOrder:

    @allure.title("Подготовка к заказу такси. Ввести два разных предустановленных адреса в поля Откуда и Куда")
    @allure.step("При переключении между видами маршрута (Оптимальный\Быстрый) " \
    "происходит смена активного таба и пересчет времени и стоимости маршрута;")
    def test_switching_route_types_optimal_fast(self, driver):
        route_pg = RoutePage(driver)
        route_pg.fillin_from_adress_inpt(Adresses.adress_1)
        route_pg.fillin_where_adress_inpt(Adresses.adress_2)

        route_pg.fast_tab_is_active()
        route_pg.optimal_tab_is_not_active()
        fast_price = route_pg.price_for_fast_type()
        fast_time = route_pg.time_for_fast_type()
        route_pg.click_on_optimal_tab()

        optimal_price = route_pg.price_for_optimal_type()
        optimal_time = route_pg.time_for_optimal_type()

        assert route_pg.optimal_tab_is_active() and route_pg.fast_tab_is_not_active()
        assert optimal_price != fast_price
        assert optimal_time != fast_time
        
    @allure.step("При переключении на вид маршрута Свой происходит смена активного таба " \
    "и становятся активны типы передвижения (Машина, Пешком, Такси, Велосипед, Самокат, Драйв);")
    def test_switching_to_my_type_change_active_type_and_make_types_of_moving_active(self, driver):
        route_pg = RoutePage(driver)
        route_pg.fillin_from_adress_inpt(Adresses.adress_1)
        route_pg.fillin_where_adress_inpt(Adresses.adress_2)

        route_pg.fast_tab_is_active()
        route_pg.my_tab_is_not_active()

        route_pg.click_on_my_tab()
        assert route_pg.my_tab_is_active and route_pg.fast_tab_is_not_active()
        assert route_pg.icon_car_is_active() 
        assert route_pg.icon_walk_is_active()
        assert route_pg.icon_taxi_is_active()
        assert route_pg.icon_bike_is_active()
        assert route_pg.icon_scooter_is_active()
        assert route_pg.icon_drive_is_active()

    @allure.step("При выборе вида маршрута Быстрый активна кнопка Вызвать такси;")
    def test_bttn_call_taxi_is_active_when_fast_tab_chosen(self, driver):
        route_pg = RoutePage(driver)
        route_pg.fillin_from_adress_inpt(Adresses.adress_1)
        route_pg.fillin_where_adress_inpt(Adresses.adress_2)
        route_pg.fast_tab_is_active()
        assert route_pg.call_taxi_bttn_is_active()

    @allure.step("При выборе вида маршрута Свой, типа передвижения Драйв активна кнопка Забронировать.")
    def test_book_bttn_is_active_when_my_tab_chosen(self, driver):
        route_pg = RoutePage(driver)
        route_pg.fillin_from_adress_inpt(Adresses.adress_1)
        route_pg.fillin_where_adress_inpt(Adresses.adress_2)
        route_pg.click_on_my_tab()
        route_pg.click_on_drive()
        assert route_pg.book_bttn_is_active()


 