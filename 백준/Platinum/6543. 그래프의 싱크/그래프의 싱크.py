# 백준 6543
# 플레티넘 4
# https://www.acmicpc.net/problem/6543

import sys
read = sys.stdin.readline
sys.setrecursionlimit(10**4)

def dfs(graph, visited, stack, v):
  visited[v] = True
  
  for next in graph[v]:
    if not visited[next]:
      dfs(graph, visited, stack, next)
  
  stack.append(v)

def reversed_dfs(graph, visited, scc, v):
  visited[v] = True
  scc.append(v)
  
  for next in graph[v]:
    if not visited[next]:
      reversed_dfs(graph, visited, scc, next)

if __name__ == '__main__':
  
  while True:
    
    command = list(map(int, read().rstrip().split()))
    
    if len(command) == 1:
      exit(0)
      
    # 노드의 수, 간선의 수
    V, E = command[0], command[1]
    
    graph = [ [] for _ in range(V + 1) ]
    reversed_graph = [ [] for _ in range(V + 1) ]
    
    # 간선의 정보 한번에 받기
    edges = list(map(int, read().rstrip().split()))
    
    for i in range(0, len(edges), 2):
      a, b = edges[i], edges[i + 1]
      graph[a].append(b)
      reversed_graph[b].append(a)
    
    # 원래 그래프에서 첫 DFS
    visited = [False] * (V + 1)
    stack = []
    
    for i in range(1, V + 1):
      if not visited[i]:
        dfs(graph, visited, stack, i)
    
    # 역방향 그래프에서 두번째 DFS (SCC 찾기)
    reversed_visited = [False] * (V + 1)
    scc_list = []
    
    while stack:
      current_vertex = stack.pop()
      
      if not reversed_visited[current_vertex]:
        scc = []
        reversed_dfs(reversed_graph, reversed_visited, scc, current_vertex)
        scc_list.append(scc)
      
    # 각 정점이 어느 SCC에 속하는지 넘버링
    scc_idx = [0] * (V + 1)
    for idx, scc in enumerate(scc_list):
      for v in scc:
        scc_idx[v] = idx
    
    # 각 SCC에서 다른 SCC로 나가는 간선이 있는지 체크
    outdegree = [False] * len(scc_list)
    
    for i in range(1, V + 1):
      for next in graph[i]:
        if scc_idx[i] != scc_idx[next]:
          outdegree[scc_idx[i]] = True
    
    # Outdegree가 0인 SCC에 포함된 정점들만 수집
    answer = []
    for i in range(1, V + 1):
      if not outdegree[scc_idx[i]]:
        answer.append(i)
    
    if answer: print(*answer)