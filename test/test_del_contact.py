from model.contact import Contact_details

def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.add(Contact_details(firstname="Ivan"))
    app.contact.del_first_contact()
