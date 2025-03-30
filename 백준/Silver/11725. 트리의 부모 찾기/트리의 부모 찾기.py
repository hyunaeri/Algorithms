# 2025.03.30 (일)
# 백준 11725 트리의 부모 찾기
# 실버 2

import sys
sys.setrecursionlimit(10**6)
read = sys.stdin.readline

def dfs(tree, parent, start):
  for next in tree[start]:
    if parent[next] == -1:
      parent[next] = start
      dfs(tree, parent, next)
      
N = int(read())
tree = [ [] for _ in range(N+1) ]
parent = [-1] * (N+1)

for _ in range(N-1):
  a,b = map(int, read().split())
  tree[a].append(b)
  tree[b].append(a)

dfs(tree, parent, 1)

for i in range(2, N+1):
  print(parent[i])