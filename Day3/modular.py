
   # Importing a file "funs" in which all the functions are  defined


import funs
num1 = int(input())
while True:
    op = input()
    if op == "=":
        print("End answer is : ",num1)
        break
    num2 = int(input())

    if op == '+':
        num1 = funs.add(num1,num2)
    elif op == '-':
        num1 = funs.sub(num1,num2)
    elif  op == '*':
        num1 = funs.mul(num1,num2)
    elif op == '/':
        num1 = funs.div(num1,num2)
    print(num1)

    
    


