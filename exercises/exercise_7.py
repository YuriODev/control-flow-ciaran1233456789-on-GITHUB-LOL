# Your solution to Exercise 7

float1 = float(input("enter first number: "))
float2 = float(input("enter second number: "))
arith_op = input("enter arithmetic operator")


if arith_op == "+":
    print(float1 + float2)
elif arith_op == "-":
    print(float1 - float2)
elif arith_op == "/":
    if float2 == 0:
        print("Division by 0!")
    else:
        print(float1 / float2)
elif arith_op == "*":
    print(float1 * float2)
elif arith_op == "mod":
    print(float1 % float2)
elif arith_op == "pow":
    print(float1 ** float2)
elif arith_op == "div":
    print(float1 // float2)
else:
    print("Error!!!\n The valid inputs are:\n + , - , / , * , mod , pow and div")
