from model.contact import Contact_details

def test_modify_first_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.add(Contact_details(firstname="Ivan", middlename="Peter", lastname="Ivanov"))
    old_contact = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact_details(firstname="Иван"))
    new_contact = app.contact.get_contact_list()
    assert len(old_contact) == len(new_contact)

def test_modify_first_contact_middlename(app):
    if app.contact.count() == 0:
        app.contact.add(Contact_details(firstname="Ivan", middlename="Peter", lastname="Ivanov"))
    old_contact = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact_details(middlename="Петр"))
    new_contact = app.contact.get_contact_list()
    assert len(old_contact) == len(new_contact)

def test_modify_first_contact_lastname(app):
    if app.contact.count() == 0:
        app.contact.add(Contact_details(firstname="Ivan", middlename="Peter", lastname="Ivanov"))
    old_contact = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact_details(lastname="Иванов"))
    new_contact = app.contact.get_contact_list()
    assert len(old_contact) == len(new_contact)