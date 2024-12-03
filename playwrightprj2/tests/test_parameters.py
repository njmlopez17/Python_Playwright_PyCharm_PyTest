# ====== IMPORT FILES AND LIBRARIES ======
import pytest
from playwright.sync_api import sync_playwright

#  ====== METHODS ======
@pytest.fixture(scope='module')
def browser_handle():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()

@pytest.fixture(scope='function')
def page_handle(browser_handle):
    page = browser_handle.new_page()
    yield page
    page.close()

#  ====== START OF TESTING ======

# Test case 01
@pytest.mark.parametrize('invalid_username, invalid_password', [('wrong1','wrong1'), ('wrong2', 'wrong2')])
def test_invalid_login(page_handle, invalid_username, invalid_password):
    page_handle.goto('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    page_handle.wait_for_selector('//input[@name="username"]').type(invalid_username)
    page_handle.wait_for_selector('//input[@type="password"]').type(invalid_password)
    page_handle.wait_for_timeout(5000)
    page_handle.wait_for_selector('//button[@type="submit"]').click()
    page_handle.wait_for_timeout(5000)
    error_msg = page_handle.wait_for_selector('//div[@role="alert"]//p').text_content()
    assert 'Invalid credentials' == error_msg
    print('Test case expected to PASS!')



