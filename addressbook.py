class Contact:
    def __init__(self, name, phone_number, email):
        self.name = name
        self.phone_number = phone_number
        self.email = email

class AddressBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print("Contact added successfully!")

    def remove_contact(self, contact):
        if contact in self.contacts:
            self.contacts.remove(contact)
            print("Contact removed successfully!")
        else:
            print("Contact not found.")

    def search_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                print("Contact found:")
                print("Name:", contact.name)
                print("Phone Number:", contact.phone_number)
                print("Email:", contact.email)
                return
        print("Contact not found.")

    def display_contacts(self):
        if len(self.contacts) > 0:
            print("Address Book:")
            for contact in self.contacts:
                print("Name:", contact.name)
                print("Phone Number:", contact.phone_number)
                print("Email:", contact.email)
                print("------------------------")
        else:
            print("Address Book is empty.")

def main():
    address_book = AddressBook()
    while True:
        print("===== Address Book Menu =====")
        print("1. Add Contact")
        print("2. Remove Contact")
        print("3. Search Contact")
        print("4. Display Contacts")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            name = input("Enter contact name: ")
            phone_number = input("Enter contact phone number: ")
            email = input("Enter contact email: ")
            contact = Contact(name, phone_number, email)
            address_book.add_contact(contact)

        elif choice == "2":
            name = input("Enter contact name to remove: ")
            contact = Contact(name, "", "")
            address_book.remove_contact(contact)

        elif choice == "3":
            name = input("Enter contact name to search: ")
            address_book.search_contact(name)

        elif choice == "4":
            address_book.display_contacts()

        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
