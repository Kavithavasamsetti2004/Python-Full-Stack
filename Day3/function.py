
  # Printing some numbers in a same line
   #  FUNCTION

def fun(num):
    global i
    for i in range(1,num+1):
        print(i , end = " " )
  

num = int(input())
fun(num)

