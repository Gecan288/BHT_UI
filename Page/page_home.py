import Page, allure, time
from base.base import Base


class PageHome(Base):
    @allure.step("跳过开屏广告")
    def page_jump_advertisement(self):
        self.base_click(Page.advertisement)
        time.sleep(5)
        self.base_switch_webview()

    @allure.step("点击我的")
    def page_click_me(self):
        self.base_switch_native()
        self.base_click(Page.navigation_me)
        self.base_switch_webview()

    @allure.step("点击首页")
    def page_click_home(self):
        self.base_switch_native()
        self.base_click(Page.navigation_home)
        self.base_switch_webview()

    @allure.step("点击首页员工认证")
    def page_click_home_authentication(self):
        self.base_click(Page.home_authentication)

    @allure.step("点击首页组织机构")
    def page_click_home_organization(self):
        self.base_click(Page.home_organization)

    @allure.step("点击首页人保钱包")
    def page_click_home_wallet(self):
        self.base_click(Page.home_wallet)

    @allure.step("登录账号")
    def page_login(self, username, password):
        self.base_input(Page.login_input_username, username)
        self.base_input(Page.login_input_password, password)
        self.base_click(Page.login_login_btn)
        time.sleep(2)

    @allure.step("退出登录")
    def page_logout(self):
        self.base_click(Page.me_setting)
        time.sleep(1)
        self.base_click(Page.set_logout)
        self.base_click(Page.set_logout_ok)
        time.sleep(2)

    @allure.step("获取toast")
    def page_get_toast(self):
        return self.base_get_text(Page.home_toast)

    def page_screenshot_and_write(self):
        self.base_switch_native()
        self.base_getImage()
        self.base_switch_webview()
        with open("./Image/faild.png", "rb")as f:
            allure.attach(f.read(), "失败原因见截图:", allure.attachment_type.PNG)

    @allure.step("获取页面title")
    def page_get_title(self):
        time.sleep(2)
        el = self.base_get_text(Page.page_title)
        self.base_back()
        return el
