# 백준 10866 덱
from collections import deque
import sys
read = sys.stdin.readline

n = int(read())
dq = deque()

for _ in range(n):
    command = read().rstrip().split()

    if command[0] == 'push_front':
        dq.appendleft(command[1])
    
    elif command[0] == 'push_back':
        dq.append(command[1])
    
    elif command[0] == 'pop_front':
        if not dq:
            print("-1")
        else:
            print(dq.popleft())

    elif command[0] == 'pop_back':
        if not dq:
            print("-1")
        else:
            print(dq.pop())

    elif command[0] == 'size':
        print(len(dq))

    elif command[0] == 'empty':
        if not dq:
            print("1")
        else:
            print("0")

    elif command[0] == 'front':
        if not dq:
            print("-1")
        else:
            print(dq[0])

    elif command[0] == 'back':
        if not dq:
            print("-1")
        else:
            print(dq[-1])
    
