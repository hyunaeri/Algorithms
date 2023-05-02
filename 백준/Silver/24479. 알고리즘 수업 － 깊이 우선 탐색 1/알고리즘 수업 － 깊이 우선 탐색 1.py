# 백준 24479 알고리즘 수업 - 깊이 우선 탐색 1

import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def DFS(start):
    global count
    count += 1
    visited[start] = count

    for i in graph[start]:
        if not visited[i]:
            DFS(i)

# 정점의 수, 간선의 수, 시작 정점
n,m,start = map(int, input().split())
count = 0
graph = [ [] for _ in range(n+1)]
visited = [ 0 for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

# 오름차순으로 방문해야 하므로, 정렬
for i in graph:
    i.sort()

# DFS
DFS(start)

for i in range(1,n+1):
    print(visited[i])
