# 백준 1976 여행가자
import sys
read = sys.stdin.readline

# 도시의 수, 여행 계획에 속한 도시의 수
N = int(read())
M = int(read())
city = [ [] for _ in range(N+1) ]

def dfs(x):
    visited[x] = True

    for node in city[x]:
        if not visited[node]:
            dfs(node) 

for i in range(1, N+1):
    temp = list(map(int,read().split()))
    for j in range(len(temp)):
        if temp[j] == 1:
            city[i].append(j+1)

travel = list(map(int,read().split()))
visited = [False] * (N+1)
result = True
dfs(travel[0])

for check in travel:
    if not visited[check]:
        result = False

print("YES" if result else "NO")

