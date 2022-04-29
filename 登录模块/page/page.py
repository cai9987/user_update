from time import sleep

from 登录模块.base.base import Base
from 登录模块 import page


class PageLogin(Base):
    def page_login_link(self):
        self.base_click(page.login_link)

    def page_input_username(self, username):
        self.base_input(page.login_input_username, username)

    def page_input_password(self, password):
        self.base_input(page.login_input_password, password)

    def page_login_btn(self):
        self.base_click(page.login_btn)

    def page_err_text(self):
        return self.base_get_text(page.login_err_text)

    def page_login_if_quit(self):
        return self.base_if_success(page.login_link)

    def page_get_image(self):
        self.base_get_image()

    def page_login(self, username, password):
        self.page_input_username(username)
        self.page_input_password(password)
        self.page_login_btn()
        sleep(1)
