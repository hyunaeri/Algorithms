# 2025.04.01 (화)
# 백준 2468 안전 영역
# 실버 1

from collections import deque
import sys
read = sys.stdin.readline

def BFS(x, y, visited, limit):
  q = deque([(x, y)])
  visited[x][y] = True
  
  while q:
    x, y = q.popleft()
    
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
      nx, ny = x + dx, y + dy
      
      if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
        if region[nx][ny] > limit:
          visited[nx][ny] = True
          q.append((nx, ny))

N = int(read())
region = [ list(map(int, read().split())) for _ in range(N) ]

maxHeight = 0
for r in region:
  maxHeight = max(maxHeight, max(r))

answer = 0

for h in range(maxHeight):
  safeArea = 0
  visited = [ [False] * N for _ in range(N) ]
  
  for i in range(N):
    for j in range(N):
      if region[i][j] > h and not visited[i][j]:
        BFS(i, j, visited, h)
        safeArea += 1
        
  answer = max(answer, safeArea)
  
print(answer)