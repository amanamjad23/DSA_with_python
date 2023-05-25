def reverse_list(elements):
    stack = []  
    for element in elements:
        stack.append(element)

    index = 0
    while len(stack) > 0:
        elements[index] = stack.pop()
        index += 1

my_list = [1, 2, 3, 4, 5] 
print("Original list:", my_list)

reverse_list(my_list)

print("Reversed list:", my_list)
