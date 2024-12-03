# == import and install files and libraries==
from playwright.sync_api import sync_playwright

# == variables==

# == methods==

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()  # context handles multiple page, new page handles only single page
    page = context.new_page()

    # ======START OF TEST======

    # >> Test case 01 - use the attribute - "//tagname[contains=(text(), 'value')]"
    # Dialog box Ok/Cancel
    print('Test case 01 START!')
    page.goto('https://demo.automationtesting.in/Register.html')
    # get and display all the cookies
    my_cookies = page.context.cookies()
    print(my_cookies)
    # clear all the cookies
    page.context.clear_cookies()
    print('All cookies cleared.')

    # syntax in insert cookies
    # new_cookies = {
    #     'name': 'test_sample',
    #     'value': 'asdflksadhjflsoadfjsdlfjsdklfsd'
    # }
    # pass the new cookies into the target page
    # page.context.add_cookies([new_cookies])

    #taking page screenshot
    page.screenshot(path='files/test.png', full_page=False)
    print('Screenshots printed.')
    # close all other opened pages
    browser.close()
    print('All opened browser pages are now closed.')
    print('Test case 01 >> PASSED!')
