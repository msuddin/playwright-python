from playwright.sync_api import Page, expect


def test_page_title(page: Page):
    # Given
    page.goto("https://www.saucedemo.com")

    # Then
    assert page.title() == 'Swag Labs'

def test_invalid_login(page: Page):
    #Given
    page.goto("https://www.saucedemo.com/inventory.html")

    # Then
    error_message = page.inner_text('h3')
    assert error_message == 'Epic sadface: You can only access \'/inventory.html\' when you are logged in.'

def test_valid_login(page: Page) -> None:
    # Using -> None: to indicate void i.e. this method returns nothing
    # This test was written using generated code from codegen (see Readme under codegen)
    # Given
    page.goto("https://www.saucedemo.com/")

    # When
    page.locator("[data-test=\"username\"]").fill("standard_user")
    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    page.locator("[data-test=\"login-button\"]").click()

    # Then
    expect(page.locator("[data-test=\"inventory-container\"]")).to_be_visible()