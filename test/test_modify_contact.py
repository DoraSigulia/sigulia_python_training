from model.contact import Contact

def test_modify_first_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.add(Contact(firstname="Ivan", middlename="Peter", lastname="Ivanov"))
    old_contact = app.contact.get_contact_list()
    contact = Contact(firstname="Иван")
    contact.id = old_contact[0].id
    app.contact.modify_first_contact(contact)
    new_contact = app.contact.get_contact_list()
    assert len(old_contact) == len(new_contact)
    old_contact[0] = contact
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)

def test_modify_first_contact_lastname(app):
    if app.contact.count() == 0:
        app.contact.add(Contact(firstname="Ivan", middlename="Peter", lastname="Ivanov"))
    old_contact = app.contact.get_contact_list()
    contact = Contact(lastname="Тестович")
    contact.id = old_contact[0].id
    app.contact.modify_first_contact(contact)
    new_contact = app.contact.get_contact_list()
    assert len(old_contact) == len(new_contact)
    old_contact[0] = contact
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)

