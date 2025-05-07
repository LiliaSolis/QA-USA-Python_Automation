import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from data import PHONE_NUMBER, CARD_NUMBER, CARD_CODE, MESSAGE_FOR_DRIVER


class UrbanRoutesPage:
    # Locators
    FROM_FIELD = (By.ID, 'from')
    TO_FIELD = (By.ID, 'to')
    # Add other locators
    CARD_NUMBER = (By.CLASS_NAME, 'card-input')
    CARD_CODE = (By.CLASS_NAME, 'code')

def test_custom_taxi_option(self):
    self.driver.get('https://cnt-ba4ac5d1-085a-4e41-9066-bf5566bd0936.containerhub.tripleten-services.com/')
    urban_routes_page = UrbanRoutesPage(self.driver)
    urban_routes_page.enter_locations('East 2nd Street, 601', '1300 1st St')
    urban_routes_page.click_custom_option()
    time.sleep(2)
    urban_routes_page.click_taxi_icon()
    time.sleep(2)
    actual_value = urban_routes_page.get_taxi_text()
    expected_value = "Taxi"
    assert expected_value in actual_value, f"Expected '{expected_value}', but got '{actual_value}'"

def test_call_a_taxi_custom_taxi_option(self):
    self.driver.get('https://cnt-ba4ac5d1-085a-4e41-9066-bf5566bd0936.containerhub.tripleten-services.com/')
    urban_routes_page = UrbanRoutesPage(self.driver)
    urban_routes_page.enter_locations('East 2nd Street, 601', '1300 1st St')
    urban_routes_page.click_custom_option()
    time.sleep(2)
    urban_routes_page.click_taxi_icon()
    time.sleep(2)
    urban_routes_page.click_call_a_taxi_icon()
    time.sleep(2)
    actual_value = urban_routes_page.get_call_a_taxi_text()
    expected_value = "Call a taxi"
    assert expected_value in actual_value, f"Expected '{expected_value}', but got '{actual_value}'"

def select_supportive_plan():
    driver = webdriver.Chrome()
        # Open the app - update the URL after starting the server
    driver.get('https://cnt-ba4ac5d1-085a-4e41-9066-bf5566bd0936.containerhub.tripleten-services.com/')

    urban_routes_page = UrbanRoutesPage(self.driver)
    urban_routes_page.enter_locations('East 2nd Street, 601', '1300 1st St')
    urban_routes_page.click_custom_option()
    time.sleep(2)
    urban_routes_page.click_taxi_icon()
    time.sleep(2)
    urban_routes_page.click_call_a_taxi_icon()
    time.sleep(2)
    actual_value = urban_route_page.click_supportive_icon()
    if supportive icon is selected.click_phone_number_field()
    expected_value = "Supportive"
    assert expected_value in actual_value, f"Expected '{expected_value}', but got '{actual_value}'"

def retrieve_phone_code(driver) -> str:
        """This code retrieves phone confirmation number and returns it as a string.
        Use it when application waits for the confirmation code to pass it into your tests.
        The phone confirmation code can only be obtained after it was requested in application."""

def __init__(self, driver):
    self.driver = driver

def phone_number(self, phone):
    self.driver.find_element(*self.phone_number_field).send_keys(PHONE_NUMBER)

def click_payment_method(self):
        self.driver.find_element(*self.payment_method_button).click()

def click_add_a_card(self):
    self.driver.find_element(*self.add_a_card_button).click()

def card_number(self, card):
    self.driver.find_element(*self.card_number_field).send_keys(CARD_NUMBER)

def card_code(self, code):
    self.driver.find_element(*self.card_code_field).send_keys(CARD_CODE)

def message_for_driver(self, message):
    self.driver.find_element(*self.message_for_driver_field).send_keys(MESSAGE_FOR_DRIVER)

def click_order_blanket_handkerchiefs(self):
    self.driver.find_element(*self.order_blanket_handkerchiefs).click()

def click_order_ice_cream(self):
    self.driver.find_element(*self.order_ice_cream).click()
