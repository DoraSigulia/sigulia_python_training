from model.contact import Contact_details

def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.add(Contact_details(firstname="Ivan"))
    old_contact = app.contact.get_contact_list()
    app.contact.del_first_contact()
    new_contact = app.contact.get_contact_list()
    assert len(old_contact) - 1 == len(new_contact)
