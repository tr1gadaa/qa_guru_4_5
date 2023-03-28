import pytest
from selene import browser


@pytest.fixture
def browser_settings():
    browser.config.browser_name = 'firefox'
    browser.config.hold_browser_open = True
    browser.config.window_width = 720
    browser.config.window_height = 960

