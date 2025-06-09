 
   # import only add function from fun module/file

from funs import add 
num1 = int(input())
while True:
    op = input()
    if op == "=":
        print("End answer is : ",num1)
        break
    num2 = int(input())

    if op == '+':
        num1 = add(num1,num2)
    elif op == '-':
        num1 = sub(num1,num2)
    elif  op == '*':
        num1 = mul(num1,num2)
    elif op == '/':
        num1 = div(num1,num2)
    print(num1)

    
    