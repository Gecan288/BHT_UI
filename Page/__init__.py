from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By

# 首页
advertisement = By.ID, "io.cordova.hellocordovauat:id/cuttime"
navigation_me = MobileBy.ANDROID_UIAUTOMATOR, 'text("%s")' % "我的"
navigation_me_xpath = By.XPATH,
navigation_home = MobileBy.ANDROID_UIAUTOMATOR, 'text("%s")' % "首页"
navigation_mall = MobileBy.ANDROID_UIAUTOMATOR, 'text("%s")' % "商城"
navigation_video = By.XPATH, ".//*[@id='app-root']/div/div[4]/div[2]"
navigation_wallet = MobileBy.ANDROID_UIAUTOMATOR, 'text("%s")' % "钱包"
home_authentication = By.XPATH, ".//*[@id='app-root']/div/div/div[2]/div/div[2]/div[3]/div[1]"
home_organization = By.XPATH, ".//*[@id='app-root']/div/div/div[2]/div/div[2]/div[3]/div[2]"
home_wallet = By.XPATH, ".//*[@id='app-root']/div/div/div[2]/div/div[2]/div[3]/div[3]"
home_toast = By.CSS_SELECTOR, '[role="alert"]'
page_title = By.CSS_SELECTOR, ".am-navbar-title"

# 登录页面
login_input_username = By.ID, "username"
login_input_password = By.ID, "password"
login_login_btn = By.CSS_SELECTOR, ".am-button.am-button-primary"
login_error_toast = By.CSS_SELECTOR, '[role="alert"]'
login_type_code = By.CSS_SELECTOR, '[aria-disabled="false"]'
login_input_phone = By.ID, "phone"
login_input_code = By.ID, "smsCode"
login_get_code = By.CSS_SELECTOR, '[data-name="smsRemainSecond"]'
login_user_register = By.LINK_TEXT, "用户注册"
login_forget_password = By.PARTIAL_LINK_TEXT, "忘记密码"

# 注册页面
register_input_phone = By.ID, "phone"
register_input_password = By.ID, "password"
register_input_code = By.ID, "smsCode"
register_get_code = By.CSS_SELECTOR, '[data-name="smsRemainSecond"]'
register_register_btn = By.CSS_SELECTOR, ".am-button.am-button-primary"
register_error_toast = By.CSS_SELECTOR, '[role="alert"]'
register_agreement = By.CSS_SELECTOR, '[type="radio"]'
register_agreement_tips = By.LINK_TEXT, "确定"
register_agreement_agree = By.CSS_SELECTOR, ".am-button.am-button-primary"

# 我的页面
me_nikename = By.XPATH, ".//*[@id='app-root']/div/div[2]/div/div[2]/div[2]/div[2]/div[2]/div[1]"
me_information = By.XPATH, ".//*[@id='app-root']/div/div[2]/div/div[2]/div[3]"
me_authentication = By.XPATH, ".//*[@id='app-root']/div/div[2]/div/div[2]/div[4]"
me_online_service = By.XPATH, ".//*[@id='app-root']/div/div[2]/div/div[2]/div[5]"
me_service_tel = By.XPATH, ".//*[@id='app-root']/div/div[2]/div/div[2]/div[6]"
me_setting = By.XPATH, ".//*[@id='app-root']/div/div[2]/div/div[2]/div[7]"

# 基本资料


# 设置页面
set_logout = By.CSS_SELECTOR, ".am-button"
set_about = By.CSS_SELECTOR, ".am-list-content"   # -1
set_logout_ok = By.LINK_TEXT, "确定"
set_safe_center = By.CSS_SELECTOR, ".am-list-content"   # -2
set_change_password = By.CSS_SELECTOR, ".am-list-content"   # 0
set_tips_forget_password = By.CSS_SELECTOR, '[role="button"]'   # -2
set_tips_remember_password = By.CSS_SELECTOR, '[role="button"]'   # -1
about_bht_introduction = By.CSS_SELECTOR, ".am-list-content"   # 0  法律声明 -1
safe_center_cancel_account = By.CSS_SELECTOR, ".am-list-content"
cancel_account_logoff_btn = By.CSS_SELECTOR, ".am-button.am-button-primary"
logoff_confirm = By.CSS_SELECTOR, ".am-button.am-button-primary.am-button-small.am-button-inline"  # 0
logoff_cancel = By.CSS_SELECTOR, ".am-button.am-button-primary.am-button-small.am-button-inline"   # -1
logoff_input_code = By.CSS_SELECTOR, '[type="text"]'
logoff_get_code = By.CSS_SELECTOR, '[data-name="smsRemainSecond"]'
logoff_toast = By.CSS_SELECTOR, '[role="alert"]'

# 修改密码
change_password_old = By.CSS_SELECTOR, '[name="originalPassword"]'
change_password_new = By.CSS_SELECTOR, '[name="newPassword"]'
change_password_confirm = By.CSS_SELECTOR, '[name="surePassword"]'
change_password_btn = By.CSS_SELECTOR, ".am-button.am-button-primary"
change_password_toast = By.CSS_SELECTOR, '[role="alert"]'
forget_password_phone = By.ID, "phone"
forget_password_code = By.ID, "smsCode"
forget_password_get_code = By.CSS_SELECTOR, '[data-name="smsRemainSecond"]'
forget_password_password = By.ID, "password"
forget_password_toast = By.CSS_SELECTOR, '[role="alert"]'

# 综合视频
video_tips_jump = By.LINK_TEXT, "跳过"
video_tips_authentication = By.LINK_TEXT, "去认证"
authentication_title = By.CSS_SELECTOR, ".am-navbar-title"

# 钱包
wallet_rb_wallet = By.XPATH, ".//*[@id='app-root']/div/div[2]/div/div[2]/div[2]/div/div/div[2]"
wallet_bank_card = By.CSS_SELECTOR, '[href="#/wallet/bankcards/wallet_gd"]'
bank_card_add = By.CSS_SELECTOR, '[href="#/wallet/bankcards/wallet_gd/add"]'
add_card_input_number = By.CSS_SELECTOR, '[name="bankCard"]'
add_card_next = By.CSS_SELECTOR, ".am-button.am-button-primary"
add_card_get_code = By.CSS_SELECTOR, '[data-name="smsRemainSecond"]'
add_card_input_code = By.CSS_SELECTOR, '[name="smsCode"]'
add_card_code_next = By.CSS_SELECTOR, ".am-button.am-button-primary"
wallet_toast = By.CSS_SELECTOR, '[role="alert"]'
add_card_cardholder = By.CSS_SELECTOR, '[name="name"]'
add_card_type = By.CSS_SELECTOR, '[name="bankAndCardType"]'
