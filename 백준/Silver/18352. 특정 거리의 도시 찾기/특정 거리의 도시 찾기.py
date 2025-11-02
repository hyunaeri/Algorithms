# 백준 18352
# 실버 2
# https://www.acmicpc.net/problem/18352

from collections import deque
import sys
read = sys.stdin.readline

# 도시의 개수, 도로의 개수, 거리정보, 출발 도시의 번호
N, M, K, X = map(int, read().rstrip().split())

road = [ [] for _ in range(N+1) ]
visited = [False] * (N+1)

for _ in range(M):
  src, dst = map(int, read().rstrip().split())
  road[src].append(dst)
  
answer = []

def bfs(start):
  q = deque([(start, 0)])
  visited[start] = True
  
  while q:
    current_node, dist = q.popleft()
    
    if dist == K:
      answer.append(current_node)
    
    for next_node in road[current_node]:
      if not visited[next_node]:
        q.append((next_node, dist + 1))
        visited[next_node] = True

bfs(X)
answer = sorted(answer)    

if len(answer) == 0: print(-1)
else: print(*answer)
