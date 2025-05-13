# 2025.05.13(화)
# 백준 7576 토마토
# 골드 5

from collections import deque
import sys
read = sys.stdin.readline

# 상자의 가로 / 세로
M, N = map(int, read().split())
box = [ list(map(int, read().split())) for _ in range(N) ]
visited = [ [False] * M for _ in range(N) ]

def is_inside(x, y):
  return True if 0 <= x < N and 0 <= y < M else False

def all_ripe(box):
  for b in box:
    if 0 in b:
      return False
  return True

def bfs(tomatoes):
  q = deque(tomatoes)
  
  for x, y, _ in tomatoes:
    visited[x][y] = True
    
  days = 0
  
  while q:
    x, y, days = q.popleft()
    
    for dx, dy in [ (-1, 0), (1, 0), (0, -1), (0, 1) ]:
      nx, ny = x + dx, y + dy
      
      if is_inside(nx, ny) and box[nx][ny] == 0 and not visited[nx][ny]:
        box[nx][ny] = 1
        q.append((nx, ny, days + 1))
        visited[nx][ny] = True
  
  return days

# 처음부터 익은 토마토에 대한 정보
t = []
for i in range(N):
  for j in range(M):
    if box[i][j] == 1:
      t.append((i, j, 0))
      
if all_ripe(box):
  print(0)
  
else:
  answer = bfs(t)
  
  if all_ripe(box):
    print(answer)
    
  else:
    print(-1)