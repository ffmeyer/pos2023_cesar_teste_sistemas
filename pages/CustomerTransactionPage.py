from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.PageObject import PageObject


class CustomerTransactionPage(PageObject):

    def __init__(self, browser):
        self.super(CustomerTransactionPage, self).__init__(browser=browser)
        self.btn_back = '.btn[ng-click="back()"]'
        self.btn_reset = '.btn[ng-show="showDate"]'
        self.tbl_amount = ''
        self.tbl_transaction_type = ''
        