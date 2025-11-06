# 백준 10026
# 골드 5
# https://www.acmicpc.net/problem/10026

from collections import deque
import sys
read = sys.stdin.readline

def solution(x, y, N, space, visited):
  q = deque([(x, y)])
  visited[x][y] = True
  
  while q:
    x, y = q.popleft()
    current_color = space[x][y]
    
    for dx, dy in [ (-1, 0), (1, 0), (0, -1), (0, 1) ]:
      nx, ny = x + dx, y + dy
      
      if nx < 0 or nx >= N or ny < 0 or ny >= N:
        continue
      
      next_color = space[nx][ny]
      
      if not visited[nx][ny] and current_color == next_color:
        q.append((nx, ny))
        visited[nx][ny] = True

if __name__ == "__main__":
  general = 0
  disabled = 0
  
  # N * N 크기의 공간
  N = int(read())
  
  # 그림 정보
  paint = [ read().rstrip() for _ in range(N) ]
  visited = [ [False] * N for _ in range(N) ]
  
  for i in range(N):
    for j in range(N):
      if not visited[i][j]:
        solution(i, j, N, paint, visited)
        general += 1
  
  paint_revise = [row.replace('G', 'R') for row in paint]
  visited = [ [False] * N for _ in range(N) ]
  
  for i in range(N):
    for j in range(N):
      if not visited[i][j]:
        solution(i, j, N, paint_revise, visited)
        disabled += 1
  
  print(general, disabled)