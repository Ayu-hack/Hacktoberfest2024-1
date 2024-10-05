#Contact Management Project

import json  

# File to store contacts  
CONTACTS_FILE = 'contacts.json'  

# Load contacts from the JSON file  
def load_contacts():  
    try:  
        with open(CONTACTS_FILE, 'r') as file:  
            return json.load(file)  
    except FileNotFoundError:  
        return {}  

# Save contacts to the JSON file  
def save_contacts(contacts):  
    with open(CONTACTS_FILE, 'w') as file:  
        json.dump(contacts, file)  

# Add a new contact  
def add_contact(contacts):  
    name = input("Enter contact name: ")  
    phone = input("Enter contact phone: ")  
    contacts[name] = phone  
    save_contacts(contacts)  
    print(f"Contact {name} added.")  

# View all contacts  
def view_contacts(contacts):  
    if not contacts:  
        print("No contacts found.")  
    else:  
        for name, phone in contacts.items():  
            print(f"Name: {name}, Phone: {phone}")  

# Delete a contact  
def delete_contact(contacts):  
    name = input("Enter the name of the contact to delete: ")  
    if name in contacts:  
        del contacts[name]  
        save_contacts(contacts)  
        print(f"Contact {name} deleted.")  
    else:  
        print("Contact not found.")  

# Main function to run the program  
def main():  
    contacts = load_contacts()  
    
    while True:  
        print("\nContact Management System")  
        print("1. Add Contact")  
        print("2. View Contacts")  
        print("3. Delete Contact")  
        print("4. Exit")  
        
        choice = input("Choose an option: ")  
        
        if choice == '1':  
            add_contact(contacts)  
        elif choice == '2':  
            view_contacts(contacts)  
        elif choice == '3':  
            delete_contact(contacts)  
        elif choice == '4':  
            print("Exiting the program.")  
            break  
        else:  
            print("Invalid choice. Please try again.")  

if __name__ == "__main__":  
    main()
