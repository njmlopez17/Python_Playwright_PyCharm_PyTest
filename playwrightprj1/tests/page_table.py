# == import and install files and libraries==
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # ======START OF TEST======

    # >> Test case 01 - web page table handling
    print('Test case 01 START!')
    page.goto('https://cosmocode.io/automation-practice-webtable')
    # locate the table from the page
    table = page.wait_for_selector('//table[@id="countries"]')
    print('Table found...')
    # from the table, find the rows
    tr = table.query_selector_all('tr')
    print('This is the table row count >> ' + str(len(tr)))
    # from the table, find the data
    td = table.query_selector_all('td')
    print('This is the table data count >> ' + str(len(td)))
    # find and get the value set for each row in the table
    for row in tr:
        td_cell = row.query_selector_all('td')
        for tv_cell in td_cell:
            print(tv_cell.text_content())
            # find a specific data value from the table
            if tv_cell.text_content() =="Harare":
                print('****** Harare found ******')
    # other actions...
    print('Test case 01 >> PASSED!')
    page.wait_for_timeout(3000)
    browser.close()
    print('All opened browser pages are now closed.')