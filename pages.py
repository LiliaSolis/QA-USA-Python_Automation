import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data import MESSAGE_FOR_DRIVER
from helpers import retrive_phone_code


class UrbanRoutesPage:
    # Locators
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    supportive_plan_card = (By.XPATH, '//div[contains(text(), "Supportive")]')
    supportive_plan_card_parent = (By.XPATH, '//div[contains(text(), "Supportive")]//')
    active_plan_card = (By.XPATH, '//div[@class="tcard active"]//div[@class="tcard-title"]')
    call_taxi_button = (By.XPATH, '//button[contains(text(), "Call a taxi")]')

def __init__(self, driver):
    self.driver = driver

def set_from(self,from_address):
    from_field = WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.from_field))
    from_field.send_keys(from_address)

def set_to(self, to_address):
    self.driver.find_element(*self.to_field).send_keys(to_address)

def get_from(self):
    return self.driver.find_element(*self.from_field).get_property('value')

def get_to(self):
    return self.driver.find_element(*self.to_field).get_property('value')

def click_call_taxi_button(self):
    WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.call_taxi_button))
    self.driver.find_element(*self.call_taxi_button).click()

def set_route(self,from_address, to_address):
    self.set_from(from_address)
    self.set_to(to_address)
    self.click_call_taxi_button()

def select_supportive_plan(self):
    supportive_plan = self.driver.find_element(*self.SUPPORTIVE_PLAN_LOCATOR)

    # Check if already selected (this is the required if condition)
    if not self.is_supportive_plan_selected():
    supportive_plan.click()

def is_supportive_plan_selected(self):
    supportive_plan = self.driver.find_element(*self.SUPPORTIVE_PLAN_LOCATOR)
    # Check if the plan is selected (you mentioned it turns gray when selected)
    return "selected" in supportive_plan.get_attribute("class")  # Adjust based on actual HTML

def phone_number(self, phone):
    self.driver.find_element(*self.phone_number_field).send_keys(PHONE_NUMBER)

def click_payment_method(self):
    self.driver.find_element(*self.payment_method_button).click()


def click_add_a_card(self):
    self.driver.find_element(*self.add_a_card_button).click()


def set_card_number(self, card):
    self.driver.find_element(*self.card_number_field).send_keys(CARD_NUMBER)


def set_card_code(self, code):
    self.driver.find_element(*self.card_code_field).send_keys(CARD_CODE)

def message_for_driver(self):
    self.driver.find_element(*self.message_for_driver_field).send_keys(MESSAGE_FOR_DRIVER)

def order_a_blanket(self):
    self.driver.find_element(*self.order_a_blanket_button).click()

def order_a_handkerchiefs(self):
    self.driver.find_element(*self.order_a_handkerchiefs_button).click()

def order_2_ice_creams(self):
    self.driver.find_element(*self.order_2_ice_creams_button).click()

def enter_the_number_and_order(self):
    self.driver.find_element(*self.click.enter_the_number_and_order).click()








