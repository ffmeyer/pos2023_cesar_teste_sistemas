from time import sleep

from pages.CustomerAccountPage import CustomerAccountPage
from pages.CustomerTransactionPage import CustomerTransactionPage


class Test_deposit_different_accounts:

    def test_deposit_different_accounts(self, login_harry, open_browser):
        cap_p = CustomerAccountPage(login_harry.driver)
        ctp_p = CustomerTransactionPage(login_harry.driver)
        assert cap_p.read_acc_number() == '1004'
        assert cap_p.read_balance_value() == '0'
        cap_p.make_a_deposit('40')
        assert cap_p.read_message() == 'Deposit Successful'
        assert cap_p.read_balance_value() == '40'
        sleep(1)
        cap_p.click_transactions_option()
        assert ctp_p.read_transactions_info() == ('40', 'Credit')
        ctp_p.click_back()
        cap_p.change_account('1005')
        assert cap_p.read_acc_number() == '1005'
        assert cap_p.read_balance_value() == '0'
        cap_p.make_a_deposit('20')
        assert cap_p.read_message() == 'Deposit Successful'
        assert cap_p.read_balance_value() == '20'
        sleep(1)
        cap_p.click_transactions_option()
        assert ctp_p.read_transactions_info() == ('20', 'Credit')
        ctp_p.click_back()
        cap_p.change_account('1004')
        assert cap_p.read_acc_number() == '1004'
        assert cap_p.read_balance_value() == '40'
        cap_p.click_transactions_option()
        assert ctp_p.read_transactions_info() == ('40', 'Credit')

