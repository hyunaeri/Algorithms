# 백준 1260 DFS와 BFS

from collections import deque
import sys
input = sys.stdin.readline

def DFS(start):
    visited[start] = 1
    print(start, end= " ")

    for i in graph[start]:
        if not visited[i]:
            DFS(i)


def BFS(start):
    queue = deque([start])
    visited[start] = 1

    while queue:
        v = queue.popleft()
        print(v, end = " ")

        for i in graph[v]:
            if not visited[i]:
                visited[i] = 1
                queue.append(i)



# 정점의 개수, 간선의 개수, 탐색을 시작할 정점의 번호
n,m,start = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

# 오름차순으로 방문해야 하므로, 정렬하기!
for i in graph:
    i.sort()

# DFS
visited = [0 for _ in range(n+1)]
DFS(start)

print()

# BFS
visited = [0 for _ in range(n+1)]
BFS(start)