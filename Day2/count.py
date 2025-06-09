
  # Counting no.of vowels in the string

def count(str):
    global count
    count = 0 
    for i in range(0,len(str) + 1):
        if str[i] in {"a","e","i","o","u"}:
            count += 1
    print(count)


str = input("Enter a string: ")
count(str)
