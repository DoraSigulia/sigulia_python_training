from model.contact import Contact
from random import randrange

def test_modify_first_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.add(Contact(firstname="Ivan", middlename="Peter", lastname="Ivanov"))
    old_contact = app.contact.get_contact_list()
    contact = Contact(firstname="Иван")
    index = randrange(len(old_contact))
    contact.id = old_contact[index].id
    app.contact.modify_contact_by_index(contact, index)
    assert len(old_contact) == app.contact.count()
    new_contact = app.contact.get_contact_list()
    old_contact[index] = contact
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)

def test_modify_first_contact_lastname(app):
    if app.contact.count() == 0:
        app.contact.add(Contact(firstname="Ivan", middlename="Peter", lastname="Ivanov"))
    old_contact = app.contact.get_contact_list()
    contact = Contact(lastname="Тестович")
    index = randrange(len(old_contact))
    contact.id = old_contact[index].id
    app.contact.modify_contact_by_index(contact, index)
    assert len(old_contact) == app.contact.count()
    new_contact = app.contact.get_contact_list()
    old_contact[index] = contact
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)

