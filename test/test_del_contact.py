from model.contact import Contact

def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.add(Contact(firstname="Ivan", middlename="Peter", lastname="Ivanov", nickname="admin911",
                            title="test", company="OOO \"LM\"", address="Lenina, 1", phone_number_home="2894523",
                            mobile="8951456789", phone_number_work="89634567823", email1="aaa@gmail.com", email2="bbb@mail.ru",
                            bday="1", bmonth="July", byear="1995", aday="1", amonth="July", ayear="2025",
                            address2="Lenina,1", phone2="Lenina,2", notes="test"))
    old_contact = app.contact.get_contact_list()
    app.contact.del_first_contact()
    new_contact = app.contact.get_contact_list()
    assert len(old_contact) - 1 == len(new_contact)
    old_contact[0:1] = []
    assert old_contact == new_contact
