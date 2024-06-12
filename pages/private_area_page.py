import allure
from pages.base_page import BasePage
from utils.locators import PrivateArea_Locators, LoginPageLocators


class ProfilePage(BasePage):

    @allure.step('Нажимаем заголовок секции Истории заказов')
    def click_orders_history_section_name(self):
        return self.click_element(PrivateArea_Locators.ORDERS_HISTORY_AREA)

    @allure.step('Ждем загрузки заголовка секции Профиль')
    def wait_for_private_area_header(self):
        return self.wait_loading_of_element(PrivateArea_Locators.PROFILE_AREA)

    @allure.step('Нажимаем Выход')
    def click_exit(self):
        return self.click_element(PrivateArea_Locators.BUTTON_EXIT_ACCOUNT)

    @allure.step('Ждем загрузки кнопки сабмит')
    def wait_for_private_area_submit_button(self):
        return self.wait_loading_of_element(LoginPageLocators.BUTTON_LOGIN)


