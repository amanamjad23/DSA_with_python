name=input("enter your name : ")
print ("Welcome ", name," to DSA with PYTHON ")

def factorial():
    num=int(input("Enter the number to find factorial "))
    result = 1
    while (num != 0):
        result *=num
        num = num - 1
    print("The Factorial of ",num," is ", result)    

factorial()         