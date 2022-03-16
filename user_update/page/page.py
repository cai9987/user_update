"""page_login.py"""
from user_update import page
from user_update.base.base import Base


class PageLogin(Base):

    # 点击个人信息
    def page_click_user(self):
        self.base_click(page.login_user)

    # 点击个人详情
    def page_click_user_all(self):
        self.base_click(page.user_all)

    # 编辑按钮
    def page_click_user_update(self):
        self.base_click(page.user_update)

    # 昵称
    def page_input_user_name(self, user_name):
        self.base_input(page.user_name, user_name)

    # 头衔
    def page_input_user_header(self, user_header):
        self.base_input(page.user_header, user_header)

    # 性别
    def page_click_user_sex(self):
        self.base_click(page.user_sex)

    # 个人|团队
    def page_click_user_team(self):
        self.base_click(page.user_team)

    # 输入验证码
    def page_input_user_money(self, user_money):
        self.base_input(page.user_money, user_money)

    # 个人经历
    def page_input_user_experience(self, user_user_experience):
        self.base_input(page.user_user_experience, user_user_experience)

    # 点击提交
    def page_click_user_summit(self):
        self.base_click(page.user_summit)

    # 修改成功
    def page_user_update_success(self):
        self.base_get_text(page.user_summit_success)

    # 截图
    def page_get_screenshot(self):
        self.base_get_image()

    # # 点击 安全退出->退出登录
    # def page_click_logout(self):
    #     self.base_click(page.login_logout)
    #
    # # 判断是否登录成功
    # def page_is_login_success(self):
    #     return self.base_if_success(page.login_logout)
    #
    # # 判断是否退出成功
    # def page_is_logout_success(self):
    #     return self.base_if_success(page.login_link)

    #  组合业务方法
    def page_login(self, user_name, user_header, user_money,user_experience):
        self.page_input_user_name(user_name)
        self.page_input_user_header(user_header)
        self.page_click_user_sex()
        self.page_click_user_team()
        self.page_input_user_money(user_money)
        self.page_input_user_experience(user_experience)
        self.page_click_user_summit()
