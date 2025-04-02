# 2025.04.02 (수)
# 백준 1197 최소 스패닝 트리
# 골드 4

import heapq
import sys
read = sys.stdin.readline

def prim(start, graph, visited, priorityQueue):
  answer = 0
  visited[start] = True
  heapq.heapify(priorityQueue)
  
  for nextCost, nextNode in graph[start]:
    if not visited[nextNode]:
      heapq.heappush(priorityQueue, (nextCost, nextNode))
      
  while priorityQueue:
    cost, currentNode = heapq.heappop(priorityQueue)
    
    if visited[currentNode]: continue
    
    else:
      visited[currentNode] = True
      answer += cost
      
      for nextCost, nextNode in graph[currentNode]:
        if not visited[nextNode]:
          heapq.heappush(priorityQueue, (nextCost, nextNode))
          
  return answer

V,E = map(int, read().split())
graph = [ [] for _ in range(V+1) ]
visited = [False] * (V+1)
pq = []

for _ in range(E):
  u, v, w = map(int, read().split())
  graph[u].append((w, v))
  graph[v].append((w, u))

print(prim(1, graph, visited, pq))

