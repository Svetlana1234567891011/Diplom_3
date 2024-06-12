from conftest import fake
from pages.login_page import LoginPage
from pages.password_recovery_page import PasswordRecoveryPage
from pages.reset_password_page import PasswordResetPage
import allure

from utils.special_requests import generate_random_string
from utils.urls import URLS

randoms_string = generate_random_string(10)

email = fake.email()


class TestPasswordRecovery:
    @allure.title('По кнопке Восстановить пароль переходим на страницу восстановления пароля')
    def test_password_recovery_brings_to_recovery_page(self, driver):
        entrance_page = LoginPage(driver)
        entrance_page.open_page(subdir=URLS.LOGIN_PAGE_SECTION)
        entrance_page.wait_for_login_page_header()
        entrance_page.click_restore_password()
        password_recovery_page = PasswordRecoveryPage(driver)
        password_recovery_page.wait_for_recovery_page_header()

        assert password_recovery_page.try_out_url(subdir=URLS.RECOVER_PASSWORD_SECTION)

    @allure.title('По кнопке Восстановить пароль переходим на страницу восстановления пароля')
    def test_password_reset_for_valid_email(self, driver):
        #payload = create_user_payload(name='randoms_string', password='randoms_string', email='email')

        password_recovery_page = PasswordRecoveryPage(driver)
        password_recovery_page.open_page(subdir=URLS.RECOVER_PASSWORD_SECTION)
        password_recovery_page.wait_for_recovery_page_header()
        email_new_one = email
        password_recovery_page.enter_email(email_new_one)
        password_recovery_page.recover_button_click()
        reset_password_page = PasswordResetPage(driver)
        reset_password_page.wait_for_recovery_page_header()

        assert reset_password_page.try_out_url(subdir=URLS.RECOVER_PASSWORD_SECTION)

    @allure.title('Кнопка "Показать пароль" делает поле ввода пароля активным')
    def test_password_reset_gets_highlighted(self, driver):
        password_recovery_page = PasswordRecoveryPage(driver)
        password_recovery_page.open_page(subdir=URLS.RECOVER_PASSWORD_SECTION)
        password_recovery_page.wait_for_recovery_page_header()
        email_new_one = email
        password_recovery_page.enter_email(email_new_one)
        password_recovery_page.recover_button_click()
        reset_password_page = PasswordResetPage(driver)
        reset_password_page.wait_for_recovery_page_header()
        password_new = 'randoms_string'
        #reset_password_page.enter_email(email_new) #ввести мейл
        reset_password_page.enter_password(password_new)
        reset_password_page.show_password_click()

        assert reset_password_page.show_password_check()
