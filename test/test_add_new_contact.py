# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact_details
from fixture.application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture
    
def test_add_new_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.add(Contact_details(firstname="Ivan", middlename="Peter", lastname="Ivanov", nickname="admin911",
                                    title="test", company="OOO \"LM\"", address="Lenina, 1", phone_number_home="2894523",
                                    mobile="8951456789", phone_number_work="89634567823", email1="aaa@gmail.com", email2="bbb@mail.ru",
                                    bday="1", bmonth="July", byear="1995", aday="1", amonth="July", ayear="2025",
                                    address2="Lenina,1", phone2="Lenina,2", notes="test"))
    app.session.logout()
