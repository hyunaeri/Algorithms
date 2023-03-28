# 백준 11866 요세푸스 문제 0
from collections import deque
import sys
read = sys.stdin.readline

# 사람 수, 제거되는 순번
n,k = map(int, read().rstrip().split())
queue = deque([ i for i in range(1,n+1) ])

# 제거된 순서
removed = []

while queue:
    # k-2번 까지는 다시 뒤로 보내야함.
    for _ in range(k-1):
        queue.append(queue.popleft())
    removed.append(queue.popleft())


print("<", end='')
print(*removed, sep=', ', end = '')
print(">")
