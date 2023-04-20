from pages.main_page import MainPage, LocatorsMainPage
from pages.order_page import OrderPage, LocatorOrderPage
import allure

class TestRegistration:

    @allure.title('Проверка регистрации через кнопку в шапке')
    def test_registration_from_header_button(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site()
        main_page.click_on_button_order_header()
        order_page = OrderPage(driver)
        order_page.registration('Дарья', 'Волк', 'На Луну', '+79112221111')
        order_page.find_element(LocatorOrderPage.locator_metro_field).click()
        metro_choice = order_page.find_element(LocatorOrderPage.locator_metro_select_cherkiz)
        metro_choice.click()
        order_page.click_button_next()
        order_page.find_element(LocatorOrderPage.locator_click_period).click()
        period_choice = order_page.find_element(LocatorOrderPage.locator_period_two)
        period_choice.click()
        order_page.find_element(LocatorOrderPage.locator_date_order).click()
        date_choice = order_page.find_element(LocatorOrderPage.locator_calendar_22)
        date_choice.click()
        order_page.find_element(LocatorOrderPage.locator_do_order).click()
        order_page.find_element(LocatorOrderPage.locator_order_agree).click()
        assert 'Заказ оформлен' in order_page.get_order_status()

    @allure.title('Проверка регистрации через кнопку внизу страницы')
    def test_registration_from_middle_button(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site()
        main_page.click_on_button_order_middle()
        order_page = OrderPage(driver)
        order_page.registration('Крокодил', 'Гена', 'В лес', '+79102120000')
        order_page.find_element(LocatorOrderPage.locator_metro_field).click()
        metro_choice = order_page.find_element(LocatorOrderPage.locator_metro_select_bulv)
        metro_choice.click()
        order_page.click_button_next()
        order_page.find_element(LocatorOrderPage.locator_click_period).click()
        period_choice = order_page.find_element(LocatorOrderPage.locator_period_three)
        period_choice.click()
        order_page.find_element(LocatorOrderPage.locator_date_order).click()
        date_choice = order_page.find_element(LocatorOrderPage.locator_calendar_25)
        date_choice.click()
        order_page.find_element(LocatorOrderPage.locator_do_order).click()
        order_page.find_element(LocatorOrderPage.locator_order_agree).click()
        assert 'Заказ оформлен' in order_page.get_order_status()

