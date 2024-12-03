# == import and install files and libraries==
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Note that for the XPath, Relative path is used because of its flexibility vs Absolute path

        # >> Test case 01 - use the attribute - '//tagname[@name="value"]'
        print('Test case 01 START!')
        # open the browser page...
        page.goto('https://demo.automationtesting.in/Register.html')
        print('browser page title is ' + '"' + page.title() + '"...')
        # using the attribute of the element under test...
        radio_btn = page.query_selector('//input[@value="Male"]')
        # radio_btn.click() # can also use radio_btn.check(), also, this test test case should fail because radio button is not selected
        print('clicked the radio button...')
        # other actions...
        page.wait_for_timeout(5000)
        if radio_btn.is_checked():
            print('Test case 01 >> PASSED!')
        else:
            print('Test case 01 >> FAILED!')
        # browser.close()

        # >> Test case 02 - use the attribute - '//tagname[@name="value"]'
        print('Test case 02 START!')
        # # using the attribute of the element under test...
        check_box = page.query_selector('//input[@value="Movies"]')
        check_box.check()
        print('checked the check box...')
        # other actions...
        page.wait_for_timeout(5000)
        print('Test case 02 >> PASSED!')
        browser.close()