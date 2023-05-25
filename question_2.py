S = []  

for i in range(25):
    S.append(i)


for i in range(12):
    try:
        top_value = S[-1]  
        print("Top value:", top_value)
    except IndexError:
        print("Stack is empty")


for i in range(10):
    try:
        S.pop(S[-1]) 
    except IndexError:
        print("Pop failed: stack is empty")

# get the current size of S
current_size = len(S)
print("Current size of S: ",current_size)