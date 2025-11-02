# 백준 18352
# 실버 2
# https://www.acmicpc.net/problem/18352

from collections import deque
import sys
read = sys.stdin.readline

# 도시의 개수, 도로의 개수, 거리정보, 출발 도시의 번호
N, M, K, X = map(int, read().rstrip().split())

road = [ [] for _ in range(N+1) ]
dist = [-1] * (N+1)

for _ in range(M):
  src, dst = map(int, read().rstrip().split())
  road[src].append(dst)

def bfs(start):
  q = deque([start])
  dist[start] = 0
  
  while q:
    current_node = q.popleft()
    
    if dist[current_node] == K:
      continue
    
    for next_node in road[current_node]:
      if dist[next_node] == -1:
        q.append((next_node))
        dist[next_node] = dist[current_node] + 1

bfs(X)

answer = []
for i in range(1, N+1):
  if dist[i] == K:
    answer.append(i)  

if len(answer) == 0: print(-1)
else: print(*answer)
