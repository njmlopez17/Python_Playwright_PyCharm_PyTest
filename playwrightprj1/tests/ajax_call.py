# == import and install files and libraries==
from playwright.sync_api import sync_playwright

# == methods==
def handle_ajax(response):
    if 'https://www.plus2net.com/php_tutorial/dd-ajax.php?' in response.url:
        status = response.status
        data = response.text()
        print(f'status:{status}, data:{data}')

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # ======START OF TEST======

    # >> Test case 01 - AJAX handling
    print('Test case 01 START!')
    page.goto('https://www.plus2net.com/php_tutorial/ajax_drop_down_list-demo.php')
    print('browser page title is ' + '"' + page.title() +'"...')
    select = page.wait_for_selector('//select[@id="s1"]')
    # setup a "listener" to display the list values of selected category
    page.on('response', lambda response : handle_ajax(response))
    select.select_option('3')
    print('Dropdown value selected...')
    # other actions...
    print('Test case 01 >> PASSED!')
    page.wait_for_timeout(5000)
    browser.close()
