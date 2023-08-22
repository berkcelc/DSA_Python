from collections import deque

q = deque(maxlen=3)

q.append(1)
q.append(2)
q.append(3)
print(q)
q.append(4)
print(q)
q.pop()
q.popleft()
q.clear()


import queue as q

q1 = q.Queue(maxsize=3)

q1.qsize()
q1.put(1)
q1.put(2)
q1.put(3)
# q1.put(3)


print('hello')