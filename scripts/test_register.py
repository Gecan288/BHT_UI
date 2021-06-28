import pytest, sys, os, allure, time
sys.path.append(os.getcwd())
from base.get_data import read_txt
from Page.page_in import PageIn

@allure.feature("注册模块")
class TestRegister():

    def setup_class(self):
        self.register = PageIn().page_get_register()
        self.register.page_jump_advertisement()
        self.register.page_click_me()
        self.register.page_click_user_register()

    def teardown_class(self):
        self.register.driver.quit()

    @allure.story("用户注册")
    @allure.title("验证注册提示")
    @allure.step("开始执行注册用例")
    @pytest.mark.parametrize("phone, password, code, except_toast, toast", read_txt("register.txt"))
    def test_register(self, phone, password, code, except_toast, toast):
        if except_toast:
            try:
                self.register.page_input_phone(phone)
                self.register.page_input_password(password)
                self.register.page_input_code(code)
                self.register.page_click_register_btn()
                assert except_toast in self.register.page_get_toast()
            except:
                self.register.page_getImage()
                self.register.page_write_to_report()
                raise
        elif toast:
            try:
                self.register.page_input_phone(phone)
                self.register.page_input_password(password)
                self.register.page_get_code()
                time.sleep(2)
                self.register.page_click_register_btn()
                assert toast in self.register.page_get_toast()
            except:
                self.register.page_getImage()
                self.register.page_write_to_report()
                raise
        else:
            try:
                self.register.page_input_phone(phone)
                self.register.page_input_password(password)
                self.register.page_click_register_btn()
                assert code in self.register.page_get_toast()
            except:
                self.register.page_getImage()
                self.register.page_write_to_report()
                raise
            finally:
                self.register.page_click_mall_agreement()
                self.register.page_read_agreement_agree()
                self.register.page_click_privacy_agreement()
                self.register.page_read_agreement_agree()
                self.register.page_click_video_agreement()
                self.register.page_read_agreement_agree()
