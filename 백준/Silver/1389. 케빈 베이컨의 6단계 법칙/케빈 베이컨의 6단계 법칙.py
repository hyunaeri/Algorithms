# 백준 1389 케빈 베이컨의 6단계 법칙
import sys
from collections import deque
read = sys.stdin.readline

# 유저의 수, 친구 관계의 수
N,M = map(int,read().rstrip().split())
graph = [ [] for _ in range(N+1) ]
kevin = [ 0 for _ in range(N+1) ]
visited = [ 0 for _ in range(N+1) ]
# print(visited)

def bfs(x,target):
    visited = [ 0 for _ in range(N+1) ]
    queue = deque()
    queue.append(x)

    while queue:
        x = queue.popleft()
        if x == target:
            return visited[x]

        for v in graph[x]:
            if visited[v] == 0:
                queue.append(v)
                visited[v] = visited[x] + 1

for _ in range(M):
    x, y = map(int,read().rstrip().split())
    graph[x].append(y)
    graph[y].append(x)

for i in range(1,N+1):
    sum = 0
    for j in range(1,N+1):
        sum += bfs(i,j)
    kevin[i] = sum


kevin_min = min(kevin[1:])

# 중복된 원소가 있으면 가장 작은 인덱스를 출력하는 index 함수
print(kevin.index(kevin_min))