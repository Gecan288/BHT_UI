import pytest, sys, os, allure
sys.path.append(os.getcwd())
from base.get_data import read_line
from Page.page_in import PageIn


@allure.feature("综合视频模块")
class TestVideo():

    def setup_class(self):
        self.video = PageIn().page_get_video()
        self.video.page_jump_advertisement()
        self.video.page_click_me()

    def teardown_class(self):
        self.video.page_logout()
        self.video.driver.quit()

    @allure.story("验证实名认证")
    @allure.title("跳转实名认证")
    @allure.step("开始执行用例")
    @pytest.mark.parametrize("username, password, page_title", read_line("video.txt", end=1))
    def test_video_authentication(self, username, password, page_title):
        try:
            self.video.page_login(username, password)
            self.video.page_click_video()
            self.video.page_tips_click_authentication()
            assert page_title in self.video.page_get_page_title()
        except:
            self.video.page_screenshot_and_write()
            raise

    @allure.story("验证服务协议")
    @allure.title("跳转协议")
    @allure.step("开始执行用例")
    @pytest.mark.parametrize("username, password, page_title", read_line("video.txt", 1))
    def test_video_agreement(self, username, password, page_title):
        try:
            self.video.page_back()
            self.video.page_click_video()
            self.video.page_tips_click_jump()
            assert page_title in self.video.page_get_page_title()
        except:
            self.video.page_screenshot_and_write()
            raise
