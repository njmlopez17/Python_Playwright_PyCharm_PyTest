# == import and install files and libraries==
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    # Note that for the XPath, Relative path is used because of its flexibility vs Absolute path

    # >> Test case 01 - use the attribute - '//tagname[@name="value"]'
    print('Test case 01 START!')
    # open the browser page...
    page.goto('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    print('browser page title is ' + '"' + page.title() +'"...')
    # using the attribute of the Username text box...
    username_xpath = page.wait_for_selector('//input[@name="username"]')
    username_xpath.type('Admin')
    print('typed the Username in the text box...')
    # using the attribute of the Password text box...
    password_xpath = page.wait_for_selector('//input[@placeholder="Password"]')
    password_xpath.type('admin123')
    print('typed the Password in the text box...')
    # using the attribute of the login button...
    page.wait_for_timeout(5000)
    buttonSubmit_xpath = page.wait_for_selector('//button[@type="submit"]')
    buttonSubmit_xpath.click()
    print('clicked the login button...')
    # other actions...
    page.wait_for_timeout(5000)
    print('Test case 01 >> PASSED!')
    # browser.close()

    # >> Test case 02 - use the visible text attribute - '//tagname[text()="text"]'
    print('Test case 02 START!')
    # open the browser page...
    page = browser.new_page()
    page.goto('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    print('browser page title is ' + '"' + page.title() + '"...')
    # using the attribute of the element under test...
    page.wait_for_timeout(5000)
    page.wait_for_selector('//p[text()="Forgot your password? "]').click()
    print('clicked the "Forgot your password?" link...')
    # other actions...
    page.wait_for_timeout(5000)
    print('Test case 02 >> PASSED!')
    # browser.close()

    # >> Test case 03 - use contains attribute (commonly used xpath locator method) - '//tagname[contains(@attribute, "value")]'
    print('Test case 03 START!')
    # open the browser page...
    page = browser.new_page()
    page.goto('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    print('browser page title is ' + '"' + page.title() + '"...')
    # using the attribute of the element under test...
    contain_xpath = page.wait_for_selector('//input[contains(@placeholder,"User")]')
    contain_xpath.type('JOHN')
    print('typed the Username in the text box...')
    # other actions...
    page.wait_for_timeout(5000)
    print('Test case 03 >> PASSED!')
    # browser.close()

    # >> Test case 04 - use contains attribute for starts-with/ends-with (used for dynamic or array of data with common value) - //tagname[starts-with(@attribute, "value")]
    print('Test case 04 START!')
    # open the browser page...
    page = browser.new_page()
    page.goto('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    print('browser page title is ' + '"' + page.title() + '"...')
    # using the attribute of the element under test...
    starts_with_xpath = page.wait_for_selector('//input[starts-with(@placeholder,"User")]')
    starts_with_xpath.type('JOHN')
    print('typed the Username in the text box...')
    # other actions...
    page.wait_for_timeout(5000)
    print('Test case 04 >> PASSED!')
    browser.close()