from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from pages.PageObject import PageObject
from selenium.webdriver.support.ui import Select


class CustomerLoginPage(PageObject):

    def __init__(self, driver):
        super(CustomerLoginPage, self).__init__(driver=driver)
        self.select_user = 'userSelect'
        self.btn_login = 'button[type="submit"]'
        self.btn_logout = '.btn.logout'

    def select_user_name(self, username):
        element = self.wait_visible_element_selected(By.ID, self.select_user, 10)
        combobox = Select(element)
        combobox.select_by_visible_text(username)
        self.click_login_btn()

    def click_login_btn(self):
        self.wait_visible_element_selected(By.CSS_SELECTOR, self.btn_login, 10).click()

    def click_logout_btn(self):
        self.driver.find_element(By.ID, self.btn_logout).click()

    def is_url_login(self):
        return self.is_url(self.url)
