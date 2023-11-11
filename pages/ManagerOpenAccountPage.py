from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.PageObject import PageObject


class ManagerOpenAccountPage(PageObject):

    def __init__(self, browser):
        self.super(ManagerOpenAccountPage, self).__init__(browser=browser)
        self.select_customer = '#userSelect'
        self.select_currency = '#currency'
        self.brn_process = 'button[type="submit"]'