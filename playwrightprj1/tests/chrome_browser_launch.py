# == import and install files and libraries==
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.google.ca")
    # other actions...
    print(page.title())
    print('Success!')
    page.wait_for_timeout(3000)
    browser.close()



