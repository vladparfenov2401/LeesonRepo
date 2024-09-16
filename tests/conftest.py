import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en', help='Language for browser interface')

@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption('language')
    chrome_options = Options()
    chrome_options.add_argument(f'--lang={language}')
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    yield browser
    browser.quit()