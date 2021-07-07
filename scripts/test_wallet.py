import pytest, sys, os, allure, time
sys.path.append(os.getcwd())
from base.get_data import read_line
from Page.page_in import PageIn


@allure.feature("钱包模块")
class TestWallet:

    def setup_class(self):
        self.wallet = PageIn().page_get_wallet()
        self.wallet.page_jump_advertisement()
        self.wallet.page_click_wallet()

    def teardown_class(self):
        self.wallet.page_logout()
        self.wallet.driver.quit()

    @allure.story("验证持卡人")
    @allure.title("{case_title}")
    @allure.step("开始执行用例")
    @pytest.mark.parametrize("case_title, username, password, cardholder", read_line("wallet.txt", end=1))
    def test_cardholder(self, case_title, username, password, cardholder):
        try:
            self.wallet.page_login(username, password)
            time.sleep(2)
            self.wallet.page_click_rb_wallet()
            time.sleep(10)
            self.wallet.page_click_bank_card()
            time.sleep(1)
            self.wallet.page_click_add_card()
            time.sleep(2)
            assert cardholder in self.wallet.page_get_cardholder()
        except Exception:
            self.wallet.page_screenshot_and_write()
            raise

    @allure.story("验证银行卡")
    @allure.title("{case_title}")
    @allure.step("开始执行用例")
    @pytest.mark.parametrize("case_title, card_number, bank, toast", read_line("wallet.txt", 1, 4))
    def test_bank_card(self, case_title, card_number, bank, toast):
        if toast:
            try:
                self.wallet.page_input_card_number(card_number)
                self.wallet.page_click_add_next()
                time.sleep(0.2)
                assert toast in self.wallet.page_get_error_toast()
            except Exception:
                self.wallet.page_screenshot_and_write()
                raise
        else:
            try:
                self.wallet.page_input_card_number(card_number)
                self.wallet.page_click_add_next()
                time.sleep(0.5)
                assert bank in self.wallet.page_get_card_type()
            except Exception:
                self.wallet.page_screenshot_and_write()
                raise
            finally:
                self.wallet.page_click_add_next()
                time.sleep(1)

    @allure.story("手机验证码")
    @allure.title("{case_title}")
    @allure.step("开始执行用例")
    @pytest.mark.parametrize("case_title, username, code, toast", read_line("wallet.txt", 4))
    def test_phone_code(self, case_title, username, code, toast):
        try:
            self.wallet.page_input_code(code)
            self.wallet.page_click_code_next()
            assert toast in self.wallet.page_get_error_toast()
        except Exception:
            self.wallet.page_screenshot_and_write()
            raise
