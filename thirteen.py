from collections import deque

D = deque([1, 2, 3, 4, 5, 6, 7, 8])
Q = deque()

Q.append(D.popleft())  

Q.append(D.popleft())  
Q.append(D.popleft())  

Q.append(D.popleft())  

Q.append(D.popleft())  

Q.append(D.popleft())  

Q.append(D.popleft())  
Q.append(D.popleft())  

while Q:
    D.append(Q.popleft())  

print(D)  
