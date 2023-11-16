from pages.ManagerAddCustomerPage import ManagerAddCustomerPage
from pages.ManagerCustomersPage import ManagerCustomersPage
from utils.UserGenerator import User


class Test_user_properties:
    # CT-003 - Busca de usuario na consulta do administrador
    def test_user_properties(self, create_user_account_association):
        login_p, user, account_id = create_user_account_association
        mcp_p = ManagerCustomersPage(login_p.driver)
        login_p.click_bank_manager_btn()
        mcp_p.click_bank_manager_list_customers()
        mcp_p.type_search_customer(user.first_name)
        assert mcp_p.get_selected_first_name() == user.first_name, 'First name nao confere'
        assert mcp_p.get_selected_last_name() == user.last_name, 'Last name nao confere'
        assert mcp_p.get_selected_postal_code() == user.postal_code, 'Postal code nao confere'
        assert mcp_p.get_selected_account_list()[0] == account_id, "Account numbers nao conferem"

    # CT-003.1 - Busca de usuario ja existente na consulta do administrador ()
    def test_already_exist_user_properties(self, open_browser):
        login_p = open_browser
        mcp_p = ManagerCustomersPage(login_p.driver)
        login_p.click_bank_manager_btn()
        mcp_p.click_bank_manager_list_customers()
        mcp_p.type_search_customer('Granger')
        hermione_account_numbers = ['1001', '1002', '1003']
        assert mcp_p.get_selected_first_name() == 'Hermoine', 'First name nao confere'
        assert mcp_p.get_selected_last_name() == 'Granger', 'Last name nao confere'
        assert mcp_p.get_selected_postal_code() == 'E859AB', 'Postal code nao confere'
        assert mcp_p.get_selected_account_list() == hermione_account_numbers, "Account numbers nao conferem"
        assert mcp_p.has_delete_button_displayed(), "Botao delete nao encontrado"

    # CT-003.2 - Busca de usuario aleatorio na consulta do administrador
    def test_random_user_properties(self, select_random_user):
        login_p, full_name = select_random_user
        first_name, last_name = full_name.split()
        mcp_p = ManagerCustomersPage(login_p.driver)
        login_p.click_bank_manager_btn()
        mcp_p.click_bank_manager_list_customers()
        mcp_p.type_search_customer(first_name)
        assert mcp_p.get_selected_first_name() == first_name, 'First name nao confere'
        assert mcp_p.get_selected_last_name() == last_name, 'Last name nao confere'
        assert mcp_p.has_delete_button_displayed(), "Botao delete nao encontrado"
