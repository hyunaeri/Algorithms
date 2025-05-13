# 2025.05.13 (화)
# 백준 2178 미로 탐색
# 실버 1
from collections import deque
import sys
read = sys.stdin.readline

# 세로 / 가로
N,M = map(int, read().split())

# 미로 입력
maze = [ list(map(int, read().rstrip())) for _ in range(N) ]
visited = [ [False] * M for _ in range(N) ]

def is_inside(x, y):
  return True if 0 <= x < N and 0 <= y < M else False

def bfs(x, y):
  q = deque([(x, y, 1)])
  visited[x][y] = True
  
  while q:
    x, y, count = q.popleft()
    
    if (x, y) == (N-1, M-1):
      return count
    
    for dx, dy in [ (-1, 0), (1, 0), (0, -1), (0, 1) ]:
      nx, ny = x + dx, y + dy
      
      if is_inside(nx, ny):
        if maze[nx][ny] == 1 and not visited[nx][ny]:
          q.append((nx, ny, count + 1))
          visited[nx][ny] = True

print(bfs(0,0))