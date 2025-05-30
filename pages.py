from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from data import MESSAGE_FOR_DRIVER, CARD_NUMBER, PHONE_NUMBER, CARD_CODE
from helpers import retrieve_phone_code
import time

class UrbanRoutesPage:
    # Locators
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    supportive_plan_card = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[1]/div[5]/div[2]')
    #supportive_plan_card_parent = (By.XPATH, '//div[contains(text(), "Supportive")]//')
    active_plan_card = (By.XPATH, '//div[@class="card active"]//div[@class="card-title"]')
    #call_taxi_button = (By.XPATH, '//button[contains(text(), "Call a taxi")]')
    call_taxi_button = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[1]/div[3]/div[1]/button')
    phone_number_field = (By.ID, 'phone')
    phone_number_button = (By.XPATH,'//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[1]/div')
    next_button = (By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/div[1]/form/div[2]/button')
    #next_button = (By.XPATH, '//button[contains(text(), "Next")]')
    enter_the_code_from_the_SMS_field = (By.ID, 'code')
    confirm_button = (By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/div[2]/form/div[2]/button[1]')
    #confirm_button = (By.XPATH, '//button[contains(text(), "Confirm")]')
    payment_method_button = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[2]/div[1]')
   #payment_method_button = (By.XPATH, '//button[contains(text(), "Payment method")]')
    add_card_button = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[1]/div[2]/div[3]/div[2]')
    #add_card_button = (By.XPATH, '//button[contains(text(), "Add card")]')    card_number_field = (By.ID, 'Card number')
    card_number = (By.ID, 'number')
    code_field = (By.XPATH, '/html/body/div/div/div[2]/div[2]/div[2]/form/div[1]/div[2]/div[2]/div[2]/input')
    link_button = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[2]/form/div[3]/button[1]')
    #link_button = (By.XPATH, '//button[contains(text(), "Link")]')
    close_button = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[1]/button')
    #close_button = (By.XPATH, '//div[@class="payment-picker open"]//button[@class="close-button section-close"]')
    message_to_the_driver_button = (By.XPATH, '/html/body/div/div/div[3]/div[3]/div[2]/div[2]/div[3]/div/label')
    message_to_the_driver  = (By.XPATH, '/html/body/div/div/div[3]/div[3]/div[2]/div[2]/div[3]/div/input')
    blanket_and_handkerchiefs_selector_button = (By.CLASS_NAME, 'switch')
    blanket_and_handkerchiefs_check = (By.CLASS_NAME, 'switch-input')
    order_2_ice_creams = (By.XPATH, '/html/body/div/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[3]/div/div[2]/div[1]/div/div[2]/div/div[3]')
    enter_the_number_and_order_button = (By.CLASS_NAME, 'smart-button-main')

    def __init__(self, driver):
        self.driver = driver

    def set_from(self,from_address):
        self.driver.find_element(*self.from_field).send_keys(from_address)

    def set_to(self, to_address):
        self.driver.find_element(*self.to_field).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def click_call_taxi_button(self):
        self.driver.find_element(*self.call_taxi_button).click()

    def set_route(self,from_address, to_address):
        self.set_from(from_address)
        self.set_to(to_address)
        self.click_call_taxi_button()

    def click_supportive_plan(self):
        self.driver.find_element(*self.supportive_plan_card).click()

    def is_supportive_plan_selected(self):
        supportive_plan = self.driver.find_element(*self.supportive_plan_card)
    # Check if the plan is selected (you mentioned it turns gray when selected)
        return "selected" in supportive_plan.get_attribute("class")  # Adjust based on actual HTML

    def click_phone_number_button(self):
        self.driver.find_element(*self.phone_number_button).click()

    def set_phone_number(self, phone_number):
        self.driver.find_element(*self.phone_number_field).send_keys(PHONE_NUMBER)

    def get_phone_number(self):
        return self.driver.find_element(*self.phone_number_button).get_property('value')

    def click_next_button(self):
        self.driver.find_element(*self.next_button).click()

    def set_phone_number_code(self, SMS_code):
        self.driver.find_element(*self.enter_the_code_from_the_SMS_field).send_keys(SMS_code)

    def click_confirm_button(self):
        self.driver.find_element(*self.confirm_button).click()

    def click_close_button(self):
        self.driver.find_element(*self.close_button).click()

    def click_payment_method_button(self):
        self.driver.find_element(*self.payment_method_button).click()

    def click_add_card_button(self):
        self.driver.find_element(*self.add_card_button).click()

    def set_card_number(self, card_number):
        self.driver.find_element(*self.card_number).send_keys(card_number)

    def get_card_number(self):
        return self.driver.find_element(*self.card_number).get_property('value')

    def set_code_field(self, code):
        self.driver.find_element(*self.code_field).send_keys(CARD_CODE)

    def get_code(self):
        return self.driver.find_element(*self.code_field).get_property('value')

    def click_link_button(self):
        self.driver.find_element(*self.link_button).click()

    def click_message_to_the_driver_button(self):
        self.driver.find_element(*self.message_to_the_driver_button).click()

    def set_message_to_the_driver(self, message_to_the_driver):
        return self.driver.find_element(*self.message_to_the_driver).send_keys(MESSAGE_FOR_DRIVER)

    def get_message_to_the_driver(self):
        return self.driver.find_element(*self.message_to_the_driver).get_property('value')

    def order_a_blanket(self):
        self.driver.find_element(*self.blanket_and_handkerchiefs_selector_button).click()

    def get_blanket_and_handkerchiefs(self):
        return self.driver.find_element(*self.blanket_and_handkerchiefs_check).get_property('checked')

    def click_order_2_ice_creams(self):
        self.driver.find_element(*self.order_2_ice_creams).click()

    def click_enter_the_number_and_order(self):
        self.driver.find_element(*self.enter_the_number_and_order_button).click()








