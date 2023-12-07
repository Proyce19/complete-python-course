from playwright.sync_api import Playwright, sync_playwright, expect, Page


def test_run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.scalefocus.com/")
    page.get_by_role("link", name="Industries").click()
    page.get_by_role("link", name="About", exact=True).click()
    page.get_by_label("Desktop Navigation").get_by_role("link", name="Careers").click()
    page.get_by_role("heading", name="Our Customers").click()
    page.get_by_role("heading", name="Our Customers").dblclick()

    # ---------------------
    context.close()
    browser.close()



