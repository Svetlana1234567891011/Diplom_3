from pages.password_recovery_page import PasswordRecoveryPage
from utils.locators import ResetPasswordPageLocators, PasswordRecoveryPageLocators, LoginPageLocators

import allure


class PasswordResetPage(PasswordRecoveryPage):

    @allure.step('Вводим имейл')
    def enter_email(self, email):
        self.enter_text_to_element(locator=PasswordRecoveryPageLocators.EMAIL_INPUT_FIELD, keys=email)

    @allure.step('Вводим пароль')
    def enter_password(self, password):
        self.enter_text_to_element(locator=PasswordRecoveryPageLocators.PASSWORD_INPUT_FIELD, keys=password)

    @allure.step('Нажимаем на кнопку Показать пароль')
    def show_password_click(self):
        self.click_element(ResetPasswordPageLocators.VIEW_PASSWORD_BUTTON)

    @allure.step('Проверяем активность поля ввода пароля')
    def show_password_check(self):
        return self.find_element_by_locator(ResetPasswordPageLocators.ACTIVE_INPUT_FIELD)

