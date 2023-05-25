from collections import deque

Q = deque() 

for i in range(32):
    Q.append(i)

for i in range(10):
    try:
        first_value = Q[0]  
        print("First value: ",first_value)
    except IndexError:
        print("Queue is empty")


for i in range(15):
    try:
        Q.popleft()  
    except IndexError:
        print("Dequeue failed: queue is empty")

# get the current size of Q
current_size = len(Q)
print("Current size of Q: ",current_size)
