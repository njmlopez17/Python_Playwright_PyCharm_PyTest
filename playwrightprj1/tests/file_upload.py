# == import and install files and libraries==
from playwright.sync_api import sync_playwright

with sync_playwright()as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # ======START OF TEST======

    # >> Test case 01 - file upload
    print('Test case 01 START!')
    page.goto('https://demo.automationtesting.in/FileUpload.html')
    print('browser page title is ' + '"' + page.title() + '"...')
    # file to upload
    file_upload = './files/test_file.txt'
    # file upload object/elements
    upload_location = page.wait_for_selector('//input[@id="input-4"]')
    # to upload the file
    upload_location.set_input_files(file_upload)
    print('File uploaded.')
    # other actions...
    page.wait_for_timeout(10000)
    print('Test case 01 >> PASSED!')
    browser.close()
