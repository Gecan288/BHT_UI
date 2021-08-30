import Page, allure, time
from base.base import Base


class PageSetting(Base):

    @allure.step("跳过开屏广告")
    def page_jump_advertisement(self):
        self.base_click(Page.advertisement)

    @allure.step("点击我的")
    def page_click_me(self):
        self.base_click(Page.navigation_me)
        self.base_switch_webview()

    @allure.step("登录账号")
    def page_login(self):
        self.base_input(Page.login_input_username, "13439200080")
        self.base_input(Page.login_input_password, "qwer1234")
        self.base_click(Page.login_login_btn)
        time.sleep(2)

    @allure.step("退出登录")
    def page_logout(self):
        self.base_back()
        self.base_back()
        self.base_click(Page.set_logout)
        self.base_click(Page.set_logout_ok)
        time.sleep(2)

    @allure.step("点击设置")
    def page_click_setting(self):
        self.base_click(Page.me_setting)

    @allure.step("点击账户安全中心")
    def page_click_safe_center(self):
        self.base_clicks(Page.set_safe_center, -2)

    @allure.step("点击注销账号")
    def page_click_cancel_account(self):
        self.base_click(Page.safe_center_cancel_account)

    @allure.step("点击申请注销")
    def page_click_logoff(self):
        self.base_click(Page.cancel_account_logoff_btn)

    @allure.step("输入验证码")
    def page_input_code(self, code):
        self.base_input(Page.logoff_input_code, code)

    @allure.step("点击确定")
    def page_click_logoff_confirm(self):
        self.base_clicks(Page.logoff_confirm, 0)

    @allure.step("获取toast")
    def page_get_toast(self):
        time.sleep(0.3)
        for i in range(10):
            if "加载中" in self.base_get_text(Page.logoff_toast, timeout=2, poll=0.1):
                pass
            else:
                return self.base_get_text(Page.logoff_toast, timeout=2, poll=0.1)

    @allure.step("点击取消")
    def page_click_logoff_cancel(self):
        self.base_clicks(Page.logoff_cancel, -1)
        self.base_back()
        self.base_back()

    @allure.step("获取验证码")
    def page_get_code(self):
        self.base_click(Page.logoff_get_code)

    @allure.step("点击关于")
    def page_click_about(self):
        self.base_clicks(Page.set_about, -1)

    @allure.step("点击保互通简介")
    def page_click_bht_introduction(self):
        self.base_clicks(Page.about_bht_introduction, 0)

    @allure.step("点击法律声明")
    def page_click_law_statement(self):
        self.base_clicks(Page.about_bht_introduction, -1)

    @allure.step("获取页面title")
    def page_get_page_title(self):
        time.sleep(1)
        return self.base_get_text(Page.page_title)

    @allure.step("返回上一页")
    def page_back(self):
        self.base_back()

    def page_screenshot_and_write(self):
        self.base_switch_native()
        self.base_getImage()
        self.base_switch_webview()
        with open("./Image/faild.png", "rb")as f:
            allure.attach(f.read(), "失败原因见截图:", allure.attachment_type.PNG)
