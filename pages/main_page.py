
from selenium.webdriver.common.by import By
from .base_page import BasePage


class MainPage(BasePage):
    def should_be_login_link(self):
        self.browser.find_element(
            By.CSS_SELECTOR, "#login_link_invalid"
        )
