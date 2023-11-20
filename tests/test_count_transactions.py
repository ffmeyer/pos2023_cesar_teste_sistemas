from time import sleep

from pages.CustomerAccountPage import CustomerAccountPage
from pages.CustomerTransactionPage import CustomerTransactionPage

class Test_count_transactions:

    def test_count_transactions(self, login_harry, open_browser):
        cap_p = CustomerAccountPage(login_harry.driver)
        ctp_p = CustomerTransactionPage(login_harry.driver)
        assert cap_p.read_balance_value() == '0'
        cap_p.make_a_deposit('10')
        assert cap_p.read_message() == 'Deposit Successful'
        assert cap_p.read_balance_value() == '10'
        sleep(1)
        cap_p.make_a_deposit('5')
        assert cap_p.read_message() == 'Deposit Successful'
        assert cap_p.read_balance_value() == '15'
        sleep(1)
        cap_p.make_a_withdrawl('5')
        assert cap_p.read_message() == 'Transaction successful'
        assert cap_p.read_balance_value() == '10'
        sleep(1)
        cap_p.click_transactions_option()
        assert ctp_p.read_transactions_info() == ('10', 'Credit', '5', 'Credit', '5', 'Debit')
