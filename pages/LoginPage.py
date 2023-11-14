from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.PageObject import PageObject


class LoginPage(PageObject):

    def __init__(self, browser):
        super(LoginPage, self).__init__(browser=browser)
        self.btn_customer_login = '.btn.btn-primary.btn-lg[ng-click="customer()"]'
        self.btn_bank_manage_login = '.btn.btn-primary.btn-lg[ng-click="manager()"]'

    def open_page(self):
        self.driver.get(self.url)

    def click_customer_btn(self):
        element = self.wait_visible_element_selected(By.CSS_SELECTOR, self.btn_customer_login, 10)
        element.click()

    def click_bank_manager_btn(self):
        element = self.wait_visible_element_selected(By.CSS_SELECTOR, self.btn_bank_manage_login, 10)
        element.click()

    def is_url_login(self):
        return self.is_url(self.url)
