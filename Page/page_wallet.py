import Page, allure, time
from base.base import Base


class PageWallet(Base):

    @allure.step("跳过开屏广告")
    def page_jump_advertisement(self):
        self.base_click(Page.advertisement)

    @allure.step("点击导航栏钱包")
    def page_click_wallet(self):
        self.base_click(Page.navigation_wallet)
        self.base_switch_webview()

    @allure.step("登录账号")
    def page_login(self, username, password):
        self.base_input(Page.login_input_username, username)
        self.base_input(Page.login_input_password, password)
        self.base_click(Page.login_login_btn)
        time.sleep(2)

    @allure.step("退出登录")
    def page_logout(self):
        self.base_back()
        time.sleep(2)
        self.base_back()
        time.sleep(2)
        self.base_back()
        time.sleep(10)
        self.base_back()
        time.sleep(2)
        self.base_switch_native()
        self.base_click(Page.navigation_me)
        self.base_switch_webview()
        self.base_click(Page.me_setting)
        time.sleep(2)
        self.base_click(Page.set_logout)
        self.base_click(Page.set_logout_ok)
        time.sleep(2)

    @allure.step("点击人保钱包")
    def page_click_rb_wallet(self):
        self.base_click(Page.wallet_rb_wallet)

    @allure.step("点击银行卡")
    def page_click_bank_card(self):
        self.base_click(Page.wallet_bank_card)

    @allure.step("点击添加银行卡")
    def page_click_add_card(self):
        self.base_click(Page.bank_card_add)

    @allure.step("获取持卡人姓名")
    def page_get_cardholder(self):
        return self.base_get_attribute(Page.add_card_cardholder, "value")

    @allure.step("获取卡类型")
    def page_get_card_type(self):
        return self.base_get_attribute(Page.add_card_type, "value")

    @allure.step("输入银行卡号")
    def page_input_card_number(self, number):
        self.base_input(Page.add_card_input_number, number)

    @allure.step("点击下一步")
    def page_click_add_next(self):
        self.base_click(Page.add_card_next)

    @allure.step("输入验证码")
    def page_input_code(self, code):
        self.base_input(Page.add_card_input_code, code)

    @allure.step("点击下一步")
    def page_click_code_next(self):
        self.base_click(Page.add_card_code_next)

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
        self.base_switch_native()
        with open("./Image/faild.png", "rb")as f:
            allure.attach(f.read(), "失败原因见截图:", allure.attachment_type.PNG)
