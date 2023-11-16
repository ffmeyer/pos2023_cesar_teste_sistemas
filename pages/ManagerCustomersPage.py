from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.PageObject import PageObject


class ManagerCustomersPage(PageObject):

    def __init__(self, browser):
        super(ManagerCustomersPage, self).__init__(driver=browser)
        self.css_btn_open_customer = '.btn.btn-lg.tab[ng-class="btnClass3"]'
        self.input_search_customer = 'input[placeholder="Search Customer"]'
        self.xpath_td_selected_firstname = '//tbody//td[1]'
        self.xpath_td_selected_lastname = '//tbody//td[2]'
        self.xpath_td_selected_postal_code = '//tbody//td[3]'
        self.xpath_td_selected_account_list = '//tbody//td[4]'
        self.xpath_td_selected_delete_button = 'button[ng-click="deleteCust(cust)"]'

    def click_bank_manager_list_customers(self):
        element = self.wait_visible_element_selected(By.CSS_SELECTOR, self.css_btn_open_customer, 10)
        element.click()

    def type_search_customer(self, user_property):
        element = self.wait_visible_element_selected(By.CSS_SELECTOR, self.input_search_customer, 10)
        element.send_keys(user_property)

    def get_selected_first_name(self):
        element = self.wait_visible_element_selected(By.XPATH, self.xpath_td_selected_firstname, 10)
        return element.text

    def get_selected_last_name(self):
        element = self.wait_visible_element_selected(By.XPATH, self.xpath_td_selected_lastname, 10)
        return element.text

    def get_selected_postal_code(self):
        element = self.wait_visible_element_selected(By.XPATH, self.xpath_td_selected_postal_code, 10)
        return element.text

    def get_selected_account_list(self):
        element = self.wait_visible_element_selected(By.XPATH, self.xpath_td_selected_account_list, 10)
        return element.text.split()

    def has_delete_button_displayed(self):
        return self.wait_visible_element(By.CSS_SELECTOR, self.xpath_td_selected_delete_button, 10)
