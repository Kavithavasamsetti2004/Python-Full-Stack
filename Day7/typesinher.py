
   # Types of inheritance in python

class College:
    def __init__(self,x,y,z):
        self.Name = x
        self.Department = y
        self.Year = z
        pass

    def display(self):
        print(f"Studying at {self.Name} in {self.Department} of {self.Year}")

k = College("BVC","AIML",2026)
 
class Student:
    def __init__(self,a,b,c):
        self.Name = a
        self.Rollno = b
        self.Branch = c

    def details(self):
        print(f"Student name is {self.Name},Their Rollno is {self.Rollno} from {self.Branch}")


stu1 = Student("kavitha",56,"Aiml")
stu2 = Student("Dhanya",55,"Aiml")
stu3 = Student("Anu",54,"Aiml")

x = Student()
print(x.details())



