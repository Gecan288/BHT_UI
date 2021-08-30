import pytest, sys, os, allure, time
sys.path.append(os.getcwd())
from base.get_data import read_txt
from Page.page_in import PageIn


@allure.feature("登录模块")
class TestLogin:

    def setup_class(self):
        self.login = PageIn().page_get_pagelogin()
        self.login.page_jump_advertisement()
        self.login.page_click_me()

    def teardown_class(self):
        self.login.driver.quit()

    @allure.story("密码登录")
    @allure.title("{case_title}")
    @allure.step("开始执行密码登录用例")
    @pytest.mark.parametrize("case_title, username, password, nike_name, login_toast", read_txt("loginPwd.txt"))
    def test_password_login(self, case_title, username, password, nike_name, login_toast):
        if nike_name:
            try:
                self.login.page_input_username(username)
                self.login.page_input_password(password)
                self.login.page_click_login_btn()
                time.sleep(2)
                assert nike_name in self.login.page_get_nikename()
            except Exception:
                self.login.page_screenshot_and_write()
                raise
            finally:
                self.login.page_logout()
                self.login.page_click_login_type()
        else:
            try:
                self.login.page_input_username(username)
                self.login.page_input_password(password)
                self.login.page_click_login_btn()
                assert login_toast in self.login.page_get_error_toast()
            except Exception:
                self.login.page_screenshot_and_write()
                raise

    @allure.story('验证码登录')
    @allure.title("{case_title}")
    @allure.step("开始执行验证码登录用例")
    @pytest.mark.parametrize("case_title, phone, code, login_toast, code_toast", read_txt("loginCode.txt"))
    def test_code_login(self, case_title, phone, code, login_toast, code_toast):
        if login_toast:
            try:
                self.login.page_input_phone(phone)
                self.login.page_input_code(code)
                self.login.page_click_login_btn()
                assert login_toast in self.login.page_get_error_toast()
            except Exception:
                self.login.page_screenshot_and_write()
                raise

        elif code_toast:
            try:
                self.login.page_input_phone(phone)
                self.login.page_get_code()
                assert code_toast in self.login.page_get_error_toast()
            except Exception:
                self.login.page_screenshot_and_write()
                raise
            time.sleep(10)
        else:
            try:
                self.login.page_input_phone(phone)
                self.login.page_get_code()
                time.sleep(1)
                self.login.page_click_login_btn()
                time.sleep(2)
                assert "止水" in self.login.page_get_nikename()
            except Exception:
                self.login.page_screenshot_and_write()
                raise
            finally:
                self.login.page_logout()
