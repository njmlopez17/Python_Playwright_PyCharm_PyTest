# == import and install files and libraries==
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()  # context handles multiple page, new page handles only single page
    page = context.new_page()

    # ======START OF TEST======

    # >> Test case 01 - use the attribute - "//tagname[contains=(text(), 'value')]"
    print('Test case 01 START!')
    # go to browser under test
    page.goto('https://demo.automationtesting.in/Selectable.html')
    # -----mouse action below...
    # find the page element and hover the mouse
    page.wait_for_selector('//a[contains(text(), "SwitchTo")]').hover()
    page.wait_for_timeout(3000)
    # # single click on a selected element value
    page.wait_for_selector('//a[contains(text(), "Frames")]').click()
    page.wait_for_timeout(3000)
    # # # double-click on a selected element value
    # page.wait_for_selector('//a[contains(text(), "SwitchTo")]').dblclick()
    # # # right-click on a selected element value
    # page.wait_for_selector('//a[contains(text(), "SwitchTo")]').click(button="right")
    # # right-click on a selected element value
    # page.wait_for_selector('//a[contains(text(), "SwitchTo")]').click(modifiers=["Shift"])
    # -----keyboard action below...
    # ie., A-Z, 0-9, F1-F12, special characters, ArrowRight, PageUp, Enter, Control, and so on
    # page.wait_for_selector('//input[@type="text"]').press("A")
    # # close all other opened pages
    browser.close()
    print('All opened browser pages are now closed.')
    print('Test case 01 >> PASSED!')