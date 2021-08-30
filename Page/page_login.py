import Page, allure, time
from base.base import Base


class PageLogin(Base):

    @allure.step("跳过开屏广告")
    def page_jump_advertisement(self):
        self.base_click(Page.advertisement)

    @allure.step("点击我的")
    def page_click_me(self):
        self.base_click(Page.navigation_me)
        self.base_switch_webview()

    @allure.step("输入用户名")
    def page_input_username(self, username):
        self.base_input(Page.login_input_username, username)

    @allure.step("输入密码吗")
    def page_input_password(self, password):
        self.base_input(Page.login_input_password, password)

    @allure.step("点击登录")
    def page_click_login_btn(self):
        self.base_click(Page.login_login_btn)

    @allure.step("获取昵称")
    def page_get_nikename(self):
        return self.base_get_text(Page.me_nikename)

    @allure.step("退出登录")
    def page_logout(self):
        self.base_click(Page.me_setting)
        self.base_click(Page.set_logout)
        self.base_click(Page.set_logout_ok)
        time.sleep(2)

    @allure.step("获取toast")
    def page_get_error_toast(self):
        for i in range(10):
            if "加载中" in self.base_get_text(Page.login_error_toast, timeout=2, poll=0.1):
                pass
            else:
                return self.base_get_text(Page.login_error_toast, timeout=2, poll=0.1)

    def page_screenshot_and_write(self):
        self.base_switch_native()
        self.base_getImage()
        self.base_switch_webview()
        with open("./Image/faild.png", "rb")as f:
            allure.attach(f.read(), "失败原因见截图:", allure.attachment_type.PNG)

    @allure.step("点击验证码登录")
    def page_click_login_type(self):
        self.base_click(Page.login_type_code)

    @allure.step("输入手机号")
    def page_input_phone(self, phone):
        self.base_input(Page.login_input_phone, phone)

    @allure.step("输入验证码")
    def page_input_code(self, ms_code):
        self.base_input(Page.login_input_code, ms_code)

    @allure.step("获取验证码")
    def page_get_code(self):
        self.base_click(Page.login_get_code)
