from .base_page import BasePage
from .locators import MainPageLocators
from selenium.webdriver.common.by import By

class MainPage(BasePage):
    def open_login_popup(self):
        link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        link.click()

  #  def auth_by_phone(self):
  #      link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
   #     link.click()
   #     input_phone = self.browser.find_element(*MainPageLocators.PHONE_INPUT)
   #     input_phone.send_keys("+79258227450")
   #     submit_button = self.browser.find_element(*MainPageLocators.SEND_CODE_BUTTON)
   #     submit_button.click()
