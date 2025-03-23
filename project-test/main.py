# main.py

from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Launch in headless=False to see the browser
        page = browser.new_page()
        page.goto('https://example.com')
        page.screenshot(path='../screenshots/example.png')  # Save a screenshot
        print('Screenshot saved as example.png')
        browser.close()

if __name__ == "__main__":
    run()
