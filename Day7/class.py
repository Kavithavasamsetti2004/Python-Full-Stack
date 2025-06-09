   # Class
class School: 
       #constructor
    def __init__(self,x,y,z):
        self.Name=x
        self.Rollno=y
        self.Branch=z
        

    def display(self):          #method
        print(f"Student name is {self.Name} and thier roll no is {self.Rollno} from {self.Branch} Branch")

#objects    
stu1 = School("Kavitha",56,"Aiml")
stu2 = School("Swetha",26,"Aiml")

#x = School()
stu2.display()
print(stu1.Name)
print(stu1.Rollno)



