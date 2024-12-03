# ====== IMPORT FILES AND LIBRARIES ======
import pytest
from playwright.sync_api import sync_playwright

#  ====== METHODS ======

# class run (runs at the start and at the end of the execution)
@pytest.fixture(scope="class")
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
@pytest.mark.usefixtures('browser')
class Test_class:
    # Test case 01
    def test_open_page_a(self, page):
        page.goto('https://www.google.ca/')
        assert page.url == 'https://www.google.ca/'
        print('Test case 01 expected to PASS!')

    # Test case 02
    def test_open_page_b(self, page):
        page.goto('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
        assert page.url == 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'
        print('Test case 02 expected to PASS!')

    # Test case 03
    def test_open_page_c(self, page):
        page.goto('https://demo.automationtesting.in/FileUpload.html')
        assert page.url == 'https://demo.automationtesting.in/FileUpload.html'
        print('Test case 03 expected to PASS!')