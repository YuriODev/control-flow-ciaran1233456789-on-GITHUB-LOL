# Your solution to Exercise 8
int1 = int(input("Enter a 3 digit number: "))
int2 = int(input("Enter a digit to search for"))
search = False

if (int1 //100) == int2:
    search = True
elif ((int1 // 10) % 10) == int2:
    search = True
elif (int1 % 10):
    search = True

print(search)
