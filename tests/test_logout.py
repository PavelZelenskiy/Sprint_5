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

class TestLogout:

    def test_logout(self, driver: WebDriver):

        driver.get(LOGIN_URL)
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.LOG_LOGIN_BUTTON))

        driver.find_element(*Locators.LOG_EMAIL_INPUT).send_keys(Creds.email)
        driver.find_element(*Locators.LOG_PASSWORD_INPUT).send_keys(Creds.password)
        driver.find_element(*Locators.LOG_LOGIN_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.PERSONAL_ACCOUNT_BUTTON))

        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.LOGOUT_BUTTON))

        driver.find_element(*Locators.LOGOUT_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.LOG_LOGIN_BUTTON))
        
        assert driver.current_url == LOGIN_URL

        

        

        