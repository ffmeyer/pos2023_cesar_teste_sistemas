
from pages.ManagerCustomersPage import ManagerCustomersPage


class Test4:

    def test_delete_user(self, create_user):
        login_p, user = create_user
        login_p.click_bank_manager_btn()
        customer_page = ManagerCustomersPage(login_p.driver)
        customer_page.click_bank_manager_list_customers()
        customer_page.type_search_customer(user.first_name)
        customer_page.delete_user()
        print('apagou!')


