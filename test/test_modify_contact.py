from model.contact import Contact_details

def test_modify_first_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.add(Contact_details(firstname="Ivan", middlename="Peter", lastname="Ivanov"))
    app.contact.modify_first_contact(Contact_details(firstname="Иван"))

def test_modify_first_contact_middlename(app):
    if app.contact.count() == 0:
        app.contact.add(Contact_details(firstname="Ivan", middlename="Peter", lastname="Ivanov"))
    app.contact.modify_first_contact(Contact_details(middlename="Петр"))

def test_modify_first_contact_lastname(app):
    if app.contact.count() == 0:
        app.contact.add(Contact_details(firstname="Ivan", middlename="Peter", lastname="Ivanov"))
    app.contact.modify_first_contact(Contact_details(lastname="Иванов"))