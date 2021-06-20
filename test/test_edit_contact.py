from model.contact import Contact_details

def test_edit_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit(Contact_details(firstname="Иван", middlename="Петр", lastname="Иванов", nickname="админ911",
                                    title="тест", company="OOO \"ЛМ\"", address="Ленина, 1", phone_number_home="2657856",
                                    mobile="89896022596", phone_number_work="8963852741", email1="aaa@gmail.com", email2="bbb@mail.ru",
                                    bday="2", bmonth="July", byear="1990", aday="2", amonth="July", ayear="2030",
                                    address2="Ленина,1", phone2="Ленина,2", notes="тест"))
    app.session.logout()
