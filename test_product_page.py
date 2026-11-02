
import pytest

from pages.product_page import ProductPage


@pytest.mark.parametrize(
    "link",
    [
        pytest.param(
            f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{i}",
            marks=pytest.mark.xfail(
                reason="Product name mismatch"
            ) if i == 7 else ()
        )
        for i in range(10)
    ]
)
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()

    page.add_product_to_basket()

    page.should_be_product_added_to_basket()
    page.should_be_correct_basket_total()
