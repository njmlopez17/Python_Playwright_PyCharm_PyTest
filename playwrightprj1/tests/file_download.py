# == import and install files and libraries==
from playwright.sync_api import sync_playwright

# == methods==
def download_handle(download):
    location_file = './files/test.zip'
    download.save_as(location_file)

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # ======START OF TEST======

    # >> Test case 01 - file download
    print('Test case 01 START!')
    page.goto('https://demo.imacros.net/Automate/Downloads')
    print('browser page title is ' + '"' + page.title() + '"...')
    # to download the file
    page.on('download', download_handle)
    page.wait_for_selector('//a[@href="/Content/Download.zip"]').click()
    print('File downloaded.')
    # other actions...
    page.wait_for_timeout(5000)
    print('Test case 01 >> PASSED!')
    browser.close()