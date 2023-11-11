from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.PageObject import PageObject


class CustomerAccountPage(PageObject):

    def __init__(self, browser):
        super(CustomerAccountPage, self).__init__(browser=browser)
        self.lbl_user_name = '.fontBig.ng-binding'
        self.select_account_number = '#accountSelect'
        self.lbl_account_number = '.ng-binding[shub-ins="1"]'
        self.lbl_balance = '.ng-binding[shub-ins="1"]'
        self.lbl_currency = '.ng-binding[shub-ins="1"]'
        self.btn_transaction = '.btn.btn-lg.tab[ng-class="btnClass1"]'
        self.btn_deposit = '.btn.btn-lg.tab[ng-class="btnClass2"]'
        self.btn_withdrawl = '.btn.btn-lg.tab[ng-class="btnClass3"]'
        self.input_amount = 'input[placeholder="amount"]'
        self.btn_submit = 'button[type="submit"]'

