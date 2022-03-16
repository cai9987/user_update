"""__init__.py"""
# -*-coding:utf-8 -*-
# Auothor:yue_luo
from selenium.webdriver.common.by import By

"""以下为服务器域名配置地址"""
url ="http://127.0.0.1/index.php"

"""以下为登录页面配置信息"""
# 登录链接
login_link = By.PARTIAL_LINK_TEXT , "登录"
# 用户名
login_username = By.ID,"username"
# 密码
login_pwd = By.NAME,"password"
# 验证码
login_verify_code = By.CSS_SELECTOR,"#verify_code"
# 登录按钮
login_btn =By.NAME,"sbtbutton"
# 获取异常文本信息
login_err_info = By.CLASS_NAME,"layui-layer-content"
# 异常提示框 确定按钮
login_err_btn_ok = By.CSS_SELECTOR,".layui-layer-btn0"
# 安全退出
login_logout = By.PARTIAL_LINK_TEXT,"安全退出"
