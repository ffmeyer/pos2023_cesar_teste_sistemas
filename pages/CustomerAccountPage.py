from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.PageObject import PageObject


class CustomerAccountPage(PageObject):

    def __init__(self, browser):
        super(CustomerAccountPage, self).__init__(driver=browser)
        self.css_lbl_user_name = '.fontBig.ng-binding'
        self.css_select_account_number = '#accountSelect'
        self.css_lbl_account_number = '.ng-binding[shub-ins="1"]'
        self.css_lbl_balance = 'strong[class="ng-binding"]'
        self.css_lbl_currency = '.ng-binding[shub-ins="1"]'
        self.css_btn_transaction = '.btn.btn-lg.tab[ng-class="btnClass1"]'
        self.css_btn_deposit = '.btn.btn-lg.tab[ng-class="btnClass2"]'
        self.css_btn_withdrawl = '.btn.btn-lg.tab[ng-class="btnClass3"]'
        self.css_input_amount = 'input[placeholder="amount"]'
        self.css_btn_submit = 'button[type="submit"]'

        # Mensagem de erro na tela
        self.css_msg_withdrawl = '.error.ng-binding'

    def read_balance_value(self):
        balance = self.wait_visible_elements_selected(By.CSS_SELECTOR, self.css_lbl_balance, 10)
        return balance[1].text

    def select_deposit_option(self):
        self.wait_visible_element_selected(By.CSS_SELECTOR, self.css_btn_deposit, 10).click()

    def select_withdrawl_option(self):
        self.wait_visible_element_selected(By.CSS_SELECTOR, self.css_btn_withdrawl, 10).click()

    def click_transactions_option(self):
        self.wait_visible_element_selected(By.CSS_SELECTOR, self.css_btn_transaction, 10).click()

    def type_amount(self, value):
        self.wait_visible_element_selected(By.CSS_SELECTOR, self.css_input_amount, 10).send_keys(value)

    def click_submit(self):
        self.driver.find_element(By.CSS_SELECTOR, self.css_btn_submit).click()

    def has_message_error_withdraw(self):
        return self.wait_visible_element(By.CSS_SELECTOR, self.css_msg_withdrawl, 10)

    def make_a_deposit(self, value):
        self.select_deposit_option()
        sleep(1)
        self.type_amount(value)
        self.click_submit()

    def make_a_withdrawl(self, value):
        self.select_withdrawl_option()
        sleep(1)
        self.type_amount(value)
        self.click_submit()

