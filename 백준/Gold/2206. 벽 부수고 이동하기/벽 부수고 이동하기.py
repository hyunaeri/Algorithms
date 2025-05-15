# 2025.05.15 (목)
# 백준 2206 벽 부수고 이동하기
# 골드 3

from collections import deque
import sys
read = sys.stdin.readline

# N * M 크기의 행렬
N, M = map(int, read().split())

# 0 : 이동할 수 있는 곳
# 1 : 벽
board = [ list(read().rstrip()) for _ in range(N) ]
visited = [ [ [False] * M for _ in range(N) ] for _ in range(2) ]

def is_inside(x, y):
  return True if 0 <= x < N and 0 <= y < M else False

def bfs(x, y):
  q = deque([(x, y, 0, 1)])
  visited[0][x][y] = True
  
  while q:
    x, y, check, count = q.popleft()
    
    if (x, y) == (N-1, M-1):
      return count
    
    for dx, dy in [ (-1, 0), (1, 0), (0, -1), (0, 1) ]:
      nx, ny = x + dx, y + dy
      
      if is_inside(nx, ny):
        # 벽을 아직 안 부쉈고, 다음이 벽이면 부수고 진행
        if board[nx][ny] == '1' and check == 0 and not visited[1][nx][ny]:
          visited[1][nx][ny] = True
          q.append((nx, ny, 1, count + 1))
        
        # 다음이 이동할 수 있는 공간인 경우
        elif board[nx][ny] == '0' and not visited[check][nx][ny]:
          visited[check][nx][ny] = True
          q.append((nx, ny, check, count + 1))
          
  return -1

print(bfs(0, 0))