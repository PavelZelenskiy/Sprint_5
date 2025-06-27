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


class TestConstructorTabs:

    def test_constructor_sauces_tab_transition(self, driver: WebDriver):

        driver.get(LOGIN_URL)
                
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.LOG_LOGIN_BUTTON))

        driver.find_element(*Locators.LOG_EMAIL_INPUT).send_keys(Creds.email)
        driver.find_element(*Locators.LOG_PASSWORD_INPUT).send_keys(Creds.password)
        driver.find_element(*Locators.LOG_LOGIN_BUTTON).click()
       
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.CONSTRUCTOR_SAUCES_TAB)).click()

        new_element = WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(Locators.CONSTRUCTOR_SAUCES_HEADER))
        assert new_element.is_displayed()

        active_tab = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.CONSTRUCTOR_ACTIVE_TAB))
        assert 'Соусы' in active_tab.text

        
    def test_constructor_fillings_tab_transition(self, driver: WebDriver):

        driver.get(LOGIN_URL)

        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.LOG_LOGIN_BUTTON))

        driver.find_element(*Locators.LOG_EMAIL_INPUT).send_keys(Creds.email)
        driver.find_element(*Locators.LOG_PASSWORD_INPUT).send_keys(Creds.password)
        driver.find_element(*Locators.LOG_LOGIN_BUTTON).click()

        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.CONSTRUCTOR_FILLINGS_TAB)).click()

        new_element = WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(Locators.CONSTRUCTOR_FILLINGS_HEADER))
        assert new_element.is_displayed()

        active_tab = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.CONSTRUCTOR_ACTIVE_TAB))
        assert 'Начинки' in active_tab.text


    def test_constructor_buns_tab_transition(self, driver: WebDriver):

        driver.get(LOGIN_URL)

        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.LOG_LOGIN_BUTTON))

        driver.find_element(*Locators.LOG_EMAIL_INPUT).send_keys(Creds.email)
        driver.find_element(*Locators.LOG_PASSWORD_INPUT).send_keys(Creds.password)
        driver.find_element(*Locators.LOG_LOGIN_BUTTON).click()
       
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.CONSTRUCTOR_FILLINGS_TAB)).click()

        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.CONSTRUCTOR_BUNS_TAB)).click()

        new_element = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.CONSTRUCTOR_BUNS_HEADER))
        assert new_element.is_displayed()

        active_tab = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.CONSTRUCTOR_ACTIVE_TAB))
        assert 'Булки' in active_tab.text

        

    
        
