from playwright.async_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page

    def navigate(self):
        self.page.goto("https://www.saucedemo.com")

    def pageTitle(self):
        return self.page.title()

    def clickLoginButton(self):
        self.page.locator("[data-test=\"login-button\"]").click()

    def getLogginErrorMessage(self):
        return self.page.inner_text('h3')

    def setUsername(self, username):
        self.page.locator("[data-test=\"username\"]").fill(username)

    def setPassword(self, password):
        self.page.locator("[data-test=\"password\"]").fill(password)

    def getInventoryContainer(self):
        return self.page.locator("[data-test=\"inventory-container\"]")
