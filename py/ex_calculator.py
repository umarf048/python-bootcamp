num1 = int(input("first number:"))
num2 = int(input("second number:"))
ope = input("operation : ")

if ope == "+":
    print(f"{num1} {ope} {num2} = {num1 + num2}")

elif ope == "-":
    print(f"{num1} {ope} {num2} = {num1 - num2}")

elif ope == "*":
    print(f"{num1} {ope} {num2} = {num1 * num2}")

elif ope == "/":
    if num2 == 0:
        print("cannot divide by 0")
    else:
        print(f"{num1} {ope} {num2} = {num1 / num2}")