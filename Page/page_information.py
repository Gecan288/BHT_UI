import Page, allure, time
from base.base import Base

class PageInformation(Base):

    @allure.step("跳过开屏广告")
    def page_jump_advertisement(self):
        self.base_click(Page.advertisement)

    @allure.step("点击我的")
    def page_click_me(self):
        self.base_click(Page.navigation_me)
        self.base_switch_webview()

    @allure.step("登录账号")
    def page_login(self, username, password):
        self.base_input(Page.login_input_username, username)
        self.base_input(Page.login_input_password, password)
        self.base_click(Page.login_login_btn)
        time.sleep(2)

    def page_logout(self):
        time.sleep(1)
        pass