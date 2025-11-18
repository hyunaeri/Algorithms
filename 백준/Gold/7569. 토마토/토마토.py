# 백준 7569
# 골드 5
# https://www.acmicpc.net/problem/7569

from collections import deque
import sys
read = sys.stdin.readline

def bfs(tomatoes):
  global R, C, H, box_info
  
  q = deque(tomatoes)
  time = 0
  
  while q:
    z, x, y, time = q.popleft()
    
    # 위, 아래, 상, 하, 좌, 우
    for dz, dx, dy in [ (-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1) ]:
      nz, nx, ny = z + dz, x + dx, y + dy
      
      # 범위 내에 존재
      if 0 <= nz < H and 0 <= nx < C and 0 <= ny < R:
        # 미 방문이면서 다음 칸에 안 익은 토마토 존재
        if box_info[nz][nx][ny] == 0:
          box_info[nz][nx][ny] = 1
          q.append((nz, nx, ny, time + 1))
  
  return time

if __name__ == '__main__':
  
  # 상자의 가로, 세로, 높이
  R, C, H = map(int, read().rstrip().split())
  
  # 토마토 상자 정보 (0 : 안 익은 토마토, 1 : 익은 토마토, -1 : 빈 칸)
  box_info = [ [ list(map(int, read().rstrip().split())) for _ in range(C) ] for _ in range(H) ]
  
  # 초기 익은 토마토 위치 미리 담기
  tomatoes = []
  has_raw = False
  
  for h in range(H):
    for c in range(C):
      for r in range(R):
        if box_info[h][c][r] == 0:
          has_raw = True
        
        if box_info[h][c][r] == 1:
          tomatoes.append((h, c, r, 0))
  
  # 처음부터 모든 토마토가 익어 있는 경우
  if not has_raw:
    print(0)
    exit(0)
  
  # BFS
  answer = bfs(tomatoes)
  
  # 익지 않은 토마토가 남은 경우
  for h in range(H):
    for c in range(C):
      for r in range(R):
        if box_info[h][c][r] == 0:
          print(-1)
          exit(0)
  
  print(answer)