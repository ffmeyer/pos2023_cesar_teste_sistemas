from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pages.PageObject import PageObject


class CustomerAccountPage(PageObject):

    def __init__(self, browser):
        super(CustomerAccountPage, self).__init__(driver=browser)
        self.css_lbl_user_name = '.fontBig.ng-binding'
        self.css_select_account_number = '#accountSelect'
        self.css_lbl_account_number = 'strong[class="ng-binding"]'
        self.css_lbl_balance = 'strong[class="ng-binding"]'
        self.css_lbl_currency = 'strong[class="ng-binding"]'
        self.css_btn_transaction = '.btn.btn-lg.tab[ng-class="btnClass1"]'
        self.css_btn_deposit = '.btn.btn-lg.tab[ng-class="btnClass2"]'
        self.css_btn_withdrawl = '.btn.btn-lg.tab[ng-class="btnClass3"]'
        self.css_input_amount = 'input[placeholder="amount"]'
        self.css_btn_submit = 'button[type="submit"]'

        # Mensagem na tela
        self.css_msg_red = '.error.ng-binding'

    def read_balance_value(self):
        balance = self.wait_visible_elements_selected(By.CSS_SELECTOR, self.css_lbl_balance, 10)
        return balance[1].text

    def read_acc_number(self):
        acc = self.wait_visible_elements_selected(By.CSS_SELECTOR, self.css_lbl_account_number, 10)
        return acc[0].text

    def change_account(self, account):
        element = self.wait_visible_element_selected(By.CSS_SELECTOR, self.css_select_account_number, 10)
        combobox = Select(element)
        combobox.select_by_visible_text(account)

    def select_deposit_option(self):
        self.wait_visible_element_selected(By.CSS_SELECTOR, self.css_btn_deposit, 10).click()

    def select_withdrawl_option(self):
        self.wait_visible_element_selected(By.CSS_SELECTOR, self.css_btn_withdrawl, 10).click()

    def click_transactions_option(self):
        self.wait_visible_element_selected(By.CSS_SELECTOR, self.css_btn_transaction, 10).click()

    def type_amount(self, value):
        self.wait_visible_element_selected(By.CSS_SELECTOR, self.css_input_amount, 10).send_keys(value)

    def click_submit(self):
        self.wait_visible_element_selected(By.CSS_SELECTOR, self.css_btn_submit, 10).click()

    def read_message(self):
        message = self.wait_visible_element_selected(By.CSS_SELECTOR, self.css_msg_red, 10)
        return message.text

    def make_a_deposit(self, value):
        self.select_deposit_option()
        self.type_amount(value)
        sleep(1) #wait nao funciona na execucao da automacao
        self.click_submit()

    def make_a_withdrawl(self, value):
        self.select_withdrawl_option()
        sleep(1) #wait nao funciona na execucao da automacao
        self.type_amount(value)
        self.click_submit()

