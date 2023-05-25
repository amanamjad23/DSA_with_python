from collections import deque

deque = deque()

deque.appendleft(4)
deque.append(8)
deque.append(9)
deque.appendleft(5)
print(deque[-1])
deque.popleft()
deque.pop()
deque.append(7)
print(deque[0])
print(deque[-1])
deque.append(6)
deque.popleft()
deque.popleft()
