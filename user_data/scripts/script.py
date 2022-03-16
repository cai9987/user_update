"""test_login.py"""
# -*-coding:utf-8 -*-
# Auothor:yue_luo

# 导包
import unittest
from time import sleep
from parameterized import parameterized

from user_data.base.get_driver import GetDriver
from user_data.page.page import PageLogin

# 参数化
from user_data.read_json.read_json  import read_json


def get_data():
    data = read_json("user_update.json")
    """
       期望数据格式：[("13099999999","123456","8888","账号不存在!",false),
            ("17864307785","error","8888","密码错误!",false)]
    """
    list = []
    for n in data.values():
        list.append((n["username"], n["pwd"], n["code"], n["msg"], n["flag"]))  # n["key"] 或n.get("key")
    return list


# 新建测试类并继承
class TestLogin(unittest.TestCase):

    # setUp
    @classmethod
    def setUpClass(cls):
        # 实例化 获取登录对象
        cls.login = PageLogin(GetDriver().get_driver())
        # 点击登录链接
        PageLogin(GetDriver().get_driver()).page_click_login_link()

    # tearDown
    @classmethod
    def tearDownClass(cls):
        # 关闭driver浏览器驱动对象
        sleep(3)
        GetDriver().quit_driver()

    # 登录测试方法
    @parameterized.expand(get_data())
    def test_login(self, username, pwd, code, expect_result, success):
        # 调用登录方法
        self.login.page_login(username, pwd, code)
        # 登陆成功
        if success:
            try:
                # 判断 安全退出是否存在
                self.assertTrue(self.login.page_is_login_success())
                print("***登录成功")
                # 退出
                self.login.page_click_logout()
                try:
                    self.assertTrue(self.login.page_is_logout_success())
                    self.login.page_click_login_link()
                except AssertionError:
                    # 截图
                    self.login.page_get_screenshot()
                    raise
            except AssertionError:
                # 截图
                self.login.page_get_screenshot()
                raise
        else:
            # 获取登录提示信息
            result = self.login.page_get_error_info()
            print("result；", result)
            sleep(1)
            # 断言
            try:
                self.assertIn(result, expect_result)
                sleep(1)
            except AssertionError:
                # 截图
                self.login.page_get_screenshot()
                raise
            finally:
                # 点击提示框确定按钮
                self.login.page_click_error_btn_ok()
                sleep(1)
