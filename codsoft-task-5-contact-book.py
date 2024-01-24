#my-contact-list
class ContactManager:
    def __init__(self):
        self.contacts = {}
        self.contact_id_counter = 1

    def display_menu(self):
        print("""

             My-Contact-List            
-------------------------------------------
1. Contact Information
2. Search Contact
3. Add Contact
4. Update Contact
5. Delete Contact
6. Exit """)
    def view_contact_list(self):
        print("__________________________________________")
        print("          View Contact List              ")
        print("__________________________________________")
        print("ID  | Name           | Phone Number     ")
        print("-------------------------------------------")
        for contact_id, details in self.contacts.items():
            print(f"{contact_id}   | {details['name']}       | {details['phone']}     ")
        print("-------------------------------------------")
    def search_contact(self):
        print("            Search Contact               ")
        search_query = input("Enter name or phone number to search: ")
        found_contacts = []
        for contact_id, details in self.contacts.items():
            if search_query.lower() in details['name'].lower() or search_query in details['phone']:
                found_contacts.append((contact_id, details))
        if found_contacts:
            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
            print("           Search Results                ")
            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
            print("ID   |Name           | Phone Number     ")
            for contact_id, details in found_contacts:
                print(f"{contact_id}    |{details['name']}       | {details['phone']}     ")
            print("-------------------------------------------")
        else:
            print("No contacts found.")
    def add_contact(self):
        print("-------------------------------------------")
        print("             Add Contact                 ")
        print("-------------------------------------------")
        name = input("Name: ")
        phone = input("Phone Number: ")
        email = input("Email: ")
        address = input("Address: ")
        new_contact = {
            'name': name,
            'phone': phone,
            'email': email,
            'address': address
        }
        contact_id = self.contact_id_counter
        self.contacts[contact_id] = new_contact
        self.contact_id_counter += 1
        print(f"Contact added successfully. ID: {contact_id}")
    def update_contact(self):
        self.view_contact_list()
        contact_id = int(input("Enter the ID of the contact to update: "))
        if contact_id in self.contacts:
            print("           Update Contact                ")
            name = input("Name: ")
            phone = input("Phone Number: ")
            email = input("Email: ")
            address = input("Address: ")

            self.contacts[contact_id] = {
                'name': name,
                'phone': phone,
                'email': email,
                'address': address
            }
            print("Contact Updated successfully.")
        else:
            print("Contact not found.")
    def delete_contact(self):
        self.view_contact_list()
        contact_id = int(input("Enter the ID of the contact to delete: "))
        if contact_id in self.contacts:
            del self.contacts[contact_id]
            print("Contact deleted successfully.")
        else:
            print("Contact not found.")
    def run(self):
        while True:
            self.display_menu()
            choice = input("Please enter the number corresponding to your choice: ")

            if choice == '1':
                self.view_contact_list()
            elif choice == '2':
                self.search_contact()
            elif choice == '3':
                self.add_contact()
            elif choice == '4':
                self.update_contact()
            elif choice == '5':
                self.delete_contact()
            elif choice == '6':
                print("BYE! SEE YOU AGAIN!")
                break
            else:
                print("Invalid choice. Please enter a valid option.")
if __name__ == "__main__":
    contact_manager = ContactManager()
    contact_manager.run()
