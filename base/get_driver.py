from appium import webdriver


# server 启动参数
def get_driver():
    desired_caps = {
        'platformName': 'Android',
        'platformVersion': '9',
        'deviceName': '8GP7N18523000526',
        'appPackage': 'io.cordova.hellocordovauat',
        'appActivity': '.activity.StartActivity',
        'automationName': 'Uiautomator2',
        'autoWebviewTimeout': 15000,
        # 'unicodeKeyboard': True,
        # 'resetKeyboard': True,
        'noReset': True,
    }

    # 声明driver对象
    return webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
