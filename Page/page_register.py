import Page, allure
from base.base import Base
from appium.webdriver.common.touch_action import TouchAction

class PageRegister(Base):

    @allure.step("跳过开屏广告")
    def page_jump_advertisement(self):
        self.base_click(Page.advertisement)

    @allure.step("点击我的")
    def page_click_me(self):
        self.base_click(Page.navigation_me)
        self.base_switch_webview()

    @allure.step("点击用户注册")
    def page_click_user_register(self):
        self.base_click(Page.login_user_register)

    @allure.step("输入手机号")
    def page_input_phone(self, phone_number):
        self.base_input(Page.register_input_phone, phone_number)

    @allure.step("输入密码")
    def page_input_password(self, password):
        self.base_input(Page.register_input_password, password)

    @allure.step("输入验证码")
    def page_input_code(self, phone_code):
        self.base_input(Page.register_input_code, phone_code)

    @allure.step("获取验证码")
    def page_get_code(self):
        self.base_click(Page.register_get_code)

    @allure.step("点击注册")
    def page_click_register_btn(self):
        self.base_click(Page.register_register_btn)

    @allure.step("获取toast")
    def page_get_toast(self):
        for i in range(10):
            if "加载中" in self.base_get_text(Page.register_error_toast, timeout=2, poll=0.1):
                pass
            else:
                return self.base_get_text(Page.register_error_toast, timeout=2, poll=0.1)

    def page_getImage(self):
        self.base_switch_native()
        self.base_getImage()
        self.base_switch_webview()

    def page_write_to_report(self):
        with open("./Image/faild.png", "rb")as f:
            allure.attach(f.read(), "失败原因见截图:", allure.attachment_type.PNG)

    @allure.step("进入商城协议")
    def page_click_mall_agreement(self):
        self.base_clicks(Page.register_agreement, 0)

    @allure.step("进入隐私协议")
    def page_click_privacy_agreement(self):
        self.base_clicks(Page.register_agreement, 1)

    @allure.step("进入视频综合协议")
    def page_click_video_agreement(self):
        self.base_clicks(Page.register_agreement, -1)

    @allure.step("阅读并同意协议")
    def page_read_agreement_agree(self):
        self.base_click(Page.register_agreement_tips)
        self.base_switch_native()
        for i in range(15):
            TouchAction(self.driver).press(x=500, y=1900).move_to(x=0, y=-2000).release().perform()
        TouchAction(self.driver).press(x=300, y=1950).release().perform()
        self.base_switch_webview()
