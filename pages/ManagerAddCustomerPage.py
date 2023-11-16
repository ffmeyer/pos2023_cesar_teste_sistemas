from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.PageObject import PageObject


class ManagerAddCustomerPage(PageObject):

    def __init__(self, browser):
        super(ManagerAddCustomerPage, self).__init__(driver=browser)
        self.css_input_add_customer = '.btn.btn-lg.tab[ng-class="btnClass1"]'
        self.css_input_first_name = 'input[placeholder="First Name"]'
        self.css_input_last_name = 'input[placeholder="Last Name"]'
        self.css_input_post_code = 'input[placeholder="Post Code"]'
        self.css_input_submit_customer = 'button[type="submit"]'

        # validacao de tela (alert)
        self.msg_validate_user_creation_successfull = 'Customer added successfully with customer id'


    def click_bank_manager_add_customer(self):
        element = self.wait_visible_element_selected(By.CSS_SELECTOR, self.css_input_add_customer, 10)
        element.click()

    def type_first_name(self, firstname):
        element = self.wait_visible_element_selected(By.CSS_SELECTOR, self.css_input_first_name, 10)
        element.send_keys(firstname)

    def type_last_name(self, lastname):
        element = self.wait_visible_element_selected(By.CSS_SELECTOR, self.css_input_last_name, 10)
        element.send_keys(lastname)

    def type_postal_code(self, postalcode):
        element = self.wait_visible_element_selected(By.CSS_SELECTOR, self.css_input_post_code, 10)
        element.send_keys(postalcode)

    def click_submit_customer(self):
        self.driver.find_element(By.CSS_SELECTOR, self.css_input_submit_customer).click()

    def create_user(self, first_name, last_name, postal_code):
        self.type_first_name(first_name)
        self.type_last_name(last_name)
        self.type_postal_code(postal_code)
        self.click_submit_customer()

    def has_message_sucessfull_new_user(self):
        yield self.msg_validate_user_creation_successfull in self.wait_visible_alert_selected().text

    def close_alert(self):
        alert = self.wait_visible_alert_selected()
        alert.accept()