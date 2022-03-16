"""__init__.py"""
# -*-coding:utf-8 -*-
# Auothor:yue_luo
from selenium.webdriver.common.by import By

"""以下为服务器域名配置地址"""
url = "https://www.zaitakugeek.cn/home/index"

cookies = {"name":"token","value":"82f8ca6b6bb4ad1483bbab9e184bfa17f0a5a0c6"}

"""以下为登录页面配置信息"""
# 个人信息
login_user = By.XPATH, "html/body/div[1]/div[2]/div[1]/div[2]/ul/li[7]/div/span[2]"
# 个人详情
user_all = By.XPATH, "html/body/div[2]/ul/li[1]"
# 编辑按钮
user_update = By.XPATH, "html/body/div[1]/div[2]/div[2]/div[2]/div[2]/div[2]/div[1]/div[1]/div[2]/button"
# 昵称
user_name = By.XPATH, "html/body/div[1]/div[2]/div[2]/div[2]/div[2]/div[2]/div/form/div[2]/div/div/input"
# 头衔
user_header = By.XPATH, "html/body/div[1]/div[2]/div[2]/div[2]/div[2]/div[2]/div/form/div[3]/div/div/input"
# 性别
user_sex = By.XPATH, "html/body/div[1]/div[2]/div[2]/div[2]/div[2]/div[2]/div/form/div[4]/div/div/label[2]/span[2]"
# 个人|团队
user_team = By.XPATH, "html/body/div[1]/div[2]/div[2]/div[2]/div[2]/div[2]/div/form/div[6]/div/div/label[1]/span[2]"
# 预期金额
user_money = By.XPATH, "html/body/div[1]/div[2]/div[2]/div[2]/div[2]/div[2]/div/form/div[7]/div/div/input"
# 个人经历
user_user_experience = By.XPATH, "html/body/div[1]/div[2]/div[2]/div[2]/div[2]/div[2]/div/form/div[10]/div/div/div/div[2]/div[1]/div"
# 提交
user_summit = By.XPATH, "html/body/div[1]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div/button[1]"
# 修改成功
user_summit_success = By.XPATH, "html/body/div[3]/p"
