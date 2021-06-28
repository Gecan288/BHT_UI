import pytest, sys, os, allure, time
sys.path.append(os.getcwd())
from base.get_data import read_txt
from Page.page_in import PageIn

@allure.feature("修改密码模块")
class TestChangePdw():

    def setup_class(self):
        self.change = PageIn().page_get_password()
        self.change.page_jump_advertisement()
        self.change.page_click_me()
        self.change.page_login()
        time.sleep(2)
        self.change.page_click_setting()
        self.change.page_click_change_password()
        self.change.page_click_remember()

    def teardown_class(self):
        self.change.driver.quit()

    @allure.story("使用原密码")
    @allure.title("验证密码规则")
    @allure.step("开始执行修改密码用例")
    @pytest.mark.parametrize("old_pwd, new_pwd, confirm_pwd, expect_toast",read_txt("changePwd.txt"))
    def test_change_pwd(self, old_pwd, new_pwd, confirm_pwd, expect_toast):
        if expect_toast:
            try:
                self.change.page_input_old_password(old_pwd)
                self.change.page_input_new_password(new_pwd)
                self.change.page_input_confirm_password(confirm_pwd)
                self.change.page_click_change()
                assert expect_toast in self.change.page_get_toast()
            except:
                self.change.page_getImage()
                self.change.page_write_to_report()
                raise
        else:
            try:
                self.change.page_input_old_password(old_pwd)
                self.change.page_input_new_password(new_pwd)
                self.change.page_input_confirm_password(confirm_pwd)
                self.change.page_click_change()
                time.sleep(3)
                assert "登录" in self.change.page_get_page_title()
            except:
                self.change.page_getImage()
                self.change.page_write_to_report()
                raise
            finally:
                self.change.page_click_forget_password()

    @allure.story("忘记密码")
    @allure.title("验证密码规则")
    @allure.step("开始执行忘记密码用例")
    @pytest.mark.parametrize("phone, code, password, expect_toast", read_txt("forgetPwd.txt"))
    def test_forget_pwd(self, phone, code, password, expect_toast):
        if phone:
            if expect_toast:
                try:
                    self.change.page_input_phone(phone)
                    self.change.page_input_code(code)
                    self.change.page_input_password(password)
                    self.change.page_click_change()
                    assert expect_toast in self.change.page_get_toast()
                except:
                    self.change.page_getImage()
                    self.change.page_write_to_report()
                    raise
            else:
                try:
                    self.change.page_input_phone(phone)
                    self.change.page_get_code()
                    self.change.page_input_password(password)
                    self.change.page_click_change()
                    assert "登录" in self.change.page_get_page_title()
                except:
                    self.change.page_getImage()
                    self.change.page_write_to_report()
                    raise
                finally:
                    self.change.page_login()
                    time.sleep(2)
                    self.change.page_click_setting()
                    self.change.page_click_change_password()
                    self.change.page_click_forget()
        else:
            if expect_toast:
                try:
                    self.change.page_input_code(code)
                    self.change.page_input_password(password)
                    self.change.page_click_change()
                    assert expect_toast in self.change.page_get_toast()
                except:
                    self.change.page_getImage()
                    self.change.page_write_to_report()
                    raise
            else:
                try:
                    self.change.page_get_code()
                    self.change.page_input_password(password)
                    time.sleep(0.5)
                    self.change.page_click_change()
                    assert "登录" in self.change.page_get_page_title()
                    time.sleep(2)
                except:
                    self.change.page_getImage()
                    self.change.page_write_to_report()
                    raise
