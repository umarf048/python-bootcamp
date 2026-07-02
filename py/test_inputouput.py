name = str(input("Enter your name:"))
height = float(input("Enter your height:"))

while True:
    try:
        age = int(input("Enter your age:"))
        if age > 0 and age < 130:
            break
        else :
            print("Age must be releven!")
    except ValueError:
        print("please enter a valid number!")

        #output
print(f"hello, {name}!")
print(f"you are {age} years old and {height} feet tall")
