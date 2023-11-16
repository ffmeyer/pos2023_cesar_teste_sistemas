from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.PageObject import PageObject


class CustomerTransactionPage(PageObject):

    def __init__(self, browser):
        super(CustomerTransactionPage, self).__init__(driver=browser)
        self.css_btn_back = '.btn[ng-click="back()"]'
        self.css_btn_reset = '.btn[ng-show="showDate"]'
        self.css_tbl_amount = ''
        self.css_tbl_transaction_type = ''
        