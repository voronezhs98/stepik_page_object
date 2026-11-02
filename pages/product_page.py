
from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_product_to_basket(self):
        button = self.browser.find_element(
            *ProductPageLocators.ADD_TO_BASKET_BUTTON
        )
        button.click()
        self.solve_quiz_and_get_code()

    def should_be_product_added_to_basket(self):
        product_name = self.browser.find_element(
            *ProductPageLocators.PRODUCT_NAME
        ).text

        added_product_name = self.browser.find_element(
            *ProductPageLocators.ADDED_PRODUCT_NAME
        ).text

        assert product_name == added_product_name, (
            "Product name in basket message does not match"
        )

    def should_be_correct_basket_total(self):
        product_price = self.browser.find_element(
            *ProductPageLocators.PRODUCT_PRICE
        ).text

        basket_total = self.browser.find_element(
            *ProductPageLocators.BASKET_TOTAL
        ).text

        assert product_price == basket_total, (
            "Basket total does not match product price"
        )

    def should_not_be_success_message(self):
        assert self.is_not_element_present(
            *ProductPageLocators.ADDED_PRODUCT_NAME
        ), "Success message is presented, but should not be"

    def should_be_disappeared_success_message(self):
        assert self.is_disappeared(
            *ProductPageLocators.ADDED_PRODUCT_NAME
        ), "Success message did not disappear"
