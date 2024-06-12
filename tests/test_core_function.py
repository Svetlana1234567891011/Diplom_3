from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.order_feed import OrderFeedPage
import allure
from utils.urls import URLS


class TestMainFunctionality:
    @allure.title('Из личного кабинета можно перейти в Конструктор')
    def test_redirect_to_constructor(self, driver):
        entrance_page = LoginPage(driver)
        entrance_page.open_page(URLS.LOGIN_PAGE_SECTION)
        entrance_page.wait_for_login_page_header()
        entrance_page.click_constructor()
        main_page = MainPage(driver)
        main_page.wait_for_main_page_header()

        assert main_page.try_out_url()

    @allure.title('Из основной страницы можно перейти в Ленту Заказов')
    def test_redirect_to_orders_feed(self, driver):
        entrance_page = LoginPage(driver)
        entrance_page.open_page(URLS.LOGIN_PAGE_SECTION)
        entrance_page.click_constructor()
        entrance_page.try_out_url()
        main_page = MainPage(driver)
        main_page.wait_for_main_page_header()
        main_page.click_feed_of_orders()
        order_line = OrderFeedPage(driver)

        assert order_line.try_out_url(URLS.FEED_SECTION)

    @allure.title('Если кликнуть на ингредиент, появится всплывающее окно с деталями')
    def test_click_to_ingredient_opens_details_modal(self, driver):
        main_page = MainPage(driver)
        main_page.open_page()
        main_page.wait_for_main_page_header()
        main_page.click_first_ingredient()

        assert main_page.try_out_opening_of_modal()

    @allure.title('Всплывающее окно с деталями закрывается крестиком')
    def test_click_to_x_closes_ingredient_popup(self, driver):
        main_page = MainPage(driver)
        main_page.open_page()
        main_page.wait_for_main_page_header()
        main_page.click_first_ingredient()
        main_page.wait_for_modal_header()
        main_page.click_cross_of_modal()

        assert not main_page.try_out_opening_of_modal()

    @allure.title('Добавление ингредиента в заказы увеличивает счетчик этого ингредиента')
    def test_drag_and_drop_ingredient_to_basket_increases_ingredient_count(self, driver):
        main_page = MainPage(driver)
        main_page.open_page()
        main_page.wait_for_main_page_header()
        initial_value = main_page.get_value_of_ingredient_counter()
        main_page.drag_n_drop_first_ingredient_to_basket()
        updated_value = main_page.get_value_of_ingredient_counter()

        assert initial_value < updated_value

    @allure.title('Залогиненный пользователь может оформить заказ')
    def test_login_user_can_place_order(self, driver, user_with_payload):
        entrance_page = LoginPage(driver)
        entrance_page.open_page(URLS.LOGIN_PAGE_SECTION)
        entrance_page.wait_for_login_page_header()
        entrance_page.fill_email_and_password_and_enter(email=user_with_payload.payload['email'],
                                                        password=user_with_payload.payload['password'])
        main_page = MainPage(driver)
        main_page.try_out_order_button()
        main_page.drag_n_drop_first_ingredient_to_basket()
        main_page.click_button_of_making_order()

        assert main_page.try_out_opening_of_modal()



