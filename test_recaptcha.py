from .pages.main_page import MainPage
import pytest

def test_login_by_phone(browser):
    link = "https://boosty-stage1.s.smailru.net/"
    page = MainPage(browser, link)
    page.open()
 #   page.auth_by_phone()