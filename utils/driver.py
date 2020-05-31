from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class Driver:
    def __init__(self, wd):
        self.wd = wd

    def switch_iframe(self, iframe):
        try:
            self.wd.switch_to.frame(iframe)
            return True
        except TimeoutException:
            return False

    def scroll_to_center(self, element):
        js = "var viewPortHeight = Math.max(document.documentElement.clientHeight, window.innerHeight || 0);var elementTop = arguments[0].getBoundingClientRect().top;window.scrollBy(0, elementTop-(viewPortHeight/2));"
        self.wd.execute_script(js, element)

    def wait_find_by_text(self, text, time=4, tag=''):
        return WebDriverWait(self.wd, time).until(ec.visibility_of_element_located((
            By.XPATH, f"//{tag}[contains(text(), '{text}')]")))

    def wait_find_by_xpath(self, xpath, time=4):
        return WebDriverWait(self.wd, time).until(ec.visibility_of_element_located((
            By.XPATH, xpath)))

    def wait_find_by_id(self, xpath, time=4):
        return WebDriverWait(self.wd, time).until(ec.visibility_of_element_located((
            By.ID, xpath)))

    def wait_finds_by_xpath(self, xpath, time=4):
        WebDriverWait(self.wd, time).until(ec.visibility_of_element_located((By.XPATH, xpath)))
        return self.wd.find_elements_by_xpath(xpath)

    def open_tab(self):
        self.wd.execute_script('''window.open("about:blank", "_blank");''')

    def hide_element(self, el):
        self.wd.execute_script("arguments[0].style.display = 'none';", el)
