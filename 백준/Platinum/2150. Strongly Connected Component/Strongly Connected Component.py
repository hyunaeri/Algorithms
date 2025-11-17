# 백준 2150
# 플레티넘 5
# https://www.acmicpc.net/problem/2150

import sys
read = sys.stdin.readline
sys.setrecursionlimit(10**4)


def dfs(graph, visited, stack, v):
    visited[v] = True

    for next in graph[v]:
        if not visited[next]:
            dfs(graph, visited, stack, next)

    # 모든 인접 정점 방문 후 스택에 push
    stack.append(v)


def reversed_dfs(graph, visited, scc, v):
    visited[v] = True
    
    # SCC 집합에 추가
    scc.append(v)

    for next in graph[v]:
        if not visited[next]:
            reversed_dfs(graph, visited, scc, next)


if __name__ == '__main__':
  
  # 정점, 간선의 개수
  V, E = map(int, read().rstrip().split())
  
  graph = [ [] for _ in range(V + 1) ]
  reversed_graph = [ [] for _ in range(V + 1) ]
  
  for _ in range(E):
    A, B = map(int, read().rstrip().split())
    graph[A].append(B)
    reversed_graph[B].append(A)
    
  visited = [False] * (V + 1)
  stack = []
  
  # 원래 그래프에서 DFS
  for i in range(1, V + 1):
    if not visited[i]: 
      dfs(graph, visited, stack, i)
  
  # 역방향 그래프에서 stack 순서대로 DFS (SCC 구하기)
  reversed_visited = [False] * (V + 1)
  scc_list = []
  
  while stack:
    current_node = stack.pop()
    
    if not reversed_visited[current_node]:
      scc = []
      reversed_dfs(reversed_graph, reversed_visited, scc, current_node)
      scc.sort()
      scc_list.append(scc)
  
  # 여러개의 SCC에 대해서 정렬
  scc_list.sort(key = lambda x: x[0])
  
  print(len(scc_list))
  
  for scc in scc_list:
    print(*scc, end=' ')
    print(-1)