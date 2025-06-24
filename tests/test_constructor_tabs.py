from  selenium import webdriver

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from creds_randomizer import *
from locators import Locators
from urls import *
from data import Creds

import time

class TestConstructorTabs:

    def test_constructor_sauces_tab_transition(self):

        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(LOGIN_URL)
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.LOG_LOGIN_BUTTON))

        driver.find_element(*Locators.LOG_EMAIL_INPUT).send_keys(Creds.email)
        driver.find_element(*Locators.LOG_PASSWORD_INPUT).send_keys(Creds.password)
        driver.find_element(*Locators.LOG_LOGIN_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.CONSTRUCTOR_SAUCES_TAB))

        driver.find_element(*Locators.CONSTRUCTOR_SAUCES_TAB).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.CONSTRUCTOR_SAUCES_HEADER))

        time.sleep(1)

        header = driver.find_element(*Locators.CONSTRUCTOR_SAUCES_HEADER)

        assert driver.execute_script("""
        const elem = arguments[0];
        const rect = elem.getBoundingClientRect();
        return rect.top >= 0 && rect.top <= window.innerHeight;""", header), "Элемент не в зоне видимости после скролла"

        driver.quit()

    def test_constructor_fillings_tab_transition(self):

        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(LOGIN_URL)
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.LOG_LOGIN_BUTTON))

        driver.find_element(*Locators.LOG_EMAIL_INPUT).send_keys(Creds.email)
        driver.find_element(*Locators.LOG_PASSWORD_INPUT).send_keys(Creds.password)
        driver.find_element(*Locators.LOG_LOGIN_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.CONSTRUCTOR_FILLINGS_TAB))

        driver.find_element(*Locators.CONSTRUCTOR_FILLINGS_TAB).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.CONSTRUCTOR_FILLINGS_HEADER))

        time.sleep(1)

        header = driver.find_element(*Locators.CONSTRUCTOR_FILLINGS_HEADER)

        assert driver.execute_script("""
        const elem = arguments[0];
        const rect = elem.getBoundingClientRect();
        return rect.top >= 0 && rect.top <= window.innerHeight;""", header), "Элемент не в зоне видимости после скролла"

        driver.quit()

    def test_constructor_buns_tab_transition(self):

        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(LOGIN_URL)
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.LOG_LOGIN_BUTTON))

        driver.find_element(*Locators.LOG_EMAIL_INPUT).send_keys(Creds.email)
        driver.find_element(*Locators.LOG_PASSWORD_INPUT).send_keys(Creds.password)
        driver.find_element(*Locators.LOG_LOGIN_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.CONSTRUCTOR_FILLINGS_TAB))

        driver.find_element(*Locators.CONSTRUCTOR_FILLINGS_TAB).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.CONSTRUCTOR_FILLINGS_HEADER))

        time.sleep(0.5)

        driver.find_element(*Locators.CONSTRUCTOR_BUNS_TAB).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.CONSTRUCTOR_BUNS_HEADER))

        time.sleep(1)

        header = driver.find_element(*Locators.CONSTRUCTOR_BUNS_HEADER)

        assert driver.execute_script("""
        const elem = arguments[0];
        const rect = elem.getBoundingClientRect();
        return rect.top >= 0 && rect.top <= window.innerHeight;""", header), "Элемент не в зоне видимости после скролла"

        driver.quit()