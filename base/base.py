from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep

class Base():
    def __init__(self, driver):
        self.driver=driver

    def base_find_element(self, loc, timeout=30, poll=0.5):
        sleep(0.3)
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(lambda x: x.find_element(*loc))

    def base_find_elements(self, loc, timeout=30, poll=0.5):
        sleep(0.3)
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(lambda x: x.find_elements(*loc))

    def base_click(self, loc):
        self.base_find_element(loc).click()

    def base_clicks(self, loc, num):
        self.base_find_elements(loc)[num].click()

    def base_input(self, loc, text):
        el = self.base_find_element(loc)
        el.clear()
        el.send_keys(text)

    def base_getImage(self):
        Path = "./Image/faild.png"
        self.driver.get_screenshot_as_file(Path)

    def base_get_toast(self, message):
        loc =(By.XPATH, "//*[contains(@text, '%s')]" %message)
        return self.base_find_element(loc, timeout=5, poll=0.1).text

    def base_get_text(self, loc, timeout=30, poll=0.5):
        return self.base_find_element(loc, timeout=timeout, poll=poll).text

    def base_get_texts(self, loc, num):
        return self.base_find_elements(loc)[num].text

    def base_drag_and_drop(self, el1, el2):
        self.driver.drag_and_drop(el1, el2)

    def base_text_click(self, text):
        loc = (By.XPATH, "//*[contains(@text, '%s')]" % text)
        self.base_find_element(loc).click()

    def base_switch_webview(self,):
        self.driver.switch_to.context(self.driver.contexts[-1])

    def base_switch_native(self):
        self.driver.switch_to.context(self.driver.contexts[0])

    def base_back(self):
        self.driver.back()

    def base_get_attribute(self, loc, value):
        return self.base_find_element(loc).get_attribute(value)
