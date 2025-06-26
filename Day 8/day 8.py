from os import name
#Contact Book

# 1: Initializing empty book
contacts = {}

# 2: Menu part
def menu():
    print("\n Menu")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Edit Contact")
    print("5. Delete Contact")
    print("6. Exit \n")

# 3: Add a contact
def add():
    name = input("Enter contact name: ")
    phone = input("Enter contact number: ")
    email = input("Enter contact email: ")
    contacts[name] = {"phone": phone, "email": email}
    print(f"Contact {name} has been added to the contact book.")

# 4: View all contact
def view():
    if contacts:
        print("\n Contact List")
        for name, details in contacts.items():
            print(f"Name : {name}")
            print(f"Phone: {details["phone"]}")
            print(f"Email: {details["email"]} \n")
    
    else:
        print("Book is empty.")

# 5: Search Contact
def search():
    name = input("Enter the name of contact you want to search: ")
    if name in contacts:
        print("Contact Details: ")
        print(f"Name : {name}")
        print(f"Phone : {contacts[name]["phone"]}")
        print(f"Email : {contacts[name]["email"]}")
    else: 
        print(f"{name} not found in the book.")

# 6: Edit Contact
def edit():
    name = input("Enter name of the contact you want to edit: ")
    if name in contacts:
        phone = input("Enter new phone number: ")
        email = input("Enter new email: ")
        contacts[name] = {"phone": {phone}, "email": {email}}
        print("Contact has been edited and updated successfully")
    else:
        print("Contact not found in contact book.")

# 7: Delete Contact
def delete():
    name = input("Enter the name of contact you want to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} has been deleted successfully.")
    else:
        print(f"Contact {name} not found.")

# 8: Main Program Loop
while True:
    menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        add()
    elif choice == "2":
        view()
    elif choice == "3":
        search()
    elif choice == "4":
        edit()
    elif choice == "5":
        delete()
    elif choice == "6":
        print("See you again. Bye!")
        break
    else:
        print("Invalid choice. Select a number between 1 to 6.")

        
