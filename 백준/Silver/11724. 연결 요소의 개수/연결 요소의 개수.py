# 백준 11724 연결요소의 개수
import sys
sys.setrecursionlimit(10**5)
read= sys.stdin.readline

# 정점의 수, 간선의 수
n,m = map(int, read().split())
graph = [ [] for _ in range(n+1) ]
visited = [False] * (n+1) 
ans = 0

def dfs(start):
    visited[start] = True

    for v in graph[start]:
        if not visited[v]:
            dfs(v)


for _ in range(m):
    x,y = map(int,read().split())
    graph[x].append(y)
    graph[y].append(x)

# 전체 순회
for i in range(1,n+1):
    if not visited[i]:
        # 방문하지는 않았으나 연결된 요소가 없으면
        if not graph[i]:
            ans += 1
            visited[i] = True
        else:
            dfs(i)
            ans += 1

print(ans)