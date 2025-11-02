# 백준 1926
# 실버 1
# https://www.acmicpc.net/problem/1926

from collections import deque
import sys
read = sys.stdin.readline

# 도화지 세로, 가로
n, m = map(int, read().rstrip().split())

# 그림 정보
pic = [ list(map(int, read().rstrip().split())) for _ in range(n) ]
visited = [ [False] * m for _ in range(n) ]

def is_inside(x, y):
  return 1 if 0 <= x < n and 0 <= y < m else 0


def bfs(sx, sy):
  q = deque([(sx, sy)])
  visited[sx][sy] = True
  size = 0
  
  while q:
    x, y = q.popleft()
    size += 1
    
    for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
      nx, ny = x + dx, y + dy
      
      if is_inside(nx, ny):
        if pic[nx][ny] == 1 and not visited[nx][ny]:
          q.append((nx, ny))
          visited[nx][ny] = True
        
  return size

max_size = 0
pic_cnt = 0

for i in range(n):
  for j in range(m):
    if pic[i][j] == 1 and not visited[i][j]:
      max_size = max(max_size, bfs(i, j))
      pic_cnt += 1

print(pic_cnt, max_size, sep='\n')
