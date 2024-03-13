# Your solution to Exercise 5

a = int(input("Enter Co-effificent of x^2: "))
b = int(input("Enter co-efficient of x: "))
c = int(input("Enter c: "))

discriminant = (b**2) - (4 * a * c)

if discriminant == 0:
    print("1 Repeated Root")
elif discriminant > 0:
    print("2 Real Roots")
else:
    print("No Real Roots")