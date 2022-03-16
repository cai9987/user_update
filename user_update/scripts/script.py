"""test_login.py"""
# -*-coding:utf-8 -*-
# Auothor:yue_luo

# 导包
import unittest
from time import sleep
from parameterized import parameterized

from user_update.base.get_driver import GetDriver
from user_update.page import page
from user_update.page.page import PageLogin

# 参数化
from user_update.read_json.read_json import ReadJson


def get_data():
    datas = ReadJson("user_update.json").read_json()
    arrs = []
    for data in datas.values():
        arrs.append((data.get("user_name"),
                     data.get("user_header"),
                     data.get("user_moner"),
                     data.get("user_experience"),
                     data.get("result")))
    return arrs


# 新建测试类并继承
class TestLogin(unittest.TestCase):

    # setUp
    @classmethod
    def setUpClass(cls):
        # 实例化 获取登录对象
        cls.login = PageLogin(GetDriver().get_driver())
        # 点击登录链接
        # sleep(5)
        # GetDriver().get_driver().add_cookie(page)
        # GetDriver().get_driver().refresh()
        # sleep(10)
        PageLogin(GetDriver().get_driver()).page_click_user()
        PageLogin(GetDriver().get_driver()).page_click_user_all()
        PageLogin(GetDriver().get_driver()).page_click_user_update()

    # tearDown
    @classmethod
    def tearDownClass(cls):
        # 关闭driver浏览器驱动对象
        sleep(3)
        GetDriver().quit_driver()

    # 登录测试方法
    @parameterized.expand(get_data())
    def test_login(self, user_name, user_header, user_money, user_experience, result):
        # 调用登录方法
        self.login.page_login(user_name, user_header, user_money, user_experience)
        msg = self.login.page_user_update_success()
        try:
            self.assertEqual(msg, result)
        except:
            self.login.page_get_screenshot()
