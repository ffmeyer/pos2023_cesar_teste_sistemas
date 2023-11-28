from pages.HeaderPage import HeaderPage
from pages.CustomerAccountPage import CustomerAccountPage


class Test_withdraw:

    def test_withdraw(self, login_harry, open_browser):
        cap_p = CustomerAccountPage(login_harry.driver)
        header = HeaderPage(login_harry.driver)
        assert cap_p.read_balance_value() == '0'
        cap_p.make_a_deposit('20')
        assert cap_p.read_message() == 'Deposit Successful'
        cap_p.make_a_withdrawl('10')
        assert cap_p.read_message() == 'Transaction successful'
        assert cap_p.read_balance_value() == '10'


