

def add_student(students):
    name = input("Enter Student name: ")
    marks = list(map(int,input().split()))
    students[name] = marks
    print(students)

def view_student(students):
    sum = 0
    for i in students:
        sum += i
        avg = sum / length[marks]
        students[name] = avg

def search_student(students):
    name = input("Enter name to search: ")
    if name in students:
        print(f"{name} ")
    else:
        print("Name not found")

def update_student(students):
    name = input("Enter name of the student:")
    if name in students:
        new_marks = input("Enter new marks with space: ") 
        marks = list(map(int,new_marks.split()))
        new_marks = students[marks]
        print(students)

def remove_student(students):
    name = input("Enter name to remove:")
    if name in students:
        del students[name]
        print(f"{name} is removed from gradebook")
        print(students)
    else:
        print("Name not found")