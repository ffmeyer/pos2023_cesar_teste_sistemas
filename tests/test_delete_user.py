
from pages.ManagerCustomersPage import ManagerCustomersPage


class Test4:

    def test_delete_user(self, create_user):
        login_p, user = create_user
        login_p.click_bank_manager_btn()

        customer_page = ManagerCustomersPage(login_p.driver)

        customer_page.delete_user()


