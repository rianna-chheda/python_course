print("CONTACT BOOK")
print()
print("Option 1: Add Contact")
print("Option 2: View Contacts")
print("Option 3: Search Contact")
print("Option 4: Update Contact")
print("Option 5: Delete Contact")
print("Option 6: Exit")
print()
choice = int(input("Select an option: "))

contacts={}

while choice == 1:
    contact_name=str(input("Enter a name: "))
    contact_no=str(input("Enter their number: ")) 
    contacts[contact_name]=contact_no
    print(contacts)
    print("Contact Added!")
    choice = int(input("Select an option: "))

while choice == 2:
    if len(contacts) == 0:
        print("No contacts found")
    else:
        print("Contacts:")
        for contact_name, contact_no in contacts.items():
            print(f"{contact_name}: {contact_no}")
    choice = int(input("Select an option: "))

while choice == 3: 
    search_name=input("Enter a contact name to search: ")
    if search_name in contacts:
        print(f"{search_name}: {contacts[contact_name]}")
    else:
        print("Contact not found")
    choice = int(input("Select an option: "))

while choice == 4:
    update_name = input("Enter contact name you want to update: ")
    if update_name in contacts:
        update_no = input("Enter a new number: ")
        contacts[update_name]=update_no
        print("Contact has been updated")
    else: 
        ("Contact not found")
    choice = int(input("Select an option: "))
    
while choice == 5:
    delete_name=input("Enter contact name to delete: ")
    if delete_name in contacts:
        del contacts[delete_name]
        print("Contact has been deleted")
    else:
        print("Contact not found")
    choice = int(input("Select an option: "))

while choice == 6:
    print("Exiting contacts")
    break