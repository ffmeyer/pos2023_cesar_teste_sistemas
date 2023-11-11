from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.PageObject import PageObject


class ManagerCustomersPage(PageObject):

    def __init__(self, browser):
        self.super(ManagerCustomersPage, self).__init__(browser=browser)
        self.input_search_customer = 'input[placeholder="Search Customer"]'
        self.tbl_firstname = ''
        self.tbl_lastname = ''
        self.tbl_post_code = ''
        self.tbl_account_number = ''
        self.tbl_delete_button = ''