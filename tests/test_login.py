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


class TestLogin:

    def test_login_from_main_site(self, driver: WebDriver):
       
        driver.get(BASE_URL)
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.LOG_BUTTON_MAIN_SITE))

        driver.find_element(*Locators.LOG_BUTTON_MAIN_SITE).click()
        WebDriverWait(driver, 10).until(expected_conditions.url_changes(BASE_URL))

        driver.find_element(*Locators.LOG_EMAIL_INPUT).send_keys(Creds.email)
        driver.find_element(*Locators.LOG_PASSWORD_INPUT).send_keys(Creds.password)
        driver.find_element(*Locators.LOG_LOGIN_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.url_changes(driver.current_url))

        assert driver.current_url == BASE_URL


    def test_login_from_personal_account_button(self, driver: WebDriver):

        driver.get(BASE_URL)
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.PERSONAL_ACCOUNT_BUTTON))

        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.url_changes(BASE_URL))

        driver.find_element(*Locators.LOG_EMAIL_INPUT).send_keys(Creds.email)
        driver.find_element(*Locators.LOG_PASSWORD_INPUT).send_keys(Creds.password)
        driver.find_element(*Locators.LOG_LOGIN_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.url_changes(driver.current_url))

        assert driver.current_url == BASE_URL

        
    def test_login_from_registration_form(self, driver: WebDriver):

        driver.get(REG_URL)
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.LOG_BUTTON_REGISTRATION_FORM))

        driver.find_element(*Locators.LOG_BUTTON_REGISTRATION_FORM).click()
        WebDriverWait(driver, 10).until(expected_conditions.url_changes(REG_URL))

        driver.find_element(*Locators.LOG_EMAIL_INPUT).send_keys(Creds.email)
        driver.find_element(*Locators.LOG_PASSWORD_INPUT).send_keys(Creds.password)
        driver.find_element(*Locators.LOG_LOGIN_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.url_changes(driver.current_url))

        assert driver.current_url == BASE_URL

        
    def test_login_from_forgot_password_form(self, driver: WebDriver):
        
        driver.get(FORGOT_PASSWORD_URL)
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.LOG_BUTTON_FORGOT_PASSWORD_FORM))
        
        driver.find_element(*Locators.LOG_BUTTON_FORGOT_PASSWORD_FORM).click()
        WebDriverWait(driver, 10).until(expected_conditions.url_changes(FORGOT_PASSWORD_URL))

        driver.find_element(*Locators.LOG_EMAIL_INPUT).send_keys(Creds.email)
        driver.find_element(*Locators.LOG_PASSWORD_INPUT).send_keys(Creds.password)
        driver.find_element(*Locators.LOG_LOGIN_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.url_changes(driver.current_url))
        
        assert driver.current_url == BASE_URL

        