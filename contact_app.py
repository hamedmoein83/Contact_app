class Contact:
    counter = 1
    def __init__(self, name, lastname, phone, email, address):
        self._id = Contact.counter
        Contact.counter += 1
        self.name = name
        self.lastname = lastname
        self.phone = phone
        self.email = email
        self.address = address
    def __str__(self):
        return "name: {}\nlastname: {}\nphone: {}\nemail: {}\naddress: {}"\
            .format(self.name, self.lastname, self.phone, self.email, self.address)


class Panel:

    def __init__(self):
        self.repo = ListRepository()

    # TODO Check phone number before add
    def add_new_contact(self):
        name = input("enter name? ")
        lastname = input("enter lastname? ")
        phone = input("enter phone? ")
        email = input("enter email? ")
        address = input("enter address? ")
        contact = Contact(name, lastname, phone, email, address)
        self.repo.save(contact)

    def search_contact(self):
        name = input("enter name? ")
        contacts = self.repo.search_by_name(name)
        for contact in contacts:
            print(contact)
            print("="*20)

    def search_contact2(self):
        name = input("enter name? ")
        lastname = input ("enter lastname? ")
        contacts = self.repo.search_by_name_and_lastname(name, lastname)
        for contact in contacts:
            print(contact)
            print("="*20)

    def show_menu(self):
        print("1-Add New Contact")
        print("2-Show All Contact")
        print("3-Search Contact By Name")
        print("4-Delete Contact")
        print("5-Update Contact")
        print("6-Send SMS to Contact")
        print("7-Send Email to Contact")
        print("8-Exit")
        print("9-search by name and lastname")
        print("10-delete by phone number")

    def show_all_contacts(self):
        contacts = self.repo.find_all()
        for contact in contacts:
            print(contact)
            print("="*20)

    def delete_contact(self):
        name = input("enter name? ")
        contacts = self.repo.search_by_name(name)
        for contact in contacts:
            print(contact)
            print("=" * 20)
            choice = input("Do you want to delete this contact?[y/n]")
            if choice == 'y':
                self.repo.delete(contact._id)
                break

    def delete_contact2(self):
        phone = input("enter phone? ")
        contacts = self.repo.search_by_phone_number(phone)
        for contact in contacts:
            print(contact)
            print("=" * 20)
            choice = input("Do you want to delete this contact?[y/n]")
            if choice == 'y':
                self.repo.delete(contact._id)
                break

    def update_contact(self):
        name = input("enter name? ")
        contacts = self.repo.search_by_name(name)
        for contact in contacts:
            print(contact)
            print("=" * 20)
            choice = input("Do you want to update this contact?[y/n]")
            if choice == 'y':
                name = input("enter name? ")
                lastname = input("enter lastname? ")
                phone = input("enter phone? ")
                email = input("enter email? ")
                address = input("enter address? ")
                name = contact.name if name == '' else name
                lastname = contact.lastname if lastname == '' else lastname
                phone = contact.phone if phone == '' else phone
                email = contact.email if email == '' else email
                address = contact.address if address == '' else address
                new_contact = Contact(name, lastname, phone, email, address)
                new_contact._id = contact._id
                self.repo.update(new_contact)


    def start_app(self):
        while True:
            self.show_menu()
            option = int(input("choose an option"))
            if option == 1:
                self.add_new_contact()
            elif option == 2:
                self.show_all_contacts()
            elif option == 3:
                self.search_contact()
            elif option == 4:
                self.delete_contact()
            elif option == 5:
                self.update_contact()
            elif option == 6:
                self.send_sms()
            elif option == 7:
                self.send_email()
            elif option == 8:
                exit(0)
            elif option == 9:
                self.search_contact2()
            elif option == 10:
                self.delete_contact2()
            else:
                print("Get Away")


class ListRepository:
    def __init__(self):
        self.repository = {}

    def save(self, contact):
        self.repository[contact._id] = contact

    def delete(self, _id):
        del self.repository[_id]

    def delete_by_phone_number(self, _id):
        del self.repository[_id]

    def search_by_name(self, name):
        l = []
        for contact in self.repository.values():
            if contact.name == name:
                # TODO copy the values or not..copy the values or copy the contacts?!
                l.append(contact)
        return l

    def search_by_name_and_lastname(self, name, lastname):
        ll = []
        for contact in self.repository.values():
            if contact.name == name and contact.lastname == lastname:
                ll.append(contact)
        return ll

    def search_by_phone_number(self, phone):
        lll = []
        for contact in self.repository.values():
            if contact.phone == phone:
                lll.append(contact)
        return lll

    def find_all(self):
        # TODO copy the values or not..copy the values or copy the contacts?!
        return self.repository.values()

    def update(self, contact):
        self.save(contact)


app = Panel()
app.start_app()
