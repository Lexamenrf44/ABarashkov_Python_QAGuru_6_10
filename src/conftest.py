import pytest
import src.tests

from selene import browser
from selene.support.shared import config
from selenium import webdriver
from pathlib import Path

browser.config.driver_options = webdriver.ChromeOptions()
browser.config.driver_options.binary_location = (
    '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
)


def path(file_name):
    return str(Path(src.tests.__file__).parent.joinpath(f'resources/{file_name}').absolute())


@pytest.fixture(scope='function', autouse=True)
def setup_browser():
    config.timeout = 10
    config.window_width = 1680
    config.window_height = 1050
    config.base_url = 'https://demoqa.com'

    yield

    browser.quit()
