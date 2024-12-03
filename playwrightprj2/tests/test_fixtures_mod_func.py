# ====== IMPORT FILES AND LIBRARIES ======
import pytest
from playwright.sync_api import sync_playwright

#  ====== METHODS ======

# module run (runs at the start and at the end of the execution)
@pytest.fixture(scope="module")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()

# function run (runs each time with each of the test case execution)
@pytest.fixture(scope="function")
def page(browser):
    page = browser.new_page()
    yield page
    page.close()

#  ====== START OF TESTING ======

# Test case 01
def test_goto_page_a(page):
    page.goto('https://www.google.ca/')
    assert page.title() == 'Google'
    print('Test case 01 expected to PASS!')

# Test case 02
def test_goto_page_b(page):
    page.goto('https://www.bestbuy.ca/en-ca')
    print('Test case 02 expected to FAIL!')
    assert page.title() == 'page test fail'
