import pytest

from pages.HeaderPage import HeaderPage
from pages.LoginPage import LoginPage
from pages.ManagerAddCustomerPage import ManagerAddCustomerPage
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
def select_random_user(open_browser):
    pass


@pytest.fixture()
def create_user_500_dollars(open_browser):
    pass
