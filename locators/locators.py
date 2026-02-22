from selenium.webdriver.common.by import By

class Locators:

    #поля Куда и Откуда
    from_inpt = (By.XPATH, "//input[@id = 'from']")
    to_inpt = (By.XPATH, "//input[@id = 'to']")

    #Блок с вводом адресов: Откуда, Куда
    dst_picker = (By.XPATH, "//div[@class='dst-picker']")

    #карта
    map_wind = (By.XPATH, "//div[@class = 'map']")

    #пины построенного маршрута
    pin_a = (By.XPATH, "//ymaps[contains(@class, 'ymaps-2-1-79-placemark-overlay')]")
    pin_b = (By.XPATH, "//ymaps[contains(@class, 'ymaps-2-1-79-placemark-overlay')]")

    #Блок с выбором вида маршрута
    picker_of_types  = (By.XPATH, "//div[contains(@class, 'type-picker shown')]")

    optimal_type = (By.XPATH, "//div[contains(@class, 'mode') and contains(text(), 'Оптимальный')]")
    optimal_type_active = (By.XPATH, "//div[contains(@class, 'mode active') and contains(text(), 'Оптимальный')]")

    the_fastest_type = (By.XPATH, "//div[contains(@class, 'mode') and contains(text(), 'Быстрый')]")
    the_fastest_type_active = (By.XPATH, "//div[contains(@class, 'mode active') and contains(text(), 'Быстрый')]")

    my_type = (By.XPATH, "//div[contains(@class, 'mode') and text()='Свой']")
    my_type_active = (By.XPATH, "//div[contains(@class, 'mode active') and text()='Свой']")
 
    #иконки типов передвижения
    by_my_car_icon = (By.XPATH, '//img[contains(@src, "/static/media/car.8a2b1ff5.svg")]')
    walk_icon = (By.XPATH, '//img[contains(@src, "/static/media/walk.d33bf83c.svg")]')
    taxi_icon = (By.XPATH, '//img[contains(@src, "/static/media/taxi-active.b0be3054.svg")]')
    bike_icon = (By.XPATH, '//img[contains(@src, "/static/media/bike.fb41c762.svg")]')
    scooter_icon = (By.XPATH, '//img[contains(@src, "/static/media/scooter.cf9bb57e.svg")]')
    drive_icon = (By.XPATH, '//img[contains(@src, "/static/media/drive.fa5137d7.svg")]')
    
    #кнопка забронировать
    book_bttn  = (By.XPATH, "//button[contains(@class, 'button round') and text()='Забронировать']")

    #кнопка Вызвать такси
    call_taxi_bttn = (By.XPATH, "//button[contains(@class, 'button round') and text()='Вызвать такси']")

    #Блок информации: Стоимость, Время в пути
    taxi_price = (By.XPATH,  "//div[contains(@class, 'text') and contains(., 'Такси') and contains(., 'руб.')]")
    taxi_time = (By.XPATH, "//div[contains(@class, 'duration') and contains(., 'В пути')]")
    my_car_price =  (By.XPATH, "//div[contains(@class, 'text') and contains(., 'Авто') and contains(., 'руб.')]")
    my_car_time = (By.XPATH, "//div[contains(@class, 'duration') and contains(., 'В пути')]")
    start_and_fin_points_are_same_mess = (By.XPATH, "//div[contains(@class, 'results-text')]//div[contains(text(), 'Авто Бесплатно')]/following-sibling::div[contains(text(), 'В пути 0 мин')]")

    #Тарифы такси
    tariff_picker = (By.XPATH, "//div[contains(@class, 'tariff-picker shown')]")
    tcard_i_work = (By.XPATH, "//button[@data-for='tariff-card-0']")
    tcard_i_sleepy = (By.XPATH, "//button[@data-for='tariff-card-1']")
    tcard_i_vacation = (By.XPATH, "//button[@data-for='tariff-card-2']")
    tcard_i_talkative = (By.XPATH, "//button[@data-for='tariff-card-3']")
    tcard_i_comforting = (By.XPATH, "//button[@data-for='tariff-card-4']")
    tcard_i_glossy = (By.XPATH, "//button[@data-for='tariff-card-5']")

    work_taxi = (By.XPATH, "//div[contains(@class, 'tcard active')]//div[contains(text(), 'Рабочий')]")
    work_taxi_info_name = (By.XPATH, "//div[@id='tariff-card-0']//div[@class='i-title']")
    work_taxi_info_discrip = (By.XPATH, "//div[@id='tariff-card-0']//div[@class='i-dPrefix']")

    sleepy_taxi = (By.XPATH, "//div[contains(@class, 'tcard')]//div[contains(text(), 'Сонный')]")
    sleepy_taxi_info_name = (By.XPATH, "//div[@id='tariff-card-1']//div[@class='i-title']")
    sleepy_taxi_info_discrip = (By.XPATH, "//div[@id='tariff-card-1']//div[@class='i-dPrefix']")

    vacation_taxi = (By.XPATH, "//div[contains(@class, 'tcard')]//div[contains(text(), 'Отпускной')]")
    vacation_taxi_info_name = (By.XPATH, "//div[@id='tariff-card-2']//div[@class='i-title']")
    vacation_taxi_info_discrip = (By.XPATH, "//div[@id='tariff-card-2']//div[@class='i-dPrefix']")

    talkative_taxi = (By.XPATH, "//div[contains(@class, 'tcard')]//div[contains(text(), 'Разговорчивый')]")
    talkative_taxi_info_name = (By.XPATH, "//div[@id='tariff-card-3']//div[@class='i-title']")
    talkative_taxi_info_discrip = (By.XPATH, "//div[@id='tariff-card-3']//div[@class='i-dPrefix']")

    comforting_taxi = (By.XPATH, "//div[contains(@class, 'tcard')]//div[contains(text(), 'Утешительный')]")
    comforting_taxi_info_name = (By.XPATH, "//div[@id='tariff-card-4']//div[@class='i-title']")
    comforting_taxi_info_discrip = (By.XPATH, "//div[@id='tariff-card-4']//div[@class='i-dPrefix']")

    glossy_taxi = (By.XPATH, "//div[contains(@class, 'tcard')]//div[contains(text(), 'Глянцевый')]")
    glossy_taxi_info_name = (By.XPATH, "//div[@id='tariff-card-5']//div[@class='i-title']")
    glossy_taxi_info_discrip = (By.XPATH, "//div[@id='tariff-card-5']//div[@class='i-dPrefix']")
    
    #Поля в блоке заказа такси
    phone_number_bttn = (By.XPATH, "//div[contains(@class, 'np-button')]//div[contains(text(), 'Телефон')]")
    comment_inpt = (By.XPATH, "//div[contains(@class, 'input-container')]//label[contains(text(), 'Комментарий водителю...')]")
    payment_method_bttn = (By.XPATH, "//div[contains(@class, 'pp-button filled')]//div[contains(text(), 'Способ оплаты')]")
    requirements_bttn = (By.XPATH, "//div[contains(@class, 'reqs-header')]//div[contains(text(), 'Требования к заказу')]")
    make_order_bttn = (By.XPATH, "//div[contains(@class, 'smart-button')]")
    switcher_bttn = (By.XPATH, "//span[contains(@class, 'slider round')]")

    #Окно оформленного заказа
    timer_in_window = (By.XPATH, "//div[contains(@class, 'order-header-time')]")
    cancel_bttn = (By.XPATH, "//button[contains(@class, 'order-button')]//img[@alt='close']")
    details_burger = (By.XPATH, "//button[contains(@class, 'order-button')]//img[@alt='burger']")
    order_wndw_title  =(By.XPATH, "//div[contains(@class, 'order-header-title')]")

    #Окно завершённого заказа
    fin_order_wndw_title = (By.XPATH, "//img[@src='/static/media/chewron.f3fff088.svg']")
    car_number = (By.XPATH, "//div[contains(@class, 'order-number')]//div[contains(@class, 'number')]")
    tariff_img = (By.XPATH, "//img[@alt='Car']")
    driver_name = (By.XPATH, "//div[contains(@class, 'order-btn-group')]")
    driver_raiting = (By.XPATH, "//div[contains(@class, 'order-btn-rating')]")
    fin_cancel_bttn = (By.XPATH, "//button[contains(@class, 'order-button')]//img[@alt='close']")
    fin_details_burger  = (By.XPATH, "//button[contains(@class, 'order-button')]//img[@alt='burger']")
    final_sum = (By.XPATH, "//div[contains(@class, 'o-d-sh')]")

    work_taxi_sum = (By.XPATH, "//div[contains(@class, 'tcard active')]//div[contains(text(), 'Рабочий')]//div[contains(@class, 'tcard-price')]")



