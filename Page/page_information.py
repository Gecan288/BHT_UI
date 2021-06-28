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
    def page_login(self, username="13439200080", password="qwer1234"):
        self.base_input(Page.login_input_username, username)
        self.base_input(Page.login_input_password, password)
        self.base_click(Page.login_login_btn)
        time.sleep(2)

    @allure.step("点击基本资料")
    def page_click_information(self):
        self.base_click(Page.me_information)
        time.sleep(1)

    @allure.step("点击昵称")
    def page_click_nikename(self):
        self.base_clicks(Page.information_nike_name, 1)
        time.sleep(1)

    @allure.step("输入新昵称")
    def page_input_new_name(self, name):
        self.base_input(Page.information_input_name, name)

    @allure.step("获取新昵称")
    def page_get_new_name(self):
        return self.base_get_texts(Page.information_nike_name, 1)

    @allure.step("获取原属性值")
    def page_get_old_value(self):
        return self.base_get_attribute(Page.information_old_name, "value")

    @allure.step("点击确定按钮")
    def page_click_confirm_btn(self):
        self.base_click(Page.information_confirm_btn)

    @allure.step("获取toast")
    def page_get_toast(self):
        time.sleep(0.1)
        for i in range(10):
            if "加载中" in self.base_get_text(Page.home_toast, timeout=2, poll=0.1):
                pass
            else:
                return self.base_get_text(Page.home_toast, timeout=2, poll=0.1)

    @allure.step("点击常用邮箱")
    def page_click_email(self):
        self.base_clicks(Page.information_email, 3)

    @allure.step("输入新邮箱")
    def page_input_new_email(self, email):
        self.base_input(Page.information_input_email, email)

    @allure.step("获取新邮箱")
    def page_get_new_email(self):
        return self.base_get_texts(Page.information_email, 3)

    @allure.step("点击手机号")
    def page_click_phone(self):
        self.base_clicks(Page.information_phone, 2)

    @allure.step("输入密码")
    def page_input_password(self, password="qwer1234"):
        self.base_input(Page.information_input_password, password)

    @allure.step("输入新手机号")
    def page_input_new_phone(self, phone="13439200080"):
        self.base_input(Page.information_input_new_phone, phone)

    @allure.step("输入验证码")
    def page_input_code(self, code):
        self.base_input(Page.information_input_code, code)

    @allure.step("获取验证码")
    def page_get_code(self):
        self.base_click(Page.information_get_code)
        time.sleep(1)

    @allure.step("获取页面title")
    def page_get_page_title(self):
        time.sleep(1)
        return self.base_get_text(Page.page_title)

    def page_screenshot_and_write(self):
        self.base_switch_native()
        self.base_getImage()
        self.base_switch_native()
        with open("./Image/faild.png", "rb")as f:
            allure.attach(f.read(), "失败原因见截图:", allure.attachment_type.PNG)
