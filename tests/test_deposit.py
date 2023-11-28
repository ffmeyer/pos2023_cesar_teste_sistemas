from time import sleep

from pages.CustomerAccountPage import CustomerAccountPage
from pages.CustomerTransactionPage import CustomerTransactionPage


class test_deposit:

    def test_deposit(self, login_harry, open_browser):
        cap_p = CustomerAccountPage(login_harry.driver)
        ctp_p = CustomerTransactionPage(login_harry.driver)
        assert cap_p.read_acc_number() == '1004'
        assert cap_p.read_balance_value() == '0'
        cap_p.make_a_deposit('2000')
        assert cap_p.read_message() == 'Deposit Successful'
        assert cap_p.read_balance_value() == '2000'
        sleep(1)
        cap_p.click_transactions_option()
        assert ctp_p.read_transactions_info() == ('2000', 'Credit')
