year = int(input("Enter the year: "))

if year % 4 == 0 and not year % 100 == 0 or year % 400 == 0:
    print("Leap Year")
else:
    print("Ordinary Year")
# Your solution to Exercise 11

