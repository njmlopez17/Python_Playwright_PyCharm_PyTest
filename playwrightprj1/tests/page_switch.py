# == import and install files and libraries==
from playwright.sync_api import sync_playwright

# == variables==

# == methods==

with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context() # context handles multiple page, new page handles only single page
        page = context.new_page()

        # ======START OF TEST======

        # >> Test case 01 - use the attribute - "//tagname[contains=(text(), 'value')]"
        # Dialog box Ok/Cancel
        print('Test case 01 START!')
        # open the browser page...
        page.goto('https://demo.automationtesting.in/Windows.html')
        # using the attribute of the element under test...
        page.wait_for_selector("//button[contains(text(), '    click   ')]").click()
        page.wait_for_timeout(3000)
        # this is to find/collect (and a list is returned) of all the pages under test
        total_pages = context.pages
        print('Total opened browser page (see below urls) >> ' + str(len(total_pages)))
        for i in total_pages:
            print(i)
        print('parent page title is ' + '"' + page.title() + '"...')
        # this is how to store new pages in a variable
        new_page = total_pages[1]
        # this brings the child page in focus or active mode
        new_page.bring_to_front()
        print('child page title is ' + '"' + new_page.title() + '"...')
        # other actions...
        new_page.wait_for_timeout(3000)
        # switch back to child page, this closes only the child page
        new_page.close()
        print('All opened child pages are now closed.')
        # this brings the main page back in focus or active mode
        page.bring_to_front()
        page.wait_for_timeout(3000)
        # close all other opened pages
        browser.close()
        print('All opened browser pages are now closed.')
        print('Test case 01 >> PASSED!')

