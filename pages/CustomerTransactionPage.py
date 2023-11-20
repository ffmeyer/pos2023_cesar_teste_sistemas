from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.PageObject import PageObject


class CustomerTransactionPage(PageObject):

    def __init__(self, browser):
        super(CustomerTransactionPage, self).__init__(driver=browser)
        self.css_btn_back = '.btn[ng-click="back()"]'
        self.css_btn_reset = '.btn[ng-show="showDate"]'
        self.css_tbl_table = '.table.table-bordered.table-striped'
        self.css_tbl_row = '.ng-scope'
        self.css_tbl_cell = '.ng-binding'

    def click_back(self):
        self.driver.find_element(By.CSS_SELECTOR, self.css_btn_back).click()

    def read_transactions_info(self):
        lst = ()

        table = self.wait_visible_element_selected(By.CSS_SELECTOR, self.css_tbl_table, 10)
        rows = table.find_elements(By.CSS_SELECTOR, self.css_tbl_row)

        for i in range(len(rows)):
            amt = rows[i].find_elements(By.CSS_SELECTOR, self.css_tbl_cell)[1].text
            type = rows[i].find_elements(By.CSS_SELECTOR, self.css_tbl_cell)[2].text
            lst = lst + (amt, type)

        return lst


