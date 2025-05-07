import data
import helpers
from helpers import is_url_rea
from selenium import webdriver
import time
from urban_route_main_page import UrbanRoutesPage

class TestUrbanRoutes:
    @classmethod
    def setup_class(cls):
        if is_url_reachable == "https://cnt-8bc31ae9-a7ba-4a3b-b6e0-3b13389243eb.containerhub.tripleten-services.com/"
            return print("Connected to the Urban Routes server")
        else:
            return print("Cannot connect to Urban Routes. Check the server is on and still running")
    from selenium.webdriver import DesiredCapabilities
    capabilities = DesiredCapabilities.CHROME
    capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
    cls.driver = webdriver.Chrome()

    def test_set_route(self):  # Add in S8
        print("function created for set route")
        pass  # Placeholder for future implementation

    def test_select_plan(self):  # Add in S8
        print()
        pass  # Placeholder for future implementation

    def test_fill_phone_number(self):  # Add in S8
        print()
        pass  # Placeholder for future implementation

    def test_fill_card(self):  # Add in S8
        print()
        pass  # Placeholder for future implementation

    def test_comment_for_driver(self):  # Add in S8
        print()
        pass  # Placeholder for future implementation

    def test_order_blanket_and_handkerchiefs(self):  # Add in S8
        print()
        pass  # Placeholder for future implementation

    def test_order_2_ice_creams(self):  # Add in S8
        for order in range(2)
        print(order)
        pass  # Placeholder for future implementation

    def test_car_search_model_appears(self):  # Add in S8
        print()
        pass  # Placeholder for future implementation

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
