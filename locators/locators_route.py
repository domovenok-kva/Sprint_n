from selenium.webdriver.common.by import By

class LocatorsRoute:

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

    



