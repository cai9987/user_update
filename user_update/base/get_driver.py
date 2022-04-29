"""get_driver.py"""
# -*-coding:utf-8 -*-
# Auothor:yue_luo
from time import sleep

from selenium import webdriver
from user_update import page


class GetDriver:
    driver = None

    @classmethod
    def get_driver(cls):
        if cls.driver is None:
            cls.driver = webdriver.Chrome()
            cls.driver.maximize_window()
            cls.driver.get(page.url)
            sleep(5)
            cls.driver.add_cookie({"name":"token","value":"2dfc33e02dec5dfeaccbb309d151197bbaa0157f"})
            cls.driver.refresh()
            sleep(10)
        return cls.driver

    @classmethod
    def quit_driver(cls):
        if cls.driver:
            cls.driver.quit()
            """置空"""
            cls.driver = None
