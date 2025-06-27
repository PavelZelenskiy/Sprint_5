
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from creds_randomizer import *
from locators import Locators
from urls import *
from data import Creds

class TestTransitionsFromPersonalAccount:

    def test_transition_from_personal_acc_by_logo(self, driver: WebDriver):

        driver.get(LOGIN_URL)
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.LOG_LOGIN_BUTTON))

        driver.find_element(*Locators.LOG_EMAIL_INPUT).send_keys(Creds.email)
        driver.find_element(*Locators.LOG_PASSWORD_INPUT).send_keys(Creds.password)
        driver.find_element(*Locators.LOG_LOGIN_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.url_changes(driver.current_url))

        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.url_changes(driver.current_url))

        driver.find_element(*Locators.LOGO_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.url_changes(PERSONAL_ACCOUNT_PROFILE_URL))

        assert driver.current_url == BASE_URL


    def test_transition_from_personal_acc_by_constructor_button(self, driver: WebDriver):

        driver.get(LOGIN_URL)
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.LOG_LOGIN_BUTTON))

        driver.find_element(*Locators.LOG_EMAIL_INPUT).send_keys(Creds.email)
        driver.find_element(*Locators.LOG_PASSWORD_INPUT).send_keys(Creds.password)
        driver.find_element(*Locators.LOG_LOGIN_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.url_changes(driver.current_url))

        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.url_changes(driver.current_url))

        driver.find_element(*Locators.CONSTRUCTOR_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.url_changes(PERSONAL_ACCOUNT_PROFILE_URL))
        
        assert driver.current_url == BASE_URL

        

