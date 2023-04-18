import calc

a = int(input("Enter first number:"))
b = int(input("Enter Second number:"))

obj = calc.Calculator()
choice = 1
while choice != 0:
    print("1. ADD")
    print("2. SUB")
    print("3. MUL")
    print("4. DIV")
    choice = int(input("Enter your choice:"))

    if choice == 1:
        print(obj.addition())
    elif choice == 2:
        print(obj.subtraction())
    elif choice == 3:
        print(obj.multiplication())
    elif choice == 4:
        print(obj.division())
    else:
        print("Invalid choice")
