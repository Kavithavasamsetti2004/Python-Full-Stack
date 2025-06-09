
class Family:
    
    def Father():
        print("Father is angry")


    def Mother():
        print("Mother is Beautiful")
        pass

class Parent(Family):

    def Child(self):
        print("Child is angry and beautiful")
        pass

x = Parent.Father()

y = Family.Mother()

