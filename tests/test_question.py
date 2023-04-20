from pages.main_page import MainPage
import allure

class TestQuestion:

    @allure.title('Проверка вопроса о цене')
    def test_question_price(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site()
        main_page.click_on_question_price()
        assert main_page.get_answer_question_price() == 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'

    @allure.title('Проверка вопроса о нескольких самокатах')
    def test_question_few_scooter(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site()
        main_page.click_on_question_few_scooter()
        check_phrase = 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'
        assert main_page.get_answer_question_few_scooter() == check_phrase

    @allure.title('Проверка вопроса о сроках аренды')
    def test_question_rental_period(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site()
        main_page.click_on_question_rental_period()
        check_phrase = 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'
        assert main_page.get_answer_question_rental_period() == check_phrase

    @allure.title('Проверка вопроса о заказе на сегодня')
    def test_question_today_order(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site()
        main_page.click_on_question_today_order()
        check_phrase = 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'
        assert main_page.get_answer_question_today_order() == check_phrase

    @allure.title('Проверка вопроса о изменении срока')
    def test_question_change_period(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site()
        main_page.click_on_question_change_period()
        check_phrase = 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'
        assert main_page.get_answer_question_change_period() == check_phrase

    @allure.title('Проверка вопроса о зарядке')
    def test_question_charge(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site()
        main_page.click_on_question_charge()
        check_phrase = 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'
        assert main_page.get_answer_question_charge() == check_phrase

    @allure.title('Проверка вопроса об отмене')
    def test_question_cancel(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site()
        main_page.click_on_question_cancel()
        check_phrase = 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'
        assert main_page.get_answer_question_cancel() == check_phrase

    @allure.title('Проверка вопроса о заказке за МКАД')
    def test_question_county(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site()
        main_page.click_on_question_county()
        check_phrase = 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'
        assert main_page.get_answer_question_county() == check_phrase