
    # printing pattern
  


def pattern(num):
    for i in range(1,num+1):
        print(i,end = " ")
        print(" ")
    
n = int(input("Enter a number: "))
for i in range(0,n):
    pattern(n)