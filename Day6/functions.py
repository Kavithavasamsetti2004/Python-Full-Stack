
def add_contact(contacts):
    try:
        file = open("textfile.txt","a")
        name = input("Enter your Name: ")
        mob = int(input("Enter your number: "))
        file.write(f"{name} : {mob}\n")
        contacts[name] = mob
    except ValueError:
        print("ValueError occured")
    

def view_contact(contacts):
    try:
        file = open("textfile.txt","r")
        data = file.read()
        print(data)
       # for i in contacts:
           # print(f"{i} = {contacts[i]}")

    except Exception as error:
        print(f"Error occured at {error}")

def delete_contact(contacts):
    try:
        file = open("textfile.txt","w+")
        name_to_delete = input("Enter the name to delete: ")
        if name_to_delete in contacts:
            del contacts[name_to_delete]
        else:
            print("Name Not found")
            print(contacts)
    except Exception as error:
        print(f"Error occured at {error}")

def edit_contact(contacts):
    try:
        file = open("textfile.txt","r+")
        name_to_edit = input("Enter name to edit: ")
        if name_to_edit in contacts:
            contacts[name_to_edit] = list(map(int,name_to_edit.split("")))
        num_to_edit = int(input("Enter number to edit: "))
        data = file.write(f"{num_to_edit}")
        print(data)
        contacts[name_to_edit] = num_to_edit
        print(f"Edited contact {name_to_edit} = {num_to_edit}")                  
    except Exception as error:
        print(f"Error occured at {error}")       




