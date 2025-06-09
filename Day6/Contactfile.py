
try:
    file = open("contactbook.txt","r")
    data = file.read()
    print(data)
except Exception as e:
    print(f"Error at {e}")
finally:
    file.close()