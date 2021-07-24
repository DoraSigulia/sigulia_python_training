from model.contact import Contact

def test_modify_first_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.add(Contact(firstname="Ivan", middlename="Peter", lastname="Ivanov"))
    old_contact = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact(firstname="Иван"))
    new_contact = app.contact.get_contact_list()
    assert len(old_contact) == len(new_contact)

def test_modify_first_contact_middlename(app):
    if app.contact.count() == 0:
        app.contact.add(Contact(firstname="Ivan", middlename="Peter", lastname="Ivanov"))
    old_contact = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact(middlename="Петр"))
    new_contact = app.contact.get_contact_list()
    assert len(old_contact) == len(new_contact)

def test_modify_first_contact_lastname(app):
    if app.contact.count() == 0:
        app.contact.add(Contact(firstname="Ivan", middlename="Peter", lastname="Ivanov"))
    old_contact = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact(lastname="Иванов"))
    new_contact = app.contact.get_contact_list()
    assert len(old_contact) == len(new_contact)