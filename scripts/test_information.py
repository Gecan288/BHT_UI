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
    @pytest.mark.parametrize("nike_name, toast", read_line("information.txt", end=1))
    def test_change_name(self, nike_name, toast):
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
                except:
                    self.information.page_screenshot_and_write()
                finally:
                    time.sleep(1)

