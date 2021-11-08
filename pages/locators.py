from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "##topMenu .BaseButton_button_1gx-n:nth-child(2)")
    PHONE_INPUT = (By.CSS_SELECTOR, '[name="phoneNumber"]')
    SEND_CODE_BUTTON = (By.CSS_SELECTOR, ".Form_small_2Jqea button")
