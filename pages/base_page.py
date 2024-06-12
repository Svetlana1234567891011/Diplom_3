from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from utils.urls import URLS
import allure


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Открываем страницу')
    def open_page(self, subdir=''):
        url = URLS.MAIN_PAGE_URL+subdir
        self.driver.maximize_window()
        return self.driver.get(url)

    @allure.step('Проверяем url')
    def try_out_url(self, subdir=''):
        combined_url = URLS.MAIN_PAGE_URL + subdir
        return self.driver.current_url == combined_url

    @allure.step('Ждем загрузки элемента')
    def wait_loading_of_element(self, locator):
        return WebDriverWait(self.driver, 25).until(EC.visibility_of_element_located(locator))

    @allure.step('Ищем элемент по локатору')
    def find_element_by_locator(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f'Element not found in {locator}')

    @allure.step('Вводим текст в элемент')
    def enter_text_to_element(self, locator, time=10, keys=None):
        WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                               message=f'Element not found in {locator}')
        self.find_element_by_locator(locator).send_keys(keys)

    @allure.step('Клик по элементу')
    def click_element(self, locator, time=10):
        click_element_located = WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f'Element not found in {locator}')
        self.driver.execute_script("arguments[0].click();", click_element_located)


    @allure.step('Получаем текст элемента')
    def get_text_of_element(self, locator):
        return self.find_element_by_locator(locator).text

    @allure.step('Драг-н-дроп элемента на элемент')
    def drag_n_drop_one_to_other_element(self, source, target):
        drag = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(source))
        drop = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(target))
        ActionChains(self.driver).drag_and_drop(drag, drop).perform()

    @allure.step('Ждем исчезновения элемента из DOMа')
    def wait_for_disappear(self, locator, time=10):
        WebDriverWait(self.driver, 20).until(EC.invisibility_of_element_located(locator))



