import pytest
from selenium import webdriver
import allure

@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()

# @pytest.fixture(scope='function')
# def driver():
#     driver = webdriver.Chrome(executable_path='./chromedriver')
#     yield driver
#     driver.quit()
