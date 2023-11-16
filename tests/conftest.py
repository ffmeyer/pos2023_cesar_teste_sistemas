import pytest

from pages.CustomerLoginPage import CustomerLoginPage
from pages.HeaderPage import HeaderPage
from pages.LoginPage import LoginPage
from pages.ManagerAddCustomerPage import ManagerAddCustomerPage
from pages.ManagerOpenAccountPage import ManagerOpenAccountPage
from utils.UserGenerator import User



@pytest.fixture()
def open_browser(request):
    login_p = LoginPage(browser='chrome')
    login_p.open_page()
    yield login_p
    login_p.close()


@pytest.fixture()
def create_user(open_browser):
    login_p = open_browser
    login_p.click_bank_manager_btn()
    mac_p = ManagerAddCustomerPage(open_browser.driver)
    header_p = HeaderPage(open_browser.driver)
    mac_p.click_bank_manager_add_customer()
    a_user = User()
    user = a_user.generate_user()
    mac_p.create_user(first_name=user.first_name, last_name=user.last_name, postal_code=user.postal_code)
    mac_p.close_alert()
    header_p.click_home_btn()

    yield login_p, user


@pytest.fixture()
def create_user_account_association(create_user):
    login_p, user = create_user
    login_p.click_bank_manager_btn()
    moap_p = ManagerOpenAccountPage(login_p.driver)
    header_p = HeaderPage(login_p.driver)
    moap_p.click_bank_manager_open_account()
    moap_p.create_new_account_in_dollar(user.full_name)
    account_id = moap_p.get_account_number()
    moap_p.close_alert()
    header_p.click_home_btn()
    yield login_p, user, account_id


@pytest.fixture()
def select_random_user(open_browser):
    login_p = open_browser
    login_p.click_customer_btn()
    clp_p = CustomerLoginPage(login_p.driver)
    header_p = HeaderPage(login_p.driver)
    full_name = clp_p.select_random_available_user()
    header_p.click_home_btn()
    yield login_p, full_name

@pytest.fixture()
def create_user_500_dollars(open_browser):
    pass
