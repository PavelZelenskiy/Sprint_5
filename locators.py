from selenium.webdriver.common.by import By

class Locators:

#Registration form locators

    REG_NAME_INPUT = (By.XPATH, "//label[contains(text(), 'Имя')]/../input") #name input
    REG_EMAIL_INPUT = (By.XPATH, "//label[contains(text(), 'Email')]/../input") #email input
    REG_PASSWORD_INPUT = (By.XPATH, "//input[@name='Пароль']") #password input
    REG_REGISTRATION_BUTTON = (By.XPATH,"//button[contains(text(), 'Зарегистрироваться')]") #registration button
    REG_INCORRECT_PASSWORD_MESSAGE = (By.XPATH, "//p[contains(text(), 'Некорректный пароль')]") #incorrect password message