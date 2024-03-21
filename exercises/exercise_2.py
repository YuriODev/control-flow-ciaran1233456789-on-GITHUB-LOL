# Your solution to Exercise 2

age = int(input("Enter the age of the person:"))

if age >= 20:
    output = "You are an adult."
elif age >= 13:
    output = "You are an teenager."
elif age > 1:
    output = "You are a child."
else: 
    output = "You are a infant."

print(output)
