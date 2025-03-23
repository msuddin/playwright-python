import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.firefox.launch(headless=False)
        page = await browser.new_page()
        await page.goto("https://playwright.dev/python/docs/intro")
        await page.screenshot(path="screenshots/sample_async_test.png")
        print(await page.title())
        await browser.close()

asyncio.run(main())