# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Application:
    def __init__(self, browser, base_url):
        if browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser %s" %browser)
        self.base_url = base_url

    def open_partner_page(self):
        wd = self.wd
        wd.get(self.base_url)

    def destroy(self):
        self.wd.quit()

    def add_partner_information(self, partner):
        wd = self.wd
        element_cookie = wd.find_element(By.CSS_SELECTOR, ".cookieBtn > span")
        if element_cookie.is_displayed():
            element_cookie.click()
            wd.implicitly_wait(5)
        wd.find_element(By.LINK_TEXT, "СТАТЬ ПАРТНЕРОМ").click()
        wd.find_element(By.NAME, "phone").send_keys(partner.phone)
        wd.find_element(By.NAME, "name").send_keys(partner.name)
        wd.find_element(By.NAME, "email").send_keys(partner.email)
        wd.find_element(By.NAME, "message").send_keys(partner.question)
        wd.execute_script('document.getElementsByName("politics")[0].click()')

    def send_partner_information(self):
        wd = self.wd
        try:
            element = WebDriverWait(wd, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.f-action span')))
            element.click()
            wd.implicitly_wait(20)
            return u'element is clickable'
        except Exception:
            return u"element is not clickable"
