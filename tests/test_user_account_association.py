from pages.ManagerOpenAccountPage import ManagerOpenAccountPage


class Test_user_account_association:
    # CT-002 - Associação entre usuario e conta
    def test_user_account_association(self, create_user):
        login_p, user = create_user
        login_p.click_bank_manager_btn()
        moap_p = ManagerOpenAccountPage(login_p.driver)
        moap_p.click_bank_manager_open_account()
        moap_p.create_new_account_in_dollar(user.full_name)
        assert moap_p.has_message_sucessfull_association(), 'Erro ao associar usuario a uma nova conta'
        assert moap_p.get_account_number() is not None
        moap_p.close_alert()
