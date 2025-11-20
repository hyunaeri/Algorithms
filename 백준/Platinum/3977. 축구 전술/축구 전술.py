# 백준 3977
# 플레티넘 4
# https://www.acmicpc.net/problem/3977

import sys
read = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(g, visited, stack, v):
  visited[v] = True
  
  for next in g[v]:
    if not visited[next]:
      dfs(g, visited, stack, next)
  
  stack.append(v)

def reversed_dfs(g, visited, scc, v):
  visited[v] = True
  scc.append(v)
  
  for next in g[v]:
    if not visited[next]:
      reversed_dfs(g, visited, scc, next)

def read_non_empty_line():
    line = read()
    while line is not None and line.strip() == "":
        line = read()
    return line

if __name__ == '__main__':
  
  T = int(read())
  
  for _ in range(T):
    
    line = read_non_empty_line()
    
    # 구역의 수, 움직임의 수
    N, M = map(int, line.split())
    
    area = [ [] for _ in range(N) ]
    reversed_area = [ [] for _ in range(N) ]
    
    for _ in range(M):
      A, B = map(int, read().split())
      area[A].append(B)
      reversed_area[B].append(A)
    
    # 첫 번째 DFS 수행
    visited = [False] * N
    stack = []
    
    for i in range(N):
      if not visited[i]:
        dfs(area, visited, stack, i)
    
    # 두 번째 DFS 수행
    reversed_visited = [False] * N
    scc_list = []
    
    while stack:
      current_node = stack.pop()
      
      if not reversed_visited[current_node]:
        scc = []
        reversed_dfs(reversed_area, reversed_visited, scc, current_node)
        scc_list.append(scc)
    
    # for scc in scc_list:
    #   print(scc)
    
    # 각 정점에 대해 SCC 넘버링
    scc_idx = [-1] * N
    
    for idx, scc in enumerate(scc_list):
      for v in scc:
        scc_idx[v] = idx
    
    indegree = [0] * len(scc_list)
    
    # 원래 그래프의 모든 간선을 돌면서 서로 다른 SCC 사이의 간선만 카운트
    for u in range(N):
        for v in area[u]:
            if scc_idx[u] != scc_idx[v]:
                indegree[scc_idx[v]] += 1
    
    # 진입 차수가 0인 SCC 찾기
    zero_indegree_scc = [idx for idx, deg in enumerate(indegree) if deg == 0]
    
    if len(zero_indegree_scc) != 1:
        print("Confused")
        print()
        continue
    
    target_scc = zero_indegree_scc[0]

    # 해당 SCC에 포함된 원래 정점들을 모두 모아서 오름차순 출력
    answer_nodes = [v for v in range(N) if scc_idx[v] == target_scc]
    answer_nodes.sort()
    
    for node in answer_nodes:
      print(node)
    
    # 테스트 케이스 사이에 빈 줄 하나 출력
    print()