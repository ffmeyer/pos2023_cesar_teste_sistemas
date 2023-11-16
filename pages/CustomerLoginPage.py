from selenium import webdriver
from selenium.webdriver.common.by import By
import random
from pages.PageObject import PageObject
from selenium.webdriver.support.ui import Select


class CustomerLoginPage(PageObject):

    def __init__(self, browser):
        super(CustomerLoginPage, self).__init__(driver=browser)
        self.css_select_customer = '#userSelect'

    def select_user_account(self, username):
        element = self.wait_visible_element_selected(By.CSS_SELECTOR, self.select_user, 10)
        combobox = Select(element)
        combobox.select_by_visible_text(username)

    def select_random_available_user(self):
        element = self.wait_visible_element_selected(By.CSS_SELECTOR, self.css_select_customer, 10)
        combobox = Select(element)
        index = random.randint(1, len(combobox.options))
        return combobox.options[index].text

