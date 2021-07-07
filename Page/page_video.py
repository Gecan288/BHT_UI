import Page, allure, time
from base.base import Base


class PageVideo(Base):

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

    @allure.step("退出登录")
    def page_logout(self):
        self.base_back()
        time.sleep(1)
        self.base_click(Page.me_setting)
        time.sleep(2)
        self.base_click(Page.set_logout)
        self.base_click(Page.set_logout_ok)
        time.sleep(2)

    @allure.step("点击综合视频")
    def page_click_video(self):
        self.base_click(Page.navigation_video)

    @allure.step("跳过认证")
    def page_tips_click_jump(self):
        self.base_click(Page.video_tips_jump)

    @allure.step("点击去认证")
    def page_tips_click_authentication(self):
        self.base_click(Page.video_tips_authentication)

    @allure.step("获取页面title")
    def page_get_page_title(self):
        time.sleep(2)
        return self.base_get_text(Page.page_title)

    @allure.step("返回上一页")
    def page_back(self):
        self.base_back()

    def page_screenshot_and_write(self):
        self.base_switch_native()
        self.base_getImage()
        self.base_switch_native()
        with open("./Image/faild.png", "rb")as f:
            allure.attach(f.read(), "失败原因见截图:", allure.attachment_type.PNG)
