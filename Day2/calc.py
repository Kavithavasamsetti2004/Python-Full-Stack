
   # Performing Calculations using if , elif , else conditions

op1 = int(input())
op2 = int(input())
op = input()
if op == "+" :
    print(op1 + op2)
elif op == "-" :
    print(op1 - op2)
elif op == "*" :
    print(op1 * op2)
elif op == "/" :
    print(op1 / op2)
elif op == "//" :
    print(op1 // op2)
elif op == "%" :
    print(op1 % op2)
else:
    print("Give valid operator")