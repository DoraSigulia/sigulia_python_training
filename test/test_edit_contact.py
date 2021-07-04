from model.contact import Contact_details

def test_edit_first_contact(app):
    if app.contact.count() == 0:
        app.contact.add(Contact_details(firstname="Ivan", middlename="Peter", lastname="Ivanov", nickname="admin911",
                                    title="test", company="OOO \"LM\"", address="Lenina, 1", phone_number_home="2894523",
                                    mobile="8951456789", phone_number_work="89634567823", email1="aaa@gmail.com", email2="bbb@mail.ru",
                                    bday="1", bmonth="July", byear="1995", aday="1", amonth="July", ayear="2025",
                                    address2="Lenina,1", phone2="Lenina,2", notes="test"))
    app.contact.edit_first(Contact_details(firstname="Иван", middlename="Петр", lastname="Иванов", nickname="админ911",
                                    title="тест", company="OOO \"ЛМ\"", address="Ленина, 1", phone_number_home="2657856",
                                    mobile="89896022596", phone_number_work="8963852741", email1="aaa@gmail.com", email2="bbb@mail.ru",
                                    bday="2", bmonth="July", byear="1990", aday="2", amonth="July", ayear="2030",
                                    address2="Ленина,1", phone2="Ленина,2", notes="тест"))
