# 백준 11403 경로 찾기
# DFS

import sys
sys.setrecursionlimit(10**5)
read = sys.stdin.readline

# 정점의 개수
n = int(read().rstrip())
matrix = [ list(map(int,read().rstrip().split())) for _ in range(n) ]
visited = [0] * n

def dfs(x):
    for i in range(n):
        if matrix[x][i] == 1 and visited[i] == 0:
            visited[i] = 1
            dfs(i)

for i in range(n):
    dfs(i)
    for j in range(n):
        if visited[j] == 1:
            print(1, end=' ')
        else:
            print(0, end=' ')
    print()
    visited = [0 for _ in range(n)]
