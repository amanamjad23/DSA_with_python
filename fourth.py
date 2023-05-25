def remove(stack):
    if len(stack) == 0:  
        return
    stack.pop()  
    remove(stack)  


S = [1, 21, 31, 41, 52]  
print("Stack S before removal:", S)

remove(S)

print("Stack S after removal:", S)
