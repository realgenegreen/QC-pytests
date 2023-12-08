import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager

@pytest.fixture(scope='session')
def driver():
    '''firefox configs'''
    firefox_options = Options()
    firefox_options.add_argument('--no sandbox')
    ## firefox_options.add_argument('start-maximazed')
    firefox_options.add_argument('--disable-infobars')
    firefox_options.add_argument('--disable-extensions')
    ##firefox_options.add_argument('--headless')

    service = Service(GeckoDriverManager().install())

    driver = webdriver.Firefox(service=service, options=firefox_options)

    yield driver
    driver.quit()