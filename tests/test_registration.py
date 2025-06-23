from  selenium import webdriver

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from creds_randomizer import *
from locators import Locators
from urls import *

class TestRegistrationForm:

    def test_registration_successfull(self):
        
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(REG_URL)
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.REG_REGISTRATION_BUTTON))

        name, email, password = valid_creds_randomizer()

        driver.find_element(*Locators.REG_NAME_INPUT).send_keys(name)
        driver.find_element(*Locators.REG_EMAIL_INPUT).send_keys(email)
        driver.find_element(*Locators.REG_PASSWORD_INPUT).send_keys(password)
        driver.find_element(*Locators.REG_REGISTRATION_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.url_changes(driver.current_url))

        assert driver.current_url == LOGIN_URL

        driver.quit()

    def test_registration_password_length_less_six_simbols(self):
        
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(REG_URL)
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.REG_REGISTRATION_BUTTON))

        name, email, password = password_length_less_six_creds_randomizer()

        driver.find_element(*Locators.REG_NAME_INPUT).send_keys(name)
        driver.find_element(*Locators.REG_EMAIL_INPUT).send_keys(email)
        driver.find_element(*Locators.REG_PASSWORD_INPUT).send_keys(password)
        driver.find_element(*Locators.REG_REGISTRATION_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.REG_INCORRECT_PASSWORD_MESSAGE))

        assert driver.find_element(*Locators.REG_INCORRECT_PASSWORD_MESSAGE).is_displayed() == True

        driver.quit()


        