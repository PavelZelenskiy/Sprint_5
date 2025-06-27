from selenium.webdriver.common.by import By

class Locators:

#Registration form locators

    REG_NAME_INPUT = (By.XPATH, "//label[contains(text(), 'Имя')]/../input") #name input
    REG_EMAIL_INPUT = (By.XPATH, "//label[contains(text(), 'Email')]/../input") #email input
    REG_PASSWORD_INPUT = (By.XPATH, "//input[@name='Пароль']") #password input
    REG_REGISTRATION_BUTTON = (By.XPATH,"//button[contains(text(), 'Зарегистрироваться')]") #registration button
    REG_INCORRECT_PASSWORD_MESSAGE = (By.XPATH, "//p[contains(text(), 'Некорректный пароль')]") #incorrect password message

#Login form locators

    LOG_BUTTON_MAIN_SITE = (By.XPATH, "//button[contains(text(), 'Войти в аккаунт')]")
    LOG_EMAIL_INPUT = (By.XPATH, "//input[@name='name']")
    LOG_PASSWORD_INPUT = (By.XPATH, "//input[@name='Пароль']")
    LOG_LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Войти')]")
    LOG_BUTTON_REGISTRATION_FORM = (By.XPATH, "//a[@href='/login']")
    LOG_BUTTON_FORGOT_PASSWORD_FORM = (By.XPATH, "//a[@href='/login']")

#Navbar locators

    LOGO_BUTTON = (By.XPATH, "//div/a[@href='/']")
    CONSTRUCTOR_BUTTON = (By.XPATH, "//li//a[@href='/']")

#Personal account locators

    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//a[@href='/account']")
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(), 'Выход')]")

#Constructor tabs locators

    CONSTRUCTOR_BUNS_TAB = (By.XPATH, "//span[contains(text(), 'Булки')]")
    CONSTRUCTOR_SAUCES_TAB = (By.XPATH, "//span[contains(text(), 'Соусы')]")
    CONSTRUCTOR_FILLINGS_TAB = (By.XPATH, "//span[contains(text(), 'Начинки')]")
    CONSTRUCTOR_BUNS_HEADER = (By.XPATH, "//h2[contains(text(), 'Булки')]")
    CONSTRUCTOR_SAUCES_HEADER = (By.XPATH, "//h2[contains(text(), 'Соусы')]")
    CONSTRUCTOR_FILLINGS_HEADER = (By.XPATH, "//h2[contains(text(), 'Начинки')]")
    CONSTRUCTOR_ACTIVE_TAB = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]")