wheel = int(input("Enter a number on routlette wheel: "))

if wheel % 2 == 0:
    even = True
else:
    even = False

if wheel == 0:
    colour = "Green"
elif wheel < 11:
    if even == False:
        colour = "Red"
    else:
        colour = "Black"
elif wheel <= 18:
    if even == False:
        colour = "Black"
    else:
        colour = "Red"
elif wheel <= 28:
    if even == False:
        colour = "Red"
    else:
        colour = "Black"
elif wheel <= 36:
    if even == False:
        colour = "Black"
    else:
        colour = "Red"
else:
    colour = "The Bet will not play!"

print(colour)

