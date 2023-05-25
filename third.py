def interchange(SA, TA):
    while len(SA) > 0:
        TA.append(SA.pop())

SA = [1, 2, 3, 4, 5]  
TA = []  

interchange(SA, TA)

print("Stack TA after transfer:", TA)
