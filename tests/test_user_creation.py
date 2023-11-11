from pages.ManagerAddCustomerPage import ManagerAddCustomerPage


class Test1:

    def test_create_user(self, open_browser):
        login_p = open_browser
        login_p.click_bank_manager_btn()
        mac_p = ManagerAddCustomerPage(open_browser.driver)
        mac_p.click_bank_manager_add_customer()
        mac_p.create_user(firstname='name1', lastname='lastName', postalcode='11111')
        assert mac_p.has_message_sucessfull_new_user(), 'Erro ao criar usuario'
        print(mac_p.get_customer_id())


