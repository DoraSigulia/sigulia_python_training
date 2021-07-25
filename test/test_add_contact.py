from model.contact import Contact

def test_add_contact(app):
    old_contact = app.contact.get_contact_list()
    contact = Contact(firstname="Ivan", lastname="Ivanov")
    app.contact.add(contact)
    assert len(old_contact) + 1 == app.contact.count()
    new_contact = app.contact.get_contact_list()
    old_contact.append(contact)
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)