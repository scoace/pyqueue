__author__ = 'andy'


from collections import deque

d=deque("ghi")

def printqueue(queue):
    for elem in queue:
      print(elem)

d.append('x')

printqueue(d)

d.pop()

printqueue(d)
print(d.maxlen)
d.clear()

printqueue(d)

d.appendleft('D')

printqueue(d)