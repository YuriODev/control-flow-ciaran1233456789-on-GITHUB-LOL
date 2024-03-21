# Your solution to Exercise 4
grade = int(input("Input your grade between 1 and 12: "))

if 0 < grade <= 12:
    if grade <= 3:
        print("Initial Level")
    elif grade <= 6:
        print("Average Level")
    elif grade <= 9:
        print("Sufficient Level")
    elif grade <= 12:
        print("High Level")

else:
    print("Level is Absent.")
