
from selenium.webdriver.common.by import By
import allure
from pages.base_page import BasePage

class LocatorOrderPage:
    #check_lettering = [By.CLASS_NAME, "Order_Header__BZXOb"]
    locator_name_field = [By.XPATH, ".//input[@placeholder='* Имя']"]
    locator_surname_field = [By.XPATH, ".//input[@placeholder='* Фамилия']"]
    locator_address_field = [By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']"]
    locator_phone_field = [By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']"]
    locator_button_next = [By.XPATH, ".//button[contains(@class,'Button_Middle')]"]

    locator_metro_field = [By.XPATH, ".//input[@placeholder='* Станция метро']"]
    locator_metro_select_cherkiz = (By.XPATH, ".//div[text()='Черкизовская']")
    locator_metro_select_bulv = (By.XPATH, ".//div[text()='Бульвар Рокоссовского']")

    locator_date_order = (By.XPATH, ".//input[@placeholder='* Когда привезти самокат']")
    locator_calendar_22 = (By.XPATH, ".//div[text()='22']")
    locator_calendar_25 = (By.XPATH, ".//div[text()='25']")

    locator_click_period = (By.XPATH, ".//div[text()='* Срок аренды']")
    locator_period_two = (By.XPATH, ".//div[text()='двое суток']")
    locator_period_three = (By.XPATH, ".//div[text()='трое суток']")
    locator_do_order = (By.XPATH, ".//div[@class='Order_Buttons__1xGrp']/button[text()='Заказать']")
    locator_order_agree = (By.XPATH, ".//div[@class='Order_Buttons__1xGrp']/button[text()='Да']")
    locator_check_status = (By.XPATH, ".//div[contains(@class, 'Order_ModalHeader')]")

    locator_scooter_logo = [By.CLASS_NAME, "Header_LogoScooter__3lsAR"]

class OrderPage(BasePage):

    def set_name(self, name):
        name_field = self.find_element(LocatorOrderPage.locator_name_field)
        name_field.send_keys(name)
        return name_field
    def set_surname(self, surname):
        surname_field = self.find_element(LocatorOrderPage.locator_surname_field)
        surname_field.send_keys(surname)
        return  surname_field

    def set_address(self, address):
        address_field = self.find_element(LocatorOrderPage.locator_address_field)
        address_field.send_keys(address)
        return address_field

    def set_phone(self, phone):
        phone_field = self.find_element(LocatorOrderPage.locator_phone_field)
        phone_field.send_keys(phone)
        return phone_field

    @allure.step('Вводим данные регистрации')
    def registration(self, name, surname, address,  phone):
        self.set_name(name)
        self.set_surname(surname)
        self.set_address(address) 
        self.set_phone(phone) 


    @allure.step('Нажимаем кнопку «Далее»')
    def click_button_next(self):
        button_next = self.find_element(LocatorOrderPage.locator_button_next)
        button_next.click()
        return button_next

    @allure.step('Проверяем статус заказа')
    def get_order_status(self):
        order_status = self.find_element(LocatorOrderPage.locator_check_status).text
        return order_status


    @allure.step('Нажимаем на логотип «Самокат»')
    def click_on_scooter_logo(self):
        scooter_logo = self.find_element(LocatorOrderPage.locator_scooter_logo)
        scooter_logo.click()
        return scooter_logo
