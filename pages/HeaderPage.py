from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.PageObject import PageObject


class HeaderPage(PageObject):

    def __init__(self, browser):
        super(HeaderPage, self).__init__(driver=browser)
        self.css_btn_home = '.btn.home'
        self.css_btn_logout = '.btn.logout'

    def click_home_btn(self):
        self.driver.find_element(By.CSS_SELECTOR, self.css_btn_home).click()

    def click_logout_btn(self):
        self.driver.find_element(By.CSS_SELECTOR, self.css_btn_logout).click()
