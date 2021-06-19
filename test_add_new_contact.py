# -*- coding: utf-8 -*-
import pytest
from contact import Contact_details
from application_contact import Application_for_Contact

@pytest.fixture
def app_cont(request):
    fixture = Application_for_Contact()
    request.addfinalizer(fixture.destroy)
    return fixture
    
def test_add_new_contact(self):
    app_cont.login(username="admin", password="secret")
    app_cont.add_new_contact(Contact_details(firstname="Ivan", middlename="Peter", lastname="Ivanov", nickname="admin911",
                                               title="test", company="OOO \"LM\"", address="Lenina, 1", phone_number_home="2894523",
                                               mobile="8951456789", phone_number_work="89634567823", email1="aaa@gmail.com", email2="bbb@mail.ru",
                                               bday="1", bmonth="July", byear="1995", aday="1", amonth="July", ayear="2025",
                                               address2="Lenina,1", phone2="Lenina,2", notes="test"))
    app_cont.logout()
