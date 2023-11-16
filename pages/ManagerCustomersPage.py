import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.PageObject import PageObject


class ManagerCustomersPage(PageObject):

    def __init__(self, browser):
        super(ManagerCustomersPage, self).__init__(driver=browser)
        self.input_search_customer = 'input[placeholder="Search Customer"]'
        self.tbl_firstname = 'input[placeholder="First Name"]'
        self.tbl_lastname = 'input[placeholder="Last Name"]'
        self.tbl_post_code = 'input[placeholder="Post Code"]'
        self.tbl_account_number = ''
        self.tbl_delete_button = '//button[contains(text(),"Delete")]'

    def delete_user(self):
        element = self.wait_visible_element_selected(By.CSS_SELECTOR, self.tbl_delete_button, 10)
        element.click()
