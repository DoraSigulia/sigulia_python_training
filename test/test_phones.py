import re


def test_phones_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_from_edit_page(0)
    assert contact_from_home_page.all_phones == merge_phone_like_of_home_page(contact_from_edit_page)


def test_phones_on_veiw_page(app):
    contact_from_veiw_page = app.contact.get_contact_from_veiw_page(0)
    contact_from_edit_page = app.contact.get_contact_from_edit_page(0)
    assert contact_from_veiw_page.homephone == contact_from_edit_page.homephone
    assert contact_from_veiw_page.workphone == contact_from_edit_page.workphone
    assert contact_from_veiw_page.mobile == contact_from_edit_page.mobile
    assert contact_from_veiw_page.phone2 == contact_from_edit_page.phone2


def clear(s):
    return re.sub("[-()]", "", s)


def merge_phone_like_of_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.homephone, contact.mobile, contact.workphone,
                                        contact.phone2]))))
