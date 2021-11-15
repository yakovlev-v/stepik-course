# content of test_expectation.py
import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


languages = [
    ("ru", "русский"),
    ("de", "немецкий"),
    ("ua", "украинский"),
    ("en-gb", "английский")
]


# @pytest.mark.parametrize("code, lang", languages)
@pytest.mark.parametrize("code", ['русский', "английский"])
def test_guest_should_see_login_link(browser, code):
    f'http://selenium1py.pythonanywhere.com/{code}/'
    print(f"Проверяемый язык {code}")
