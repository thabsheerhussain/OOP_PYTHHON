class Contact:
    all_contact = []

    def __init__(self,name,email):
        self.name = name
        self.email = email
        Contact.all_contact.append(self)
class supply(Contact):
    def order(self, order):
        print("the order is" '{order}' "nmae is "'{self.name}')