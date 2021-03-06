from model.contact import Contact
from random import randrange

def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.add(Contact(firstname="Ivan", middlename="Peter", lastname="Ivanov", nickname="admin911",
                                title="test", company="OOO \"LM\"", address="Lenina, 1", homephone="2894523",
                                mobile="8951456789", workphone="89634567823", email1="aaa@gmail.com", email2="bbb@mail.ru",
                                bday="1", bmonth="July", byear="1995", aday="1", amonth="July", ayear="2025",
                                address2="Lenina,1", phone2="Lenina,2", notes="test"))
    old_contact = app.contact.get_contact_list()
    index = randrange(len(old_contact))
    app.contact.del_contact_by_index(index)
    assert len(old_contact) - 1 == app.contact.count()
    new_contact = app.contact.get_contact_list()
    old_contact[index:index+1] = []
    assert old_contact == new_contact
