
from pages.CustomerAccountPage import CustomerAccountPage
from pages.HeaderPage import HeaderPage


class Test_withdraw_bigger_than_balance:

    def test_withdraw_bigger_than_balance(self, login_harry, open_browser):
        cap_p = CustomerAccountPage(login_harry.driver)
        cap_p.make_a_deposit('20')
        cap_p.make_a_withdrawl('21')
        assert cap_p.has_message_error_withdraw() == True
        assert cap_p.read_balance_value() == '20'


