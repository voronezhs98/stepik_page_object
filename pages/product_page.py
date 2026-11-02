
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait

from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def click_add_to_basket_button(self):
        button = self.browser.find_element(
            *ProductPageLocators.ADD_TO_BASKET_BUTTON
        )
        button.click()

    def add_product_to_basket(self, solve_quiz=False):
        self.click_add_to_basket_button()

        if solve_quiz:
            self.solve_quiz_and_get_code()

    def get_element_text(self, locator, timeout=10):
        def read_text(browser):
            element = browser.find_element(*locator)
            return element.text

        return WebDriverWait(
            self.browser,
            timeout,
            ignored_exceptions=(StaleElementReferenceException,)
        ).until(read_text)

    def should_be_product_added_to_basket(self):
        product_name = self.get_element_text(
            ProductPageLocators.PRODUCT_NAME
        )

        added_product_name = self.get_element_text(
            ProductPageLocators.ADDED_PRODUCT_NAME
        )

        assert product_name == added_product_name, \
            "Product name in basket message does not match"

    def should_be_correct_basket_total(self):
        product_price = self.get_element_text(
            ProductPageLocators.PRODUCT_PRICE
        )

        basket_total = self.get_element_text(
            ProductPageLocators.BASKET_TOTAL
        )

        assert product_price == basket_total, \
            "Basket total does not match product price"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(
            *ProductPageLocators.ADDED_PRODUCT_NAME
        ), "Success message is presented, but should not be"

    def should_be_disappeared_success_message(self):
        assert self.is_disappeared(
            *ProductPageLocators.ADDED_PRODUCT_NAME
        ), "Success message did not disappear"
