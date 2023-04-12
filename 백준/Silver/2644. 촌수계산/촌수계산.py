# 백준 2644 촌수 계산
# BFS

import sys
from collections import deque
read = sys.stdin.readline

# 전체 사람의 수
n = int(read())
family = [ [] for _ in range(n+1) ]
visited = [ 0 for _ in range(n+1) ]

# 촌수를 계산 해야하는 두 사람의 번호
a,b = map(int,read().rstrip().split())

# 부모 자식간의 관계 개수
c = int(read())

for _ in range(c):
    x,y = map(int,read().rstrip().split())
    family[x].append(y)
    family[y].append(x)

def bfs(x):
    queue = deque()
    queue.append(x)

    # 자기 자신은 0촌이므로 visted[x] = 1을 하지 않음
    # visited[x] = 1

    while queue:
        x = queue.popleft()
        for node in family[x]:
            if visited[node] == 0:
                visited[node] = visited[x] + 1
                queue.append(node)

bfs(a)
print(visited[b] if visited[b] > 0 else -1)