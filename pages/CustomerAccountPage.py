from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.PageObject import PageObject


class CustomerAccountPage(PageObject):

    def __init__(self, driver):
        super(CustomerAccountPage, self).__init__(driver=driver)
        self.lbl_user_name = '.fontBig.ng-binding'
        self.select_account_number = '#accountSelect'
        self.lbl_account_number = '.ng-binding[shub-ins="1"]'
        self.lbl_balance = '.ng-binding[shub-ins="1"]'
        self.lbl_currency = '.ng-binding[shub-ins="3"]'
        self.btn_transaction = '.btn.btn-lg.tab[ng-class="btnClass1"]'
        self.btn_deposit = '.btn.btn-lg.tab[ng-class="btnClass2"]'
        self.btn_withdrawl = '.btn.btn-lg.tab[ng-class="btnClass3"]'
        self.input_amount = 'input[placeholder="amount"]'
        self.btn_submit = 'button[type="submit"]'

        # Mensagem de erro na tela
        self.msg_withdrawl = '.error.ng-binding'

    def read_balance_value(self):
        balance = self.wait_visible_element_selected(By.CSS_SELECTOR, self.select_account_number, 10)
        return balance.text

    def select_deposit_option(self):
        self.wait_visible_element_selected(By.CSS_SELECTOR, self.btn_deposit, 10).click()

    def select_withdrawl_option(self):
        self.wait_visible_element_selected(By.CSS_SELECTOR, self.btn_withdrawl, 10).click()

    def click_transactions_option(self):
        self.wait_visible_element_selected(By.CSS_SELECTOR, self.btn_transaction, 10).click()
        sleep(4)

    def type_amount(self, value):
        self.wait_visible_element_selected(By.CSS_SELECTOR, self.input_amount, 10).send_keys(value)

    def click_submit(self):
        self.driver.find_element(By.CSS_SELECTOR, self.btn_submit).click()

    def has_message_error_withdraw(self):
        return self.wait_visible_element(By.CSS_SELECTOR, self.msg_withdrawl, 10)

    def make_a_deposit(self, value):
        self.select_deposit_option()
        sleep(1)
        self.type_amount(value)
        self.click_submit()
        sleep(1)

    def make_a_withdrawl(self, value):
        self.select_withdrawl_option()
        sleep(1)
        self.type_amount(value)
        self.click_submit()
        sleep(1)


