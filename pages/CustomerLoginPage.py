from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.PageObject import PageObject


class CustomerLoginPage(PageObject):

    def __init__(self, browser):
        super(CustomerLoginPage, self).__init__(browser=browser)
        self.select_user = '#userSelect'
        self.btn_login = 'button[type="submit"]'
        self.btn_logout = '.btn.logout'

    def select_user(self, name):
        print(name)

    def click_login_btn(self):
        self.driver.find_element(By.ID, self.btn_login).click()

    def click_logout_btn(self):
        self.driver.find_element(By.ID, self.btn_logout).click()

    def is_url_login(self):
        return self.is_url(self.url)
