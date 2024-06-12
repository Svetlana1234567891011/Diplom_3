from pages.private_area_page import ProfilePage
from pages.login_page import LoginPage
from pages.main_page import MainPage
import allure
from utils.urls import URLS


class TestPrivateArea:
    @allure.title('По клику на кнопку "Личный кабинет" переходим на страницу входа в Личный Кабинет')
    def test_main_page_route_to_private_area(self, driver):
        main_page = MainPage(driver)
        main_page.open_page()
        main_page.wait_for_main_page_header()
        main_page.click_private_area_button()
        login_page = ProfilePage(driver)  # Создаем экземпляр ProfilePage
        assert login_page.wait_for_private_area_submit_button()

    @allure.title('Из личного кабинета можно перейти в Историю Заказов')
    def test_private_area_route_to_history(self, driver, user_with_payload):
        login_page = LoginPage(driver)
        login_page.open_page(subdir=URLS.LOGIN_PAGE_SECTION)
        login_page.wait_for_login_page_header()
        login_page.fill_email_and_password_and_enter(email=user_with_payload.payload['email'],
                                                     password=user_with_payload.payload['password'])

        main_page = MainPage(driver)
        main_page.wait_for_main_page_header()
        main_page.click_private_area_button()
        main_page.try_out_url(URLS.PRIVATE_AREA_SECTION)
        private_page = ProfilePage(driver)
        private_page.wait_for_private_area_header()
        private_page.click_orders_history_section_name()

        assert login_page.try_out_url(URLS.HISTORY_SECTION)

    @allure.title('Из личного кабинета можно Выйти из аккаунта')
    def test_account_logout(self, driver, user_with_payload):
        entrance_page = LoginPage(driver)
        entrance_page.open_page(URLS.LOGIN_PAGE_SECTION)
        entrance_page.wait_for_login_page_header()
        entrance_page.fill_email_and_password_and_enter(email=user_with_payload.payload['email'],
                                                        password=user_with_payload.payload['password'])
        main_page = MainPage(driver)
        main_page.wait_for_main_page_header()
        main_page.click_private_area_button()
        main_page.try_out_url(URLS.PRIVATE_AREA_SECTION)
        profile_page = ProfilePage(driver)
        profile_page.wait_for_private_area_header()
        profile_page.try_out_url(URLS.PRIVATE_AREA_SECTION)
        profile_page.click_exit()
        entrance_page.try_out_url(URLS.LOGIN_PAGE_SECTION)
        entrance_page.wait_for_login_page_header()
        entrance_page.click_constructor()
        entrance_page.try_out_url()
        main_page.wait_for_main_page_header()

        assert main_page.try_out_enter_button()
