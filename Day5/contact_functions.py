def add_contact(contacts):
    name = input("Enter your Name: ")
    mob = int(input("Enter your number: "))
    contacts[name] = mob

def view_contact(contacts):
    for i in contacts:
        print(f"{i} = {contacts[i]}")

def delete_contact(contacts):
    name_to_delete = input("Enter the name to delete: ")
    del contacts[name_to_delete]
    print(contacts)

def edit_contact(contacts):
    name_to_edit = input("Enter name to edit: ")
    num_to_edit = int(input("Enter number to edit: "))
    contacts[name_to_edit] = num_to_edit
    print(f"Edited contact 2{name_to_edit} = {num_to_edit}")                      




