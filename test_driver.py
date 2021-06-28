from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

# server 启动参数

desired_caps = {
    'platformName':'Android',
    'platformVersion': '9',
    'deviceName':'8GP7N18523000526',
    # 'appPackage':'com.glgw.steeltrade',
    # 'appActivity':'com.glgw.steeltrade.mvp.ui.activity.SplashActivity',
    # 线上包
    # 'appPackage':'com.kwl.bhtapp',
    'appPackage':'io.cordova.hellocordovauat',
    'appActivity':'.activity.StartActivity',
    'automationName':'Uiautomator2',
    'autoWebviewTimeout':8000,
    # 'unicodeKeyboard': True,
    # 'resetKeyboard': True,
    'noReset':True,
}

# 声明driver对象
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
driver.implicitly_wait(8)
driver.find_element_by_id("io.cordova.hellocordovauat:id/cuttime").click()
# time.sleep(3)
driver.find_element_by_android_uiautomator('text("%s")' % "我的").click()
if len(driver.contexts) > 1:
    driver.switch_to.context(driver.contexts[-1])
    print("切换成功")
    print(driver.current_context)
    time.sleep(2)
    # driver.find_element_by_id("username").clear()
    # driver.find_element_by_id("username").send_keys(13439200080)
    # print("输入用户名")
    # time.sleep(1)
    # driver.find_element_by_id("password").send_keys("qwer1234")
    # print("输入密码")
    # time.sleep(1)
    # driver.find_element_by_css_selector(".am-button.am-button-primary").click()
    # print("点击登录")
    # time.sleep(2)
    # print(driver.find_element_by_xpath(".//*[@id='app-root']/div/div[4]/div[2]"))
    # driver.find_element_by_xpath(".//*[@id='app-root']/div/div[4]/div[2]").click()
    # print(driver.find_element_by_link_text("用户注册").text)
    # # print(driver.find_elements_by_css_selector("[aria-disabled='false']").text)
    # driver.find_element_by_css_selector("[aria-disabled='false']").click()
    # time.sleep(2)
    # driver.find_element_by_id("phone").send_keys(13439200061)
    # print(driver.find_element_by_id("smsCode").get_attribute('value'))
    # driver.find_element_by_css_selector("[data-name='smsRemainSecond']").click()
    # print(driver.find_element_by_xpath(".//*[@id='app-root']/div/div[2]/div/div[2]/div[2]/div[2]/div[2]/div[1]").text)
    # driver.find_element_by_xpath(".//*[@id='app-root']/div/div[2]/div/div[2]/div[7]").click()
    # print("设置")
    # time.sleep(2)
    # driver.find_element_by_css_selector(".am-button").click()
    # print("退出")
    # time.sleep(2)
    # driver.find_elements_by_css_selector(".am-modal-button")[1].click()

    # driver.find_element_by_link_text("用户注册").click()
    # time.sleep(4)
    # el = driver.find_elements_by_css_selector('.am-radio')
    # print(len(el))
    # el[0].click()
    # time.sleep(2)
    # print(driver.window_handles)
    # driver.find_element_by_link_text("确定").click()
    # time.sleep(1)
    # driver.switch_to.context(driver.contexts[0])
    # for i in range(15):
    #     TouchAction(driver).press(x=500, y=1900).move_to(x=0, y=-2000).release().perform()
    #     # time.sleep(0.1)
    #
    # time.sleep(1)
    # # btn = driver.find_element_by_css_selector(".am-button.am-button-primary>span")
    # # driver.execute_script("arguments[0].click();", btn)
    # TouchAction(driver).press(x=300, y=1950).release().perform()
    # driver.switch_to.context(driver.contexts[1])

    # 注销账号
    # driver.find_element_by_xpath(".//*[@id='app-root']/div/div[2]/div/div[2]/div[7]").click()
    # time.sleep(1)
    # driver.find_elements_by_css_selector(".am-list-content")[-2].click()
    # time.sleep(1)
    # driver.find_element_by_css_selector(".am-list-content").click()
    # driver.find_element_by_css_selector(".am-button.am-button-primary").click()
    # time.sleep(1)
    # driver.find_element_by_css_selector('[data-name="smsRemainSecond"]').click()

    # 钱包
    # driver.find_element_by_xpath(".//*[@id='app-root']/div/div[2]/div/div[2]/div[2]/div/div/div[2]").click()
    # time.sleep(7)
    # driver.find_element_by_css_selector('[href="#/wallet/bankcards/wallet_gd"]').click()
    # time.sleep(2)
    # driver.find_element_by_css_selector('[href="#/wallet/bankcards/wallet_gd/add"]').click()
    # time.sleep(2)
    # e = driver.find_element_by_css_selector('[name="name"]')
    # print(e.get_attribute("value"))
    # driver.find_element_by_css_selector('[name="bankCard"]').send_keys("6228480039046662779")
    # driver.find_element_by_css_selector(".am-button.am-button-primary").click()
    # time.sleep(2)
    # driver.find_element_by_css_selector(".am-button.am-button-primary").click()
    # driver.find_element_by_css_selector('[data-name="smsRemainSecond"]').click()
    # time.sleep(1)
    # driver.find_element_by_css_selector(".am-button.am-button-primary")

    # 基本资料
    driver.find_element_by_xpath(".//*[@id='app-root']/div/div[2]/div/div[2]/div[3]").click()
    time.sleep(1)
    e = driver.find_elements_by_css_selector(".am-list-line")
    print(len(e))
    e[1].click()

else:
    print("切换失败")
    print(driver.current_context)


time.sleep(15)
driver.quit()
