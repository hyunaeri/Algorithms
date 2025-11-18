# 백준 4196
# 플레티넘 4
# https://www.acmicpc.net/problem/4196

import sys
read = sys.stdin.readline
sys.setrecursionlimit(10**6)

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
  
  T = int(read())
  
  for _ in range(T):
    
    # 도미노 개수, 관계의 개수
    N, M = map(int, read().rstrip().split())
    
    # 도미노 정보 (기존 그래프 / 역 그래프)
    domino = [ [] for _ in range(N + 1) ]
    reversed_domino = [ [] for _ in range(N + 1) ]
    
    for _ in range(M):
      a, b = map(int, read().rstrip().split())
      domino[a].append(b)
      reversed_domino[b].append(a)
    
    # 첫 번째 DFS
    visited = [False] * (N + 1)
    stack = []
    
    for i in range(1, N + 1):
      if not visited[i]:
        dfs(domino, visited, stack, i)
    
    # 두 번째 DFS
    reversed_visited = [False] * (N + 1)
    scc_list = []
    
    while stack:
      current_vertex = stack.pop()
      
      if not reversed_visited[current_vertex]:
        scc = []
        reversed_dfs(reversed_domino, reversed_visited, scc, current_vertex)
        scc_list.append(scc)
    
    # 각 정점 에 해당하는 SCC 넘버링
    scc_idx = [0] * (N + 1)
    
    for idx, scc in enumerate(scc_list):
      for v in scc:
        scc_idx[v] = idx
    
    # 각 SCC 에서 들어오는 간선이 있는지 체크
    indegree = [False] * len(scc_list)
    
    for i in range(1, N + 1):
      for next in domino[i]:
        if scc_idx[i] != scc_idx[next]:
          indegree[scc_idx[next]] = True
    
    # 외부 SCC 에서 들어오는 간선이 없는 SCC 개수 : 손으로 넘어뜨려야 하는 최소 도미노 블럭 개수
    answer = 0
    
    for check in indegree:
      if not check: answer +=1
    
    print(answer)