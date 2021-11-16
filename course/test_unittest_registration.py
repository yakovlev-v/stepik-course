from selenium import webdriver
import time
import pytest

import unittest


class TestAbs(unittest.TestCase):
    # link = "http://suninjuly.github.io/registration1.html"
    # browser = webdriver.Chrome()
    # browser.get(link)

    def test_first(self):
        # Ваш код, который заполняет обязательные поля
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)
        browser.find_element_by_css_selector('.form-control.first[required]').send_keys("Ivan")
        browser.find_element_by_css_selector('.form-control.second[required]').send_keys("Ivanov")
        browser.find_element_by_css_selector('.form-control.third[required]').send_keys("Ivan@qwe.qwe")
        browser.find_element_by_css_selector("button.btn").click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)
        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        # assert "Congratulations! You have successfully registered!" == welcome_text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Что-то пошло не так")
        browser.quit()

    def test_second(self):
        # Ваш код, который заполняет обязательные поля
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)
        browser.find_element_by_css_selector('.form-control.first[required]').send_keys("Ivan")
        browser.find_element_by_css_selector('.form-control.second[required]').send_keys("Ivanov")
        browser.find_element_by_css_selector('.form-control.third[required]').send_keys("Ivan@qwe.qwe")
        browser.find_element_by_css_selector("button.btn").click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)
        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        # assert "Congratulations! You have successfully registered!" == welcome_text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Что-то пошло не так")
        browser.quit()


if __name__ == "__main__":
    unittest.main()
