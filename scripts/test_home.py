import pytest, sys, os, allure, time
sys.path.append(os.getcwd())
from base.get_data import read_line
from Page.page_in import PageIn


@allure.feature("首页模块")
class TestHome:

    def setup_class(self):
        self.home = PageIn().page_get_home()
        self.home.page_jump_advertisement()

    def teardown_class(self):
        self.home.driver.quit()

    @allure.story("用户未登录")
    @allure.title("{case_title}")
    @allure.step("开始执行用例")
    @pytest.mark.parametrize("case_title, username, password, home_toast, page_title", read_line("home.txt", end=1))
    def test_not_login(self, case_title, username, password, home_toast, page_title):
        try:
            self.home.page_click_home_authentication()
            assert home_toast in self.home.page_get_toast()
        except Exception:
            self.home.page_screenshot_and_write()
            raise
        finally:
            time.sleep(3)
        try:
            self.home.page_click_home_organization()
            assert home_toast in self.home.page_get_toast()
        except Exception:
            self.home.page_screenshot_and_write()
            raise
        finally:
            time.sleep(3)

    @allure.story("用户登录")
    @allure.title("{case_title}")
    @allure.step("开始执行用例")
    @pytest.mark.parametrize("case_title, username, password, page_title, wallet_title", read_line("home.txt", 1))
    def test_user_login(self, case_title, username, password, page_title, wallet_title):
        try:
            self.home.page_click_home()
            self.home.page_login(username, password)
            self.home.page_click_home_organization()
            assert page_title in self.home.page_get_title()
        except Exception:
            self.home.page_screenshot_and_write()
            raise
        try:
            self.home.page_click_home_wallet()
            assert wallet_title in self.home.page_get_title()
        except Exception:
            self.home.page_screenshot_and_write()
            raise
        finally:
            time.sleep(8)
            self.home.page_click_me()
            self.home.page_logout()
