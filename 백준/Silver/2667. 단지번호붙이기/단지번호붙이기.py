# 2025.05.30 (금)
# 백준 2667 단지 번호 붙이기
# 실버 1

from collections import deque
import sys
read = sys.stdin.readline

# 지도의 크기
N = int(read())

# 지도
house_map = [ list(read().rstrip()) for _ in range(N) ]

def is_inside(x, y):
  return True if 0 <= x < N and 0 <= y < N else False

visited = [ [False] * N for _ in range(N) ]

def bfs(x, y):
  cnt = 1
  q = deque([(x, y)])
  visited[x][y] = True
  
  while q:
    x, y = q.popleft()
    
    for dx, dy in [ (-1, 0), (1, 0), (0, -1), (0, 1) ]:
      nx, ny = x + dx, y + dy
      
      if is_inside(nx, ny) and not visited[nx][ny] and house_map[nx][ny] == '1':
        q.append((nx, ny))
        visited[nx][ny] = True
        cnt += 1
  
  return cnt

total_num = 0
result = []

for i in range(N):
  for j in range(N):
    if not visited[i][j] and house_map[i][j] == '1':
      result.append(bfs(i, j))
      total_num += 1
      
result.sort()

print(total_num)
for r in result:
  print(r)