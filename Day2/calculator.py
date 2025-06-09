  # Performing realtime calculator operations
num1 = int(input())
while True:
        op = input()
        num2 = int(input())
        if op == "=":
                break  
        
        elif op == "+":
                num1 = num1 + num2
                
        elif op == "-":
                num1 = num1 - num2
                
        elif op == "*":
                num1 = num1 * num2
        
        elif op == "/":
                num1 = num1 / num2
        print(num1)


        
        


