list=[]
ch='y'
while ch=='y' :
    print("enter Element : ")
    element=input()
    list.append(element)
    print("Want to enter more elemnt \n YES or NO ")
    ch=input()
list.sort()
print(list)
print("The second largest elemnt in the list is ",list[-2])