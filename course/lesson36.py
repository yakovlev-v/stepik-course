import pytest
from selenium import webdriver as app
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as exp_con

text_edit = []
urls = ['https://stepik.org/lesson/236895/step/1',
        'https://stepik.org/lesson/236896/step/1',
        'https://stepik.org/lesson/236897/step/1',
        'https://stepik.org/lesson/236898/step/1',
        'https://stepik.org/lesson/236899/step/1',
        'https://stepik.org/lesson/236903/step/1',
        'https://stepik.org/lesson/236904/step/1',
        'https://stepik.org/lesson/236905/step/1']


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = app.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()
    print(text)


@pytest.mark.parametrize('url', urls)
def test_open_page(browser, url):
    browser.get(url)
    wait_page_load = WebDriverWait(browser, 30)
    answer_field = wait_page_load.until(exp_con.element_to_be_clickable(
        (By.CSS_SELECTOR, ".ember-text-area.ember-view.textarea.string-quiz__textarea")))
    answer_field.send_keys(str(math.log(int(time.time()))))
    button = browser.find_element_by_css_selector('.submit-submission')
    button.click()
    black_field = wait_page_load.until(exp_con.presence_of_element_located((By.CSS_SELECTOR, ".smart-hints__hint")))
    check = black_field.get_attribute("innerHTML")
    assert check == "Correct!", text.append(check + ' ')
