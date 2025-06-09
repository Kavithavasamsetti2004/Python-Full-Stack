

import functions as con

contacts = {}
try:
    while True:
        print("Enter your choice: ")
        print("1.Add contact")
        print("2.View contact")
        print("3.Delete contact")
        print("4.Edit contact")
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
except Exception as error:
    print(f"Error occured at {error}")
else:
    print("No error")
finally:
    print("==>Contact Book<==")
