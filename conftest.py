import pytest
from selene import browser


@pytest.fixture(scope="session")
def open_google():
    browser.config.window_height = 1920
    browser.config.window_width = 1080
    browser.open('https://google.com')
    yield
    browser.quit()

