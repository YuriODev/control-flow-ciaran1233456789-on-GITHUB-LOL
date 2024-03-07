# Your solution to Exercise 1
Alex = int(input("Input Alex Age: "))
Tatyana = int(input("Input Tatyana Age: "))

if Alex > Tatyana:
    output = "Alex is the eldest."
elif Alex < Tatyana:
    output = "Tatyana is the eldest."
else:
    output = "Alex and Tatyana are of the same age."

print(output)

