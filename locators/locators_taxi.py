from selenium.webdriver.common.by import By

class LocatorsTaxi:
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