# == import and install files and libraries==
from playwright.sync_api import sync_playwright

# == methods==

with sync_playwright()as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context(record_video_dir='./files/videos')
    page = context.new_page()

    # >> Test case 01 - page video recording and screenshot
    print('Test case 01 START!')
    page.goto('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    print('browser page title is ' + '"' + page.title() + '"...')
    # fill the login fields
    page.wait_for_timeout(5000)
    page.wait_for_selector('//input[@name="username"]').fill('Admin')
    page.wait_for_selector('//input[@type="password"]').fill('admin123')
    # take a screenshot before logging in
    page.screenshot(path='./files/screenshot.png')
    print('Screenshot captured.')
    page.wait_for_timeout(5000)
    # login into the page
    page.query_selector('//button[@type="submit"]').click()
    # other actions...
    page.wait_for_timeout(5000)
    print('Video captured.')
    print('Test case 01 >> PASSED!')
    browser.close()