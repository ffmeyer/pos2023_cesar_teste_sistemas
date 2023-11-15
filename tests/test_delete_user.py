
from pages.ManagerCustomersPage import ManagerCustomersPage


class Test4:

    def test_delete_user(self, open_browser):
        login_p = open_browser
        login_p.click_bank_manager_btn()
        customer_page = ManagerCustomersPage

        customer_page.delete_user


