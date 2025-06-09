try:
    num1 = int(input())
    num2 = int(input())
    result = num1/num2
    print(result)
except ZeroDivisionError:
    print("Error occured")
finally:
    print("OK bye!!!")


