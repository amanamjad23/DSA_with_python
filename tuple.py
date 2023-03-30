fruits = ('banana', 'orange', 'mango', 'lemon')
print('orange' in fruits) # True
print('apple' in fruits) # False
fruits=list(fruits)
fruits[0]='apple'
print('banana' in fruits) 
print('apple' in fruits) 




print("the last element after converting tuple into list is ",fruits[-1])