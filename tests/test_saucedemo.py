from playwright.sync_api import Page


def test_page_title(page: Page):
    page.goto("https://www.saucedemo.com")
    assert page.title() == 'Swag Labs'

def test_login_error(page: Page):
    page.goto("https://www.saucedemo.com/inventory.html")
    error_message = page.inner_text('h3')
    assert error_message == 'Epic sadface: You can only access \'/inventory.html\' when you are logged in.'