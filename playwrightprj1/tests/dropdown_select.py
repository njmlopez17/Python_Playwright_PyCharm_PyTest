# == import and install files and libraries==
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    # >> Test case 01 - use the attribute - '//tagname[@name="value"]'
    print('Test case 01 START!')
    # open the browser page...
    page.goto('https://demo.automationtesting.in/Register.html')
    print('browser page title is ' + '"' + page.title() +'"...')
    # using the attribute of the element under test...
    select_dropdown1 = page.query_selector("//select[@id='Skills']")
    # select the option
    select_dropdown1.select_option(label='Adobe Photoshop')
    print('Dropdown value selected...')
    # other actions...
    page.wait_for_timeout(10000)
    print('Test case 01 >> PASSED!')


    # >> Test case 02 - use the attribute - '//tagname[@name='value']", @name='value')'
    print('Test case 02 START!')
    # open the browser page...
    page.goto('https://demo.automationtesting.in/Register.html')
    print('browser page title is ' + '"' + page.title() +'"...')
    # using the attribute of the element under test...
    select_dropdown2 = page.select_option("//select[@id='yearbox']", label='1918')
    print('Dropdown value selected...')
    # other actions...
    page.wait_for_timeout(10000)
    print('Test case 02 >> PASSED!')
    browser.close()