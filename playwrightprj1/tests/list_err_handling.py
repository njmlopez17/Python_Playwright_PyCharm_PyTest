# == import and install files and libraries==
from contextlib import nullcontext

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    try:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()  # context handles multiple page, new page handles only single page
        page = context.new_page()

        # ======START OF TEST======

        # >> Test case 01 - PASSED test case
        print('Test case 01 START!')
        # go to browser under test
        page.goto('https://demo.automationtesting.in/Selectable.html')
        # store multiple elements1 using List
        # correct page attribute below
        elements1 = page.query_selector_all('b')
        print('There are a total number of elements1 of >> ' + str(len(elements1)))
        print('Collecting of elements1 started...')
        for i in elements1:
            print(i.text_content())
        print('Display the list of elements1 completed.')
        page.wait_for_timeout(3000)
        # store multiple elements2 using List
        elements2 = page.query_selector_all('a')
        print('There are a total number of elements2 of >> ' + str(len(elements2)))
        print('Collecting of elements2 started...')
        for i in elements2:
            print(i.get_attribute('href'))
        print('Display the list of elements2 completed.')
        page.wait_for_timeout(3000)
        print('Test case 01 >> PASSED!')
    # error handling...
    except Exception as e:
        print(str(e))
        if str(e) != nullcontext:
            print('Test case 01 >> FAILED!')
    finally:
        print('Execute')
    # # close all other opened pages
    # browser.close()
    # print('All opened browser pages are now closed.')

    try:
        # >> Test case 02 - FAILED test case
        print('Test case 02 START!')
        # go to browser under test
        page.goto('https://demo.automationtesting.in/Selectable.html')
        # store multiple elements1 using List
        # incorrect page attribute below (to test the error handling syntax)
        page.query_selector('d//[sf="wrong"]').click()
        # correct page attribute below
        elements1 = page.query_selector_all('b')
        print('There are a total number of elements1 of >> ' + str(len(elements1)))
        print('Collecting of elements1 started...')
        for i in elements1:
            print(i.text_content())
        print('Display the list of elements1 completed.')
        page.wait_for_timeout(3000)
        # store multiple elements2 using List
        elements2 = page.query_selector_all('a')
        print('There are a total number of elements2 of >> ' + str(len(elements2)))
        print('Collecting of elements2 started...')
        for i in elements2:
            print(i.get_attribute('href'))
        print('Display the list of elements2 completed.')
        page.wait_for_timeout(3000)
        print('Test case 02 >> PASSED!')
    # error handling...
    except Exception as e:
        print(str(e))
        if str(e) != nullcontext:
            print('Test case 02 >> FAILED!')
    finally:
        print('Execute')
    # # close all other opened pages
    browser.close()
    print('All opened browser pages are now closed.')

