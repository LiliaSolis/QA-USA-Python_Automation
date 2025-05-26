from selenium import webdriver
import data
import helpers
from pages import UrbanRoutesPage, click_payment_method


class TestUrbanRoutes:
    @classmethod
    def test_setup_class(cls):
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
        routes_page.click_custom_option()
        routes_page.click_taxi_icon()

            # Verify "Call a taxi" text appears
        actual_value = routes_page.get_taxi_text()
        expected_value = "Call a taxi"
        assert expected_value in actual_value, f"Expected '{expected_value}', but got '{actual_value}'"

            # Select Supportive plan with conditional check
        routes_page.select_supportive_plan()  # This method should contain the if condition

            # Verify Supportive plan is selected
        assert routes_page.is_supportive_plan_selected(), "Supportive plan should be selected"

    def test_fill_phone_number(self):  # Add in S8
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.get_phone_number.send_keys()
        routes_page.get_retrive_phone_code.send_keys()
        assert routes_page.get_PHONE_NUMBER() == data.PHONE_NUMBER

    def test_fill_card(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_payment_method.button()
        routes_page.click_add_a_card.button()
        routes_page.enter_card_number.field()
        routes_page.enter_card_code.field()

    def test_comment_for_driver(self):  # Add in S8
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.enter_message_for_driver.field()

    def test_order_blanket_and_handkerchiefs(self):  # Add in S8
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_order_blanket_and_handkerchiefs.button()

    def test_order_2_ice_creams(self):  # Add in S8
            for order in range(2)
                print(order)

    def test_car_search_model_appears(self):  # Add in S8
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_enter_the_number_and_order.button()

        @classmethod
        def teardown_class(cls):
            cls.driver.quit()