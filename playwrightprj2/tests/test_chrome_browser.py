# ====== IMPORT FILES AND LIBRARIES ======
from playwright.sync_api import sync_playwright

# Test case 01
def test_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
        assert page.title() == 'OrangeHRM'
        print(page.title())
        page.wait_for_timeout(5000)


    # # ====== IMPORT FILES AND LIBRARIES ======
    # from playwright.sync_api import Playwright
    #
    # # Test case 01
    # def test_login(playwright: Playwright) -> None:
    #     browser = playwright.chromium.launch(headless=False)
    #     context = browser.new_context()
    #     page = context.new_page()
    #     page.goto('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    #     assert page.title() == 'OrangeHRM'
    #     print(page.title())
    #     page.wait_for_timeout(5000)
