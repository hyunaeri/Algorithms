# 백준 2606 바이러스
import sys
read = sys.stdin.readline

def DFS(start):
    global count
    visited[start] = 1

    for i in graph[start]:
        if not visited[i]:
            count += 1
            DFS(i)

n = int(read())
m = int(read())
graph = [ [] for _ in range(n+1) ]
visited = [ 0 for _ in range(n+1) ]
count = 0

for _ in range(m):
    x, y = map(int, read().split())
    graph[x].append(y)
    graph[y].append(x)

DFS(1)
print(count)