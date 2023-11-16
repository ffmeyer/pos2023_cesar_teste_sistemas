from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.PageObject import PageObject


class ManagerOpenAccountPage(PageObject):
    CURRENCY_DOLLAR = 'Dollar'
    CURRENCY_POUND = 'Pound'
    CURRENCY_RUPEE = 'Rupee'

    def __init__(self, browser):
        super(ManagerOpenAccountPage, self).__init__(driver=browser)
        self.css_btn_open_account = '.btn.btn-lg.tab[ng-class="btnClass2"]'
        self.css_select_customer = '#userSelect'
        self.css_select_currency = '#currency'
        self.css_btn_process = 'button[type="submit"]'

        # validacao de tela (alert)
        self.msg_validate_user_association_successfull = 'Account created successfully with account Number'

    def click_bank_manager_open_account(self):
        element = self.wait_visible_element_selected(By.CSS_SELECTOR, self.css_btn_open_account, 10)
        element.click()

    def select_user_account(self, username):
        element = self.wait_visible_element_selected(By.CSS_SELECTOR, self.css_select_customer, 10)
        combobox = Select(element)
        combobox.select_by_visible_text(username)

    def select_currency(self, currency):
        element = self.wait_visible_element_selected(By.CSS_SELECTOR, self.css_select_currency, 10)
        combobox = Select(element)
        combobox.select_by_visible_text(currency)

    def click_process(self):
        element = self.wait_visible_element_selected(By.CSS_SELECTOR, self.css_btn_process, 10)
        element.click()

    def create_new_account(self, username, currency):
        self.select_user_account(username)
        self.select_currency(currency)
        self.click_process()

    def create_new_account_in_dollar(self, username):
        return self.create_new_account(username=username, currency=self.CURRENCY_DOLLAR)

    def create_new_account_in_pounds(self, username):
        return self.create_new_account(username=username, currency=self.CURRENCY_POUND)

    def create_new_account_in_rupee(self, username):
        return self.create_new_account(username=username, currency=self.CURRENCY_RUPEE)

    def has_message_sucessfull_association(self):
        return self.msg_validate_user_association_successfull in self.wait_visible_alert_selected().text

    def get_account_number(self):
        return self.wait_visible_alert_selected().text.split(':')[1]

    def close_alert(self):
        alert = self.wait_visible_alert_selected()
        alert.accept()