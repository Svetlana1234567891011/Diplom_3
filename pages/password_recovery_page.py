from pages.base_page import BasePage
import allure
from utils.locators import PasswordRecoveryPageLocators


class PasswordRecoveryPage(BasePage):

    @allure.step('Ждем загрузки заголовка страницы Восстановления пароля')
    def wait_for_recovery_page_header(self):
        self.wait_loading_of_element(PasswordRecoveryPageLocators.HEADER_RESTORE_PASSWORD)

    @allure.step('Вводим имейл')
    def enter_email(self, email):
        self.enter_text_to_element(locator=PasswordRecoveryPageLocators.EMAIL_INPUT_FIELD, keys=email)

    @allure.step('Вводим пароль')
    def enter_password(self, password):
        self.enter_text_to_element(locator=PasswordRecoveryPageLocators.PASSWORD_INPUT_FIELD, keys=password)

    @allure.step('Нажимаем кнопку восстановления пароля')
    def recover_button_click(self):
        self.click_element(PasswordRecoveryPageLocators.BUTTON_RESTORE_PASSWORD)
