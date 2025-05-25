# 2025.05.25 (일)
# 백준 7562
# 실버 1

from collections import deque
import sys
read = sys.stdin.readline

def is_inside(x, y):
  return True if 0 <= x < row and 0 <= y < row else False

def bfs(row, init_x, init_y, goal_x, goal_y):
  q = deque([(init_x, init_y, 0)])
  visited = [ [False] * row for _ in range(row) ]
  visited[init_x][init_y] = True
  
  while q:
    x, y, cnt = q.popleft()
    
    if (x, y) == (goal_x, goal_y):
      return cnt
    
    # 대각선 8방향
    for dx, dy in [ (-2, -1), (-1, -2), (-2, 1), (-1, 2), (1, -2), (2, -1), (1, 2), (2, 1) ]:
      nx, ny = x + dx, y + dy
      
      if is_inside(nx, ny) and not visited[nx][ny]:
        q.append((nx, ny, cnt + 1))
        visited[nx][ny] = True
        
# 테스트 케이스 개수
case = int(read())

for _ in range(case):
  # 체스판의 한 변의 길이
  row = int(read())
  
  # 나이트 현재 위치
  knight_x, knight_y = map(int, read().split())
  
  # 나이트 목표 위치
  goal_x, goal_y = map(int, read().split())
  
  result = bfs(row, knight_x, knight_y, goal_x, goal_y)
  print(result)
