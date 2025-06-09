   
   # Finding large number among 3 numbers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a>b and a>c :
    print("a is large")
elif b>a and b>c :
    print("b is large")
else:
    print("c is large")