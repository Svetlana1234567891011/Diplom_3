from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from utils.locators import MainPageLocators
import allure


class MainPage(BasePage):

    @allure.step('Ждем загрузки заголовка главной страницы проекта')
    def wait_for_main_page_header(self):
        self.wait_loading_of_element(MainPageLocators.MAIN_PAGE_HEADER)

    @allure.step('Кликаем по кнопке Личный кабинет')
    def click_private_area_button(self):
        self.click_element(MainPageLocators.PRIVATE_AREA)

    @allure.step('Проверяем наличие кнопки Войти в аккаунт, видимой только для незалогиненного пользователя')
    def try_out_enter_button(self):
        return self.find_element_by_locator(MainPageLocators.BUTTON_ENTER_ACCOUNT)

    @allure.step('Проверяем наличие кнопки Оформить заказ, видимой только для незалогиненного пользователя')
    def try_out_order_button(self):
        return self.find_element_by_locator(MainPageLocators.ORDER_BUTTON)

    @allure.step('Кликаем Лента Заказов')
    def click_feed_of_orders(self):
        self.click_element(MainPageLocators.ORDER_LINE)

    @allure.step('Кликаем первый ингредиент на главной странице')
    def click_first_ingredient(self):
        self.click_element(MainPageLocators.FIRST_INGREDIENT)

    @allure.step('Проверяем видимость модального окна')
    def try_out_opening_of_modal(self):
        try:
            self.driver.find_element(By.XPATH, MainPageLocators.INGREDIENT_MODAL_XPATH)
        except NoSuchElementException:
            return False
        return True

    @allure.step('Ждем загрузки заголовка модального окна')
    def wait_for_modal_header(self):
        self.wait_loading_of_element(MainPageLocators.INGREDIENT_MODAL_HEADER)

    @allure.step('Нажимаем на крестик, закрывающий модальное окно')
    def click_cross_of_modal(self):
        #self.wait_for_element_loaded(MainPageLocators.CLOSE_MODAL).click()
        close_modal_button=self.wait_loading_of_element(MainPageLocators.CLOSE_MODAL)
        self.driver.execute_script("arguments[0].click();", close_modal_button)

    @allure.step('Получаем значение счетчика ингредиента')
    def get_value_of_ingredient_counter(self):
        return self.driver.find_element(By.XPATH, MainPageLocators.FIRST_INGREDIENT_COUNTER_XPATH).text

    @allure.step('Перетаскиваем первый ингредиент в корзину')
    def drag_n_drop_first_ingredient_to_basket(self):
        self.drag_n_drop_one_to_other_element(source=MainPageLocators.FIRST_INGREDIENT, target=MainPageLocators.BASKET)

    @allure.step('Кликаем Оформить заказ')
    def click_button_of_making_order(self):
        self.click_element(MainPageLocators.ORDER_BUTTON)

    @allure.step('Получаем значение ID заказа при его оформлении')
    def get_order_id(self):
        self.wait_for_disappear(MainPageLocators.TEMPORARY_ORDER_MODAL_HEADER)
        return self.driver.find_element(By.XPATH, MainPageLocators.ORDER_ID_XPATH).text

    @allure.step('Создаем заказ')
    def make_order(self):
        self.drag_n_drop_first_ingredient_to_basket()
        self.click_button_of_making_order()










