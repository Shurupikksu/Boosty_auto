from .pages.main_page import MainPage
import pytest

def test_can_open_main_page(browser):
    link = "https://boosty.to/"
    page = MainPage(browser, link)
    page.open()

