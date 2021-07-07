import pytest, sys, os, allure
sys.path.append(os.getcwd())
from base.get_data import read_line
from Page.page_in import PageIn


@allure.feature("设置模块")
class TestSetting:

    def setup_class(self):
        self.setting = PageIn().page_get_setting()
        self.setting.page_jump_advertisement()
        self.setting.page_click_me()
        self.setting.page_login()

    def teardown_class(self):
        self.setting.page_logout()
        self.setting.driver.quit()

    @allure.story("保互通简介")
    @allure.title("{case_title}")
    @allure.step("开始执行用例")
    @pytest.mark.parametrize("case_title, page_title, toast", read_line("setting.txt", end=1))
    def test_bht_introduction(self, case_title, page_title, toast):
        try:
            self.setting.page_click_setting()
            self.setting.page_click_about()
            self.setting.page_click_bht_introduction()
            assert page_title in self.setting.page_get_page_title()
        except Exception:
            self.setting.page_screenshot_and_write()
            raise

    @allure.story("法律声明")
    @allure.title("{case_title}")
    @allure.step("开始执行用例")
    @pytest.mark.parametrize("case_title, page_title, toast", read_line("setting.txt", 1, 2))
    def test_law_statement(self, case_title, page_title, toast):
        try:
            self.setting.page_back()
            self.setting.page_click_law_statement()
            assert page_title in self.setting.page_get_page_title()
        except Exception:
            self.setting.page_screenshot_and_write()
            raise

    @allure.story("注销协议")
    @allure.title("{case_title}")
    @allure.step("开始执行用例")
    @pytest.mark.parametrize("case_title, page_title, toast", read_line("setting.txt", 2, 3))
    def test_cancel_notice(self, case_title, page_title, toast):
        try:
            self.setting.page_back()
            self.setting.page_back()
            self.setting.page_click_safe_center()
            self.setting.page_click_cancel_account()
            assert page_title in self.setting.page_get_page_title()
        except Exception:
            self.setting.page_screenshot_and_write()
            raise
        finally:
            self.setting.page_click_logoff()

    @allure.story("注销提示toast")
    @allure.title("{case_title}")
    @allure.step("开始执行用例")
    @pytest.mark.parametrize("case_title, code, toast", read_line("setting.txt", 3))
    def test_cancel_toast(self, case_title, code, toast):
        if toast:
            try:
                self.setting.page_input_code(code)
                self.setting.page_click_logoff_confirm()
                assert toast in self.setting.page_get_toast()
            except Exception:
                self.setting.page_screenshot_and_write()
                raise
