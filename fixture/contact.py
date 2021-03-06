import re

from selenium.webdriver.support.ui import Select
from model.contact import Contact

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def add(self, contact):
        wd = self.app.wd
        self.open_contact_page()
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        wd.find_element_by_xpath('(//input[@value="Enter"])[2]').click()
        self.return_home_page()
        self.contact_cache = None

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.homephone)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("work", contact.workphone)
        self.change_field_value("email", contact.email1)
        self.change_field_value("email2", contact.email2)
        self.change_field_value_select("bday", contact.bday)
        self.change_field_value_select("bmonth", contact.bmonth)
        self.change_field_value("byear", contact.byear)
        self.change_field_value_select("aday", contact.aday)
        self.change_field_value_select("amonth", contact.amonth)
        self.change_field_value("ayear", contact.ayear)
        self.change_field_value("address2", contact.address2)
        self.change_field_value("phone2", contact.phone2)
        self.change_field_value("notes", contact.notes)

    def change_field_value_select(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            Select(wd.find_element_by_name(field_name)).select_by_visible_text(text)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def open_contact_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/") and len(wd.find_elements_by_name("MainForm")) > 0):
            wd.find_element_by_link_text("home").click()

    def return_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/") and len(wd.find_elements_by_name("MainForm")) > 0):
            wd.find_element_by_link_text("home page").click()

    def del_first_contact(self):
        self.del_contact_by_index(0)

    def del_contact_by_index(self, index):
        wd = self.app.wd
        self.open_contact_page()
        self.select_contact_by_index(index)
        wd.find_element_by_css_selector('input[value="Delete"]').click()
        wd.switch_to_alert().accept()
        wd.find_element_by_css_selector('div.msgbox')
        self.contact_cache = None

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def count(self):
        wd = self.app.wd
        self.open_contact_page()
        return len(wd.find_elements_by_name("selected[]"))

    def modify_first_contact(self):
        self.modify_contact_by_index(0)

    def modify_contact_by_index(self,new_contact_form, index):
        wd = self.app.wd
        self.open_contact_page()
        self.select_modify_contact_by_index(index)
        self.fill_contact_form(new_contact_form)
        wd.find_element_by_xpath("(//input[@value='Update'])[2]").click()
        self.return_home_page()
        self.contact_cache = None

    def select_modify_contact_by_index(self, index):
        wd = self.app.wd
        self.open_contact_page()
        wd.find_elements_by_css_selector('img[title="Edit"]')[index].click()

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_contact_page()
            self.contact_cache = []
            for element in wd.find_elements_by_name("entry"):
                cells = element.find_elements_by_css_selector('td')
                firstname = cells[2].text
                lastname = cells[1].text
                id = cells[0].find_element_by_name("selected[]").get_attribute('value')
                all_phones = cells[5].text
                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, id=id,
                                                  all_phones=all_phones))
        return list(self.contact_cache)


    def get_contact_from_edit_page(self, index):
        wd = self.app.wd
        self.select_modify_contact_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobile = wd.find_element_by_name("mobile").get_attribute("value")
        phone2 = wd.find_element_by_name("phone2").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname,id=id,
                       homephone=homephone, workphone=workphone,
                       mobile=mobile,phone2=phone2)

    def open_veiw_page_by_index(self, index):
        wd = self.app.wd
        self.open_contact_page()
        wd.find_elements_by_css_selector('img[title="Details"]')[index].click()

    def get_contact_from_veiw_page(self, index):
        wd = self.app.wd
        self.open_veiw_page_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        mobile = re.search("M: (.*)", text).group(1)
        phone2 = re.search("P: (.*)", text).group(1)
        return Contact(homephone=homephone, workphone=workphone,
                       mobile=mobile,phone2=phone2)