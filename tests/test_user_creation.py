from pages.ManagerAddCustomerPage import ManagerAddCustomerPage
from utils.UserGenerator import User


class Test_user_creation:

    # CT-001 - Criação de Usuario
    def test_user_creation(self, open_browser):
        login_p = open_browser
        login_p.click_bank_manager_btn()
        mac_p = ManagerAddCustomerPage(open_browser.driver)
        mac_p.click_bank_manager_add_customer()
        a_user = User()
        user = a_user.generate_user()
        mac_p.create_user(first_name=user.first_name, last_name=user.last_name, postal_code=user.postal_code)
        assert mac_p.has_message_sucessfull_new_user(), 'Erro ao criar usuario'
        mac_p.close_alert()

