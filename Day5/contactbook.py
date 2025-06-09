 # Main code for Contactbook
import contact_functions as con
contacts = {}

while True:
    print(" Enter your choice: ")
    print("Add contact")
    print("View contact")
    print("Delete contact")
    print("Edit contact")
    print("Exit ")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        con.add_contact(contacts)
    elif choice == 2:
        con.view_contact(contacts)
    elif choice == 3:
        con.delete_contact(contacts)
    elif choice == 4:
        con.edit_contact(contacts)
    else:
        print("Thank you !!!")
        break
        