
   # Finding Factorial of a number 


def factorial(num):
    if num<0:
        return
    fact = 1
    for i in range(1,n+1):
        fact *= i
    print(fact)
    
n = int(input("Enter a number: "))
factorial(n)