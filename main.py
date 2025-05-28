from selenium import webdriver
import data
import helpers
from pages import UrbanRoutesPage


class TestUrbanRoutes:
    @classmethod
    def setup_class(cls):
        # do not modify - we need additional logging enabled in order to retrieve phone confirmation code
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(5)
        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print("Connected to the Urban Routes server")
        else:
            print("Cannot connect to Urban Routes. Check the server is on and still running")

    def test_set_route(self):  # Add in S8
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page =UrbanRoutesPage(self.driver)
        routes_page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        assert routes_page.get_from() == data.ADDRESS_FROM
        assert routes_page.get_to() == data.ADDRESS_TO

    def test_select_plan(self):  # Add in S8
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        routes_page.click_call_taxi_button()
        assert routes_page.click_call_taxi_button()

    def test_fill_phone_number(self):  # Add in S8
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        routes_page.click_call_taxi_button()
        routes_page.click_phone_number_field()
        routes_page.set_phone_number(data.PHONE_NUMBER)
        routes_page.click_next_button()
        routes_page.set_phone_number_code(helpers.retrieve_phone_code(self.driver))
        routes_page.click_confirm_button()
        routes_page.click_close_button()
        assert routes_page.click_phone_number_field()
        assert routes_page.set_phone_number_code()
        assert routes_page.click_confirm_button()
        assert routes_page.click_close_button()

    def test_fill_card(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        routes_page.click_payment_method_button()
        routes_page.click_add_card_button()
        routes_page.set_card_number()
        routes_page.get_card_number()
        routes_page.set_code_field()
        routes_page.click_link_button()
        routes_page.close_button()
        assert routes_page.get_card_number() == data.CARD_NUMBER
        assert routes_page.get_code() == data.CARD_CODE

    def test_comment_for_driver(self):  # Add in S8
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        routes_page.set_message_to_the_driver_field()
        routes_page.get_message_to_the_driver()
        assert routes_page.get_message_to_the_driver() == data.MESSAGE_FOR_DRIVER

    def test_order_blanket_and_handkerchiefs(self):  # Add in S8
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        routes_page.select_supportive_plan()
        routes_page.order_a_blanket()
        assert routes_page.get_blanket_and_handkerchiefs()

    def test_order_two_ice_creams(self):  # Add in S8
        for order in range(2):
            print(order)
        assert expected_value in actual_value, f"Expected '{expected_value}', but got '{actual_value}'"
        routes_page.select_order_two_ice_creams()
        assert routes_page.is_order_2_ice_creams_selected(), "Order ice creams should be selected"

    def test_car_search_model_appears(self):  # Add in S8
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        routes_page.click_enter_the_number_and_order.button()
        assert expected_value in actual_value, f"Expected '{expected_value}', but got '{actual_value}'"
        routes_page.select_enter_the_number_and_order()
        assert routes_page.is_enter_the_number_and_order_selected(), "Enter the number and order should be selected"

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()