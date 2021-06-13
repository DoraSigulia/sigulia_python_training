# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest

class TestAddNewAddress(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
    
    def test_add_new_address(self):
        driver = self.driver
        driver.get("http://localhost/addressbook/")
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys("admin")
        driver.find_element_by_name("pass").clear()
        driver.find_element_by_name("pass").send_keys("secret")
        driver.find_element_by_xpath("//input[@value='Login']").click()
        driver.find_element_by_link_text("add new").click()
        driver.find_element_by_name("firstname").clear()
        driver.find_element_by_name("firstname").send_keys("Ivan")
        driver.find_element_by_name("middlename").clear()
        driver.find_element_by_name("middlename").send_keys("Peter")
        driver.find_element_by_name("lastname").clear()
        driver.find_element_by_name("lastname").send_keys("Ivanov")
        driver.find_element_by_name("nickname").clear()
        driver.find_element_by_name("nickname").send_keys("admin911")
        driver.find_element_by_name("title").clear()
        driver.find_element_by_name("title").send_keys("test")
        driver.find_element_by_name("company").clear()
        driver.find_element_by_name("company").send_keys("OOO \"LM\"")
        driver.find_element_by_name("address").clear()
        driver.find_element_by_name("address").send_keys("Lenina, 1")
        driver.find_element_by_name("home").clear()
        driver.find_element_by_name("home").send_keys("2894523")
        driver.find_element_by_name("mobile").clear()
        driver.find_element_by_name("mobile").send_keys("8951456789")
        driver.find_element_by_name("work").clear()
        driver.find_element_by_name("work").send_keys("89634567823")
        driver.find_element_by_name("email").clear()
        driver.find_element_by_name("email").send_keys("aaa@gmail.com")
        driver.find_element_by_name("email2").clear()
        driver.find_element_by_name("email2").send_keys("bbb@mail.ru")
        driver.find_element_by_name("bday").click()
        Select(driver.find_element_by_name("bday")).select_by_visible_text("1")
        driver.find_element_by_xpath("//option[@value='1']").click()
        driver.find_element_by_name("bmonth").click()
        Select(driver.find_element_by_name("bmonth")).select_by_visible_text("July")
        driver.find_element_by_xpath("//option[@value='July']").click()
        driver.find_element_by_name("byear").clear()
        driver.find_element_by_name("byear").send_keys("1995")
        driver.find_element_by_name("aday").click()
        Select(driver.find_element_by_name("aday")).select_by_visible_text("1")
        driver.find_element_by_xpath("(//option[@value='1'])[2]").click()
        driver.find_element_by_name("amonth").click()
        Select(driver.find_element_by_name("amonth")).select_by_visible_text("July")
        driver.find_element_by_xpath("(//option[@value='July'])[2]").click()
        driver.find_element_by_name("ayear").clear()
        driver.find_element_by_name("ayear").send_keys("2025")
        driver.find_element_by_name("address2").clear()
        driver.find_element_by_name("address2").send_keys("Lenina,1")
        driver.find_element_by_name("phone2").clear()
        driver.find_element_by_name("phone2").send_keys("Lenina,2")
        driver.find_element_by_name("notes").clear()
        driver.find_element_by_name("notes").send_keys("test")
        driver.find_element_by_xpath("(//input[@value=\"Enter\"])[2]").click()
        driver.find_element_by_link_text("home page").click()
        driver.find_element_by_link_text("Logout").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
