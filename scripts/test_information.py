import pytest, sys, os, allure, time
sys.path.append(os.getcwd())
from base.get_data import read_line
from Page.page_in import PageIn

@allure.feature("基本资料模块")
class TestInformation():

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
    @allure.title("验证修改昵称提示")
    @allure.step("开始执行用例")
    @pytest.mark.parametrize("nike_name, toast", read_line("information.txt", end=3))
    def test_change_nike_name(self, nike_name, toast):
        if toast:
            try:
                self.information.page_input_new_name(nike_name)
                self.information.page_click_confirm_btn()
                assert toast in self.information.page_get_toast()
            except:
                self.information.page_screenshot_and_write()
        else:
            if nike_name in self.information.page_get_old_value():
                pass
            else:
                try:
                    self.information.page_input_new_name(nike_name)
                    self.information.page_click_confirm_btn()
                    time.sleep(1)
                    assert nike_name in self.information.page_get_new_name()
                except:
                    self.information.page_screenshot_and_write()
                finally:
                    self.information.page_click_email()

    @allure.story("修改邮箱")
    @allure.title("验证修改邮箱提示")
    @allure.step("开始执行用例")
    @pytest.mark.parametrize("email, toast, title", read_line("information.txt", 3, 7))
    def test_change_email(self, email, toast, title):
        if toast:
            try:
                self.information.page_input_new_email(email)
                self.information.page_click_confirm_btn()
                assert toast in self.information.page_get_toast()
            except:
                self.information.page_screenshot_and_write()
        else:
            if email in self.information.page_get_old_value():
                pass
            else:
                try:
                    self.information.page_input_new_email(email)
                    self.information.page_click_confirm_btn()
                    time.sleep(1)
                    assert email in self.information.page_get_new_email()
                except:
                    self.information.page_screenshot_and_write()
                finally:
                    self.information.page_click_phone()

    @allure.story("修改手机号")
    @allure.title("身份验证")
    @allure.step("开始执行用例")
    @pytest.mark.parametrize("pwd, toast, title", read_line("information.txt", 7, 10))
    def test_check_identity(self, pwd, toast, title):
        if toast:
            try:
                self.information.page_input_password(pwd)
                self.information.page_click_confirm_btn()
                assert toast in self.information.page_get_toast()
            except:
                self.information.page_screenshot_and_write()
        else:
            try:
                self.information.page_input_password(pwd)
                self.information.page_click_confirm_btn()
                assert title in self.information.page_get_page_title()
            except:
                self.information.page_screenshot_and_write()

    @allure.story("修改手机号")
    @allure.title("验证手机号和验证码")
    @allure.step("开始执行用例")
    @pytest.mark.parametrize("phone, code, toast", read_line("information.txt", 10, 16))
    def test_change_phone(self, phone, code, toast):
        if code:
            try:
                self.information.page_input_new_phone(phone)
                self.information.page_input_code(code)
                self.information.page_click_confirm_btn()
                assert toast in self.information.page_get_toast()
            except:
                self.information.page_screenshot_and_write()
        else:
            try:
                self.information.page_input_new_phone(phone)
                self.information.page_get_code()
                self.information.page_click_confirm_btn()
                assert toast in self.information.page_get_page_title()
            except:
                self.information.page_screenshot_and_write()
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
