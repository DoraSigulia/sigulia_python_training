from sys import maxsize

class Contact():
    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, title=None, company=None, address=None, phone_number_home=None,
                        mobile=None, phone_number_work=None, email1=None, email2=None, bday=None, bmonth=None, byear=None, aday=None, amonth=None, ayear=None, address2=None,
                        phone2=None, notes=None, id=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.phone_number_home = phone_number_home
        self.mobile = mobile
        self.phone_number_work = phone_number_work
        self.email1 = email1
        self.email2 = email2
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.aday = aday
        self.amonth = amonth
        self.ayear = ayear
        self.address2 = address2
        self.phone2 = phone2
        self.notes = notes
        self.id = id

    def __repr__(self):
        return "%s:%s" % (self.id, self.firstname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id), self.firstname == other.firstname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize