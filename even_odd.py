list=[4,5,9,3,8,6]
list_even=[]
list_odd=[]
for x in list:
    if x %2==0:
        list_even.append(x)
    else:
        list_odd.append(x)
print("even list is ",list_even)
print("odd list is ",list_odd)        