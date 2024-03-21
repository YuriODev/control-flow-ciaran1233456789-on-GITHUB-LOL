# Your solution to Exercise 6
x1 = int(input("Input X Co-ord: "))
y1 = int(input("Input Y Co-ord: "))
x2 = int(input("Input 2nd X Co-ord: ")) 
y2 = int(input("Input 2nd Y Co-ord: "))

Point1 = ((x1**2) + (y1**2)) ** 0.5
Point2 = ((x2**2) + (y2**2)) ** 0.5

if Point1 > Point2:
    print("A is further from the origin.")
elif Point2 > Point1:
    print("B is further from the origin")
else:
    print("A and B are at the same distance from the origin.")
