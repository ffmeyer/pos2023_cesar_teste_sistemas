from pages.HeaderPage import HeaderPage
from pages.CustomerAccountPage import CustomerAccountPage

class Test_withdraw_bigger_than_balance:

    def test_withdraw_bigger_than_balance(self, login_harry, open_browser):
        cap_p = CustomerAccountPage(login_harry.driver)
        header = HeaderPage(login_harry.driver)
        assert cap_p.read_balance_value() == '0'
        cap_p.make_a_deposit('20')
        assert cap_p.read_message() == 'Deposit Successful'
        cap_p.make_a_withdrawl('21')
        assert cap_p.read_message() == 'Transaction Failed. You can not withdraw amount more than the balance.'
        assert cap_p.read_balance_value() == '20'


