three_digit = int(input("Enter a three digit integer: "))

digit2 = (three_digit % 100) // 10
sum = (three_digit // 100) + ((three_digit % 100) % 10)


if sum == digit2:
    print("=")
elif sum > digit2:
    print(">")
else:
    print("<")


