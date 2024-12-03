# == import and install files and libraries==
from playwright.sync_api import sync_playwright

with sync_playwright() as play:
    browser = play.chromium.launch(headless=False)
    page = browser.new_page()

    # css Selector - id + "#", class = ., attribute = tagname[attribute = "value"]

    # >> Test case 01 - using the id + "#" locator...
    print('Test case 01 START!')
    # open the browser page...
    page.goto('https://demo.automationtesting.in')
    print('browser page title is ' + '"' + page.title() +'"...')
    # using the attribute of the email text box...
    emailtxtbox = page.wait_for_selector('#email')
    emailtxtbox.type('test_email@yahoo.com')
    # other actions...
    print('typed the email in the text box...')
    page.wait_for_timeout(5000)
    # using the attribute of the login button...
    buttonLogin1 = page.wait_for_selector('#enterimg')
    buttonLogin1.click()
    print('clicked the login button...')
    page.wait_for_timeout(5000)
    print('Test case 01 >> PASSED!')
    # browser.close()

    # >> Test case 02 - using the attribute 'tagname[attribute = "value"]' locator...
    print('Test case 02 START!')
    # open the browser page...
    page.goto('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    print('browser page title is ' + '"' + page.title() +'"...')
    # using the attribute of the Username text box...
    username = page.wait_for_selector('input[name="username"]')
    username.type('Admin')
    print('typed the Username in the text box...')
    # using the attribute of the Password text box...
    password = page.wait_for_selector('input[name="password"]')
    password.type('admin123')
    print('typed the Password in the text box...')
    # using the attribute of the login button...
    page.wait_for_timeout(5000)
    buttonLogin2 = page.wait_for_selector('button[type="submit"]')
    buttonLogin2.click()
    print('clicked the login button...')
    # other actions...
    page.wait_for_timeout(5000)
    print('Test case 02 >> PASSED!')
    browser.close()
