from base.get_driver import get_driver
from Page.page_login import PageLogin
from Page.page_register import PageRegister
from Page.page_home import PageHome
from Page.page_video import PageVideo
from Page.page_change_pwd import PagePwd
from Page.page_setting import PageSetting
from Page.page_wallet import PageWallet
from Page.page_information import PageInformation

# 获取driver
class PageIn():

    def page_get_pagelogin(self):
        return PageLogin(get_driver())

    def page_get_register(self):
        return PageRegister(get_driver())

    def page_get_home(self):
        return PageHome(get_driver())

    def page_get_video(self):
        return PageVideo(get_driver())

    def page_get_password(self):
        return PagePwd(get_driver())

    def page_get_setting(self):
        return PageSetting(get_driver())

    def page_get_wallet(self):
        return PageWallet(get_driver())

    def page_get_information(self):
        return PageInformation(get_driver())
