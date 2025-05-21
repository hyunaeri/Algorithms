# 2025.05.21 (수)
# 백준 14502 연구소
# 골드 4

from collections import deque
from itertools import combinations
import sys
read = sys.stdin.readline

# [세로 / 가로]
N, M = map(int, read().split())

# [지도 정보]
# 빈 칸 : 0
# 벽 : 1
# 바이러스 위치 : 2
map = [ list(map(int,read().split())) for _ in range(N) ]

# 벽을 세울 수 있는 공간 리스트, 초기 바이러스 위치
possible = []
virus = []
for i in range(N):
  for j in range(M):
    if map[i][j] == 0:
      possible.append((i, j))
    elif map[i][j] == 2:
      virus.append((i, j))

# 최대 64C3 = 41664
combinations_wall = list(combinations(possible, 3))

def is_inside(x, y):
  return True if 0 <= x < N and 0 <= y < M else False

# 안전 영역 계산
def calc_safety_space(maps):
  result = 0  
  for m in maps:
    for space in m:
      if space == 0:
        result += 1
  return result

answer = 0

def bfs():
  global answer
  
  for combination in combinations_wall:
    q = deque(virus)
    copy_map = [ row[:] for row in map ]
    visited = [ [False] * M for _ in range(N) ]
    
    for x, y in combination:
      copy_map[x][y] = 1

    # 초기 바이러스 방문 처리
    for x, y in virus:
      visited[x][y] = True

    while q:
      x, y = q.popleft()
      
      for dx, dy in [ (-1, 0), (1, 0), (0, -1), (0, 1) ]:
        nx, ny = x + dx, y + dy
        
        # 지도의 범위를 벗어나지 않고
        if is_inside(nx, ny):
          # 미 방문 공간이면서 빈 칸인 경우
          if not visited[nx][ny] and copy_map[nx][ny] == 0:
            copy_map[nx][ny] = 2
            visited[nx][ny] = True
            q.append((nx, ny))

    answer = max(answer, calc_safety_space(copy_map))
  
  return answer

print(bfs())