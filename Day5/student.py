
import Gradebook as grad
students = {}

while True:
    print("GradeBook management System ")
    print("1.Add student")
    print("2.View all students avg marks")
    print("3.Search for the student by name")
    print("4.Update marks of existing student")
    print("5.Remove a student from the gradebook")
    print("6.Exit ")

    choice = int(input("Enter your Choice: "))

    if choice == 1:
        grad.add_student(students)
    elif choice == 2:
        grad.view_student(students)
    elif choice == 3:
        grad.search_student(students)
    elif choice == 4:
        grad.update_student(students)
    elif choice == 5:
        grad.remove_student(students)
    else:
        print("Exit")
        
