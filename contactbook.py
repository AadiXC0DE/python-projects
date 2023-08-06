import json

def load_contacts():
    try:
        with open('contacts.json', 'r') as file:
            contacts = json.load(file)
    except FileNotFoundError:
        contacts = []
    return contacts

def save_contacts(contacts):
    with open('contacts.json', 'w') as file:
        json.dump(contacts, file)

def add_contact(name, phone, email):
    contact = {
        'name': name,
        'phone': phone,
        'email': email
    }
    contacts = load_contacts()
    contacts.append(contact)
    save_contacts(contacts)
    print(f'Contact {name} added successfully.')

def view_contacts():
    contacts = load_contacts()
    if not contacts:
        print("No contacts found.")
        return

    print("Contacts:")
    for index, contact in enumerate(contacts, start=1):
        print(f"{index}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")

def search_contact(query):
    contacts = load_contacts()
    results = []
    for contact in contacts:
        if query.lower() in contact['name'].lower() or query.lower() in contact['phone']:
            results.append(contact)
    if not results:
        print("No matching contacts found.")
        return

    print("Search Results:")
    for index, contact in enumerate(results, start=1):
        print(f"{index}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")

def delete_contact(index):
    contacts = load_contacts()
    if 0 < index <= len(contacts):
        deleted_contact = contacts.pop(index - 1)
        save_contacts(contacts)
        print(f"Contact {deleted_contact['name']} deleted successfully.")
    else:
        print("Invalid contact index.")

def main():
    print("Welcome to the Contact Book!")
    while True:
        print("\nOptions:")
        print("1. Add a contact")
        print("2. View all contacts")
        print("3. Search for a contact")
        print("4. Delete a contact")
        print("5. Exit")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == '1':
            name = input("Enter the name: ")
            phone = input("Enter the phone number: ")
            email = input("Enter the email address: ")
            add_contact(name, phone, email)
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            query = input("Enter the search query: ")
            search_contact(query)
        elif choice == '4':
            index = int(input("Enter the contact index to delete: "))
            delete_contact(index)
        elif choice == '5':
            print("Exiting the Contact Book.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
