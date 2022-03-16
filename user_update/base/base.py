"""base.py"""
# -*-coding:utf-8 -*-
# Auothor:yue_luo
import time

from selenium.webdriver.support.wait import WebDriverWait


class Base:

    # 初始化
    def __init__(self, driver):
        self.driver = driver

    # 查找元素方法
    def base_find_element(self, loc, timeout=30, poll_frequency=0.5):
        return WebDriverWait(driver=self.driver, timeout=timeout, poll_frequency=poll_frequency).until(
            lambda x: x.find_element(*loc))

    # 点击方法
    def base_click(self, loc):
        self.base_find_element(loc).click()

    # 输入方法
    def base_input(self, loc, value):
        element = self.base_find_element(loc)
        element.clear()
        element.send_keys(value)

    # 获取文本方法
    def base_get_text(self, loc):
        msg = self.base_find_element(loc).text
        return msg

    # 截图
    def base_get_image(self, ):
        self.driver.get_screenshot_as_file("../report/{}.png".format(time.strftime("%Y_%m_%d_%H_%M_%S")))

    # 判断元素是否存在
    def base_if_success(self, loc):
        try:
            self.base_find_element(loc, timeout=2)
            # 找到元素 assertTrue
            return True
        except:
            return False
