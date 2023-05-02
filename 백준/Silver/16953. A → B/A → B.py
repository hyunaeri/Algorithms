# 백준 16953 A+B
import sys
from collections import deque
read = sys.stdin.readline

A,B = map(int,read().split())

def bfs(x):
    queue = deque()
    queue.append([x,0])

    while queue:
        x,cnt = queue.popleft()
        if x == B:
            return cnt + 1
        
        for nx in [2*x, 10*x+1]:
            if 0 <= nx <= B:
                queue.append([nx,cnt+1])

    return -1

print(bfs(A))