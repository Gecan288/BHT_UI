import Page, allure, time
from base.base import Base


class PagePwd(Base):

    @allure.step("跳过开屏广告")
    def page_jump_advertisement(self):
        self.base_click(Page.advertisement)

    @allure.step("点击我的")
    def page_click_me(self):
        self.base_click(Page.navigation_me)
        self.base_switch_webview()

    @allure.step("登录账号")
    def page_login(self):
        self.base_input(Page.login_input_username, "15704912750")
        self.base_input(Page.login_input_password, "qwer1234")
        self.base_click(Page.login_login_btn)

    @allure.step("点击设置")
    def page_click_setting(self):
        self.base_click(Page.me_setting)

    @allure.step("点击修改登录密码")
    def page_click_change_password(self):
        self.base_clicks(Page.set_change_password, 0)

    @allure.step("选择不记得")
    def page_click_forget(self):
        self.base_clicks(Page.set_tips_forget_password, -2)

    @allure.step("选择记得")
    def page_click_remember(self):
        self.base_clicks(Page.set_tips_remember_password, -1)

    @allure.step("输入手机号")
    def page_input_phone(self, phone):
        self.base_input(Page.forget_password_phone, phone)

    @allure.step("输入验证码")
    def page_input_code(self, code):
        self.base_input(Page.forget_password_code, code)

    @allure.step("获取验证码")
    def page_get_code(self):
        self.base_click(Page.forget_password_get_code)

    @allure.step("输入密码")
    def page_input_password(self, password):
        self.base_input(Page.forget_password_password, password)

    @allure.step("点击确定")
    def page_click_change(self):
        self.base_click(Page.change_password_btn)

    @allure.step("获取toast")
    def page_get_toast(self):
        time.sleep(0.1)
        for i in range(10):
            if "加载中" in self.base_get_text(Page.login_error_toast, timeout=2, poll=0.1):
                pass
            else:
                return self.base_get_text(Page.login_error_toast, timeout=2, poll=0.1)

    def page_getImage(self):
        self.base_switch_native()
        self.base_getImage()
        self.base_switch_webview()

    @staticmethod
    def page_write_to_report():
        with open("./Image/faild.png", "rb")as f:
            allure.attach(f.read(), "失败原因见截图:", allure.attachment_type.PNG)

    @allure.step("输入原密码")
    def page_input_old_password(self, old_password):
        self.base_input(Page.change_password_old, old_password)

    @allure.step("输入新密码")
    def page_input_new_password(self, new_password):
        self.base_input(Page.change_password_new, new_password)

    @allure.step("输入确认密码")
    def page_input_confirm_password(self, confirm):
        self.base_input(Page.change_password_confirm, confirm)

    @allure.step("获取页面title")
    def page_get_page_title(self):
        return self.base_get_text(Page.page_title)

    @allure.step("点击忘记密码")
    def page_click_forget_password(self):
        self.base_click(Page.login_forget_password)
