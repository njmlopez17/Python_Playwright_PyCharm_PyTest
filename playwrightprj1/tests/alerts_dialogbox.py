# == import and install files and libraries==
from playwright.sync_api import sync_playwright

# == variables==
text_alert = []

# == methods==
def handle_dialog(dialog):
    message = dialog.message
    text_alert.append(message)
    if "Please enter your name" in text_alert:
        dialog.accept('UNCLE SAM!')
    else:
        dialog.dismiss() # or dialog.accept()

with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # ======START OF TEST======

# one way of coding the test case is below (relying on a method)...
        # >> Test case 01 - use the attribute - '//tagname[@name="value"]/element type'
        # Dialog box Ok/Cancel
        print('Test case 01 START!')
        # open the browser page...
        page.goto('https://demo.automationtesting.in/Alerts.html')
        print('browser page title is ' + '"' + page.title() + '"...')
        # using the attribute of the element under test...
        page.query_selector('//a[@href="#CancelTab"]').click()
        print('clicked the Ok & Cancel button...')
        page.wait_for_timeout(3000)
        # control and catch the dialog box before pressing the next button
        page.on("dialog", handle_dialog)
        page.query_selector('//div[@id="CancelTab"]/button').click()
        # display the message from the popup dialog box
        print('This is the message from the popup box >> ' + text_alert[0])
        # other actions...
        page.wait_for_timeout(5000)
        print('Test case 01 >> PASSED!')
        # browser.close()

# another way of coding the test case is below (not relying on a method)...
        # # >> Test case 01 - use the attribute - '//tagname[@name="value"]/element type'
        # print('Test case 01 START!')
        # # open the browser page...
        # page.goto('https://demo.automationtesting.in/Alerts.html')
        # print('browser page title is ' + '"' + page.title() + '"...')
        # # using the attribute of the element under test...
        # page.query_selector('//a[@href="#CancelTab"]').click()
        # print('clicked the Ok & Cancel button...')
        # page.wait_for_timeout(3000)
        # # control and catch the dialog box before pressing the next button
        # page.on("dialog", lambda dialog: dialog.dismiss())  # dialog.accept() for OK, dialog.dismiss() for CANCEL; without this line the popup window will be hardly visible
        # # display the message from the popup dialog box
        # page.on("dialog", lambda dialog: print('This is the message from the popup box >> ' + dialog.message))
        # page.query_selector('//div[@id="CancelTab"]/button').click()
        # # other actions...
        # page.wait_for_timeout(5000)
        # print('Test case 01 >> PASSED!')
        # browser.close()

        # >> Test case 02 - use the attribute - '//tagname[@name="value"]/element type'
        # Dialog box with Textbox
        print('Test case 02 START!')
        # open the browser page...
        page.goto('https://demo.automationtesting.in/Alerts.html')
        print('browser page title is ' + '"' + page.title() + '"...')
        # using the attribute of the element under test...
        page.query_selector('//a[@href="#Textbox"]').click()
        print('clicked the Alerts with Textbox button...')
        page.wait_for_timeout(3000)
        # control and catch the dialog box before pressing the next button
        page.on("dialog", handle_dialog)
        page.query_selector('//div[@id="Textbox"]/button').click()
        # display the message from the popup dialog box
        print('This is the message from the popup box >> ' + text_alert[1])
        # other actions...
        page.wait_for_timeout(5000)
        print('Test case 02 >> PASSED!')
        browser.close()