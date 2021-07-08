import pytest, sys, os, allure, time
sys.path.append(os.getcwd())
from base.get_data import read_line
from Page.page_in import PageIn


@allure.feature("基本资料模块")
class TestInformation:

    def setup_class(self):
        self.information = PageIn().page_get_information()
        self.information.page_jump_advertisement()
        self.information.page_click_me()
        self.information.page_login()
        self.information.page_click_information()
        self.information.page_click_nikename()

    def teardown_class(self):
        self.information.driver.quit()

    @allure.story("修改昵称")
    @allure.title("{case_title}")
    @allure.step("开始执行用例")
    @pytest.mark.parametrize("case_title, nick_name, toast, alternate", read_line("information.txt", end=2))
    def test_change_nick_name(self, case_title, nick_name, toast, alternate):
        if toast:
            try:
                self.information.page_input_new_name(nick_name)
                self.information.page_click_confirm_btn()
                assert toast in self.information.page_get_toast()
            except Exception:
                self.information.page_screenshot_and_write()
                raise
        else:
            if nick_name in self.information.page_get_old_value():
                nick_name = alternate
            else:
                pass
            try:
                self.information.page_input_new_name(nick_name)
                self.information.page_click_confirm_btn()
                time.sleep(1)
                assert nick_name in self.information.page_get_new_name()
            except Exception:
                self.information.page_screenshot_and_write()
                raise
            finally:
                self.information.page_click_email()

    @allure.story("修改邮箱")
    @allure.title("{case_title}")
    @allure.step("开始执行用例")
    @pytest.mark.parametrize("case_title, email, toast, alternate", read_line("information.txt", 2, 5))
    def test_change_email(self, case_title, email, toast, alternate):
        if toast:
            try:
                self.information.page_input_new_email(email)
                self.information.page_click_confirm_btn()
                assert toast in self.information.page_get_toast()
            except Exception:
                self.information.page_screenshot_and_write()
                raise
        else:
            if email in self.information.page_get_old_value():
                email = alternate
            else:
                pass
            try:
                self.information.page_input_new_email(email)
                time.sleep(1)
                self.information.page_click_confirm_btn()
                time.sleep(1)
                assert email in self.information.page_get_new_email()
            except Exception:
                self.information.page_screenshot_and_write()
                raise
            finally:
                self.information.page_click_phone()

    @allure.story("修改手机号")
    @allure.title("{case_title}")
    @allure.step("开始执行用例")
    @pytest.mark.parametrize("case_title, pwd, toast, title", read_line("information.txt", 5, 8))
    def test_check_identity(self, case_title, pwd, toast, title):
        if toast:
            try:
                self.information.page_input_password(pwd)
                self.information.page_click_confirm_btn()
                assert toast in self.information.page_get_toast()
            except Exception:
                self.information.page_screenshot_and_write()
                raise
            finally:
                time.sleep(1)
        else:
            try:
                self.information.page_input_password(pwd)
                self.information.page_click_confirm_btn()
                assert title in self.information.page_get_page_title()
            except Exception:
                self.information.page_screenshot_and_write()
                raise
            finally:
                time.sleep(1)

    @allure.story("修改手机号")
    @allure.title("{case_title}")
    @allure.step("开始执行用例")
    @pytest.mark.parametrize("case_title, phone, code, toast", read_line("information.txt", 8))
    def test_change_phone(self, case_title, phone, code, toast):
        if code == '1':
            try:
                self.information.page_input_new_phone(phone)
                self.information.page_get_code()
                self.information.page_click_confirm_btn()
                assert toast in self.information.page_get_page_title()
            except Exception:
                self.information.page_screenshot_and_write()
                raise
            finally:
                self.information.page_login(phone)
                self.information.page_click_information()
                self.information.page_click_phone()
                self.information.page_input_password()
                self.information.page_click_confirm_btn()
                self.information.page_input_new_phone()
                self.information.page_get_code()
                self.information.page_click_confirm_btn()
                time.sleep(3)
        else:
            try:
                self.information.page_input_new_phone(phone)
                self.information.page_input_code(code)
                self.information.page_click_confirm_btn()
                assert toast in self.information.page_get_toast()
            except Exception:
                self.information.page_screenshot_and_write()
                raise
