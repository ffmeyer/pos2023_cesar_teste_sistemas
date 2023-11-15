from pages.ManagerOpenAccountPage import ManagerOpenAccountPage


class Test_user_account_association:
    def test_user_account_association(self, create_user):
        login_p, user = create_user
        login_p.click_bank_manager_btn()
        moap_p = ManagerOpenAccountPage(login_p.driver)
        moap_p.click_bank_manager_open_account()
        moap_p.create_new_account_in_dollar(user.full_name)
        assert moap_p.has_message_sucessfull_association(), 'Erro ao associar usuario a uma nova conta'
