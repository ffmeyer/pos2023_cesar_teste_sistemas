from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.PageObject import PageObject


class HeaderPage(PageObject):

    def __init__(self, driver):
        super(HeaderPage, self).__init__(driver=driver)
        self.btn_home = '.btn.home'
        self.btn_logout = '.btn.logout'

    def click_home_btn(self):
        self.driver.find_element(By.CSS_SELECTOR, self.btn_home).click()

    def click_logout_btn(self):
        self.driver.find_element(By.CSS_SELECTOR, self.btn_logout).click()
