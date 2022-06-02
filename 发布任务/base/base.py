import time

from selenium.webdriver.support.wait import WebDriverWait


class Base:
    def __init__(self, driver):
        self.driver = driver

    def base_find_element(self, loc, timeout=30, poll=0.5):
        return WebDriverWait(driver=self.driver,timeout=timeout,poll_frequency=poll).until(lambda x:x.find_element(*loc))

    def base_click(self, loc):
        self.base_find_element(loc).click()

    def base_input(self, loc, value):
        ul = self.base_find_element(loc)
        ul.clear()
        ul.send_keys(value)

    def base_get_text(self, loc):
        return self.base_find_element(loc).text

    def base_if_success(self, loc):
        try:
            self.base_find_element(loc, timeout=2)
            return True
        except:
            return False

    def base_get_image(self):
        self.driver.get_screenshot_as_file("./{}.png".format(time.strftime("%Y_%m_%d_%H_%M_%S")))
