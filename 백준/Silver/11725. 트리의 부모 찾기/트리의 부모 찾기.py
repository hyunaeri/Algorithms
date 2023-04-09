# 백준 11725 트리의 부모 찾기
import sys
sys.setrecursionlimit(10**9)
read = sys.stdin.readline

# 노드의 개수
n = int(read().rstrip())
tree = [ [] for _ in range(n+1) ]
parent = [ -1 for _ in range(n+1) ]

# 트리 정보 업데이트
for _ in range(n-1):
    a,b = map(int, read().rstrip().split())
    tree[a].append(b)
    tree[b].append(a)

def dfs(start):
    for i in tree[start]:
        if parent[i] == -1:
            parent[i] = start
            dfs(i)

dfs(1)
for p in parent[2:]:
    print(p)