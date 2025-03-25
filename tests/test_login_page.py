from pytest import fixture
from playwright.sync_api import Page, expect
from page_objects.login_page import LoginPage

@fixture
#Fixtures can be used to set up tests, in this case initialising the Landing Page
#Otherwise would have had to pass it in everytime
def login_page(page: Page):
    login_page = LoginPage(page)
    login_page.navigate()
    return login_page

def test_page_title(login_page):
    # Then
    assert login_page.pageTitle() == 'Swag Labs'

def test_invalid_login(login_page):
    #Given
    login_page.clickLoginButton()

    # Then
    error_message = login_page.getLogginErrorMessage()
    assert error_message == 'Epic sadface: Username is required'

def test_valid_login(login_page):
    # Using -> None: to indicate void i.e. this method returns nothing
    # When
    login_page.setUsername("standard_user")
    login_page.setPassword("secret_sauce")
    login_page.clickLoginButton()

    # Then
    expect(login_page.getInventoryContainer()).to_be_visible()