# 2025.05.14 (수)
# 백준 4179 불!
# 골드 3

from collections import deque
import sys
read = sys.stdin.readline

# 세로, 가로
R, C = map(int, read().split())

# 벽 : #
# 지나갈 수 있는 공간 : .
# 지훈이의 초기 위치 : J
# 불이 난 공간 : F
maze = [ list(read().rstrip()) for _ in range(R) ]
visited = [ [False] * C for _ in range(R) ]

jihun, fire = deque(), deque()

# 초기 지훈이의 위치, 불이 난 공간 체크
for i in range(R):
  for j in range(C):
    if maze[i][j] == 'J':
      jihun.append((i, j, 0))
      maze[i][j] = '.'
    
    elif maze[i][j] == 'F':
      fire.append((i, j))
      
def is_inside(x, y):
  return True if 0 <= x < R and 0 <= y < C else False

def burn():
  for _ in range(len(fire)):
    x, y = fire.popleft()
    
    for dx, dy in [ (-1, 0), (1, 0), (0, -1), (0, 1) ]:
      nx, ny = x + dx, y + dy
      
      # 미로 범위 안이면서 지나갈 수 있는 공간에만 불이 옮겨 붙을 수 있음
      if is_inside(nx, ny) and maze[nx][ny] == '.':
        maze[nx][ny] = 'F'
        fire.append((nx, ny))

def bfs():
  time = 0
  
  while jihun:
    # 불 번짐 → 지훈 이동 완료 
    burn()
    
    for _ in range(len(jihun)):
      x, y, time = jihun.popleft()

      # 미로 가장 자리인 경우 = 탈출
      if x == 0 or x == R-1 or y == 0 or y == C-1:
        print(time + 1)
        return
      
      for dx, dy in [ (-1, 0), (1, 0), (0, -1), (0, 1) ]:
        nx, ny = x + dx, y + dy
        
        # 미로 범위 안이면서 지나갈 수 있는 공간에만 지훈이가 이동할 수 있음
        if is_inside(nx, ny) and maze[nx][ny] == '.' and not visited[nx][ny]:
          jihun.append((nx, ny, time + 1))
          visited[nx][ny] = True
    
    
  print('IMPOSSIBLE')
  return 

bfs()