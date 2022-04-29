from time import sleep

from parameterized import parameterized
import unittest

from 登录模块.base.get_driver import GetDriver
from 登录模块.page.page import PageLogin
from 登录模块.read_json.read_json import ReadJson


def get_data():
    datas = ReadJson("login.json").read_json()
    arrs = []
    for data in datas.values():
        arrs.append((data.get("username"),
                     data.get("password"),
                     data.get("result"),
                     data.get("flag"),
                     data.get("num")))
    return arrs


class TestLogin(unittest.TestCase):

    login = None

    @classmethod
    def setUpClass(cls):
        # 实例化driver并获取
        cls.driver = GetDriver().get_driver()
        # 实例化 获取登录对象
        cls.login = PageLogin(GetDriver().get_driver())
        # 点击登录链接
        cls.login.page_login_link()

    @classmethod
    def tearDownClass(cls) -> None:
        sleep(3)
        GetDriver.quit_driver()

    @parameterized.expand(get_data())
    def test_wind(self, username, password, result, flag, num):
        self.login.page_login(username, password)
        # if flag:
        #     try:
        #         # 判断 安全退出是否存在
        #         self.assertTrue(self.login.page_if_success())
        #         print("登录成功",num)
        #         # 退出
        #         self.login.page_login_success()
        #         self.login.page_quit_login()
        #         # self.driver.find_element_by_css_selector("#J_head_user_a").click()
        #         #
        #         # sleep(2)
        #         # self.driver.find_element_by_xpath(
        #         #     "html/body/div[1]/header/div/div[5]/div/div/div/ul[2]/li[2]/a").click()
        #         try:
        #             self.assertTrue(self.login.page_login_if_quit())
        #         except AssertionError:
        #             # 截图
        #             self.login.page_get_image()
        #             raise
        #     except AssertionError:
        #         # 截图
        #         self.login.page_get_image()
        #         raise
        #     finally:
        #         self.login.page_login_link()
        # else:
        #     msg = self.login.page_err_text()
        #     print(msg)
        #     try:
        #         self.assertEqual(msg,result)
        #     except AssertionError:
        #         self.login.page_get_image()
        #         print("错误",num)
        #         raise





