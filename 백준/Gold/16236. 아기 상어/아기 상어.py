# 백준 16236
# 골드 3
# https://www.acmicpc.net/problem/16236

from collections import deque
import sys
read = sys.stdin.readline

# 공간의 크기 N * N
N = int(read())

# 공간의 상태
space = [ list(map(int, read().rstrip().split())) for _ in range(N) ]

# 아기 상어 초기 좌표, 초기 크기
baby_x, baby_y, baby_size = -1, -1, 2

for i in range(N):
  for j in range(N):
    if space[i][j] == 9:
      baby_x, baby_y = i, j
      space[i][j] = 0

def get_possible_fish_list(start_x, start_y, shark_size):
  possible = []
  visited = [ [False] * N for _ in range(N) ]
  
  q = deque([(0, start_x, start_y)])
  visited[start_x][start_y] = True
  
  while q:
    dist, current_x, current_y = q.popleft()
    
    # 상하좌우로 이동가능
    for dx, dy in [ (-1,0), (1,0), (0,-1), (0,1) ]:
      nx, ny = current_x + dx, current_y + dy
      
      # 범위를 벗어나면
      if nx < 0 or nx >= N or ny < 0 or ny >= N:
        continue
      
      if not visited[nx][ny] and space[nx][ny] <= shark_size:
        q.append((dist + 1, nx, ny))
        visited[nx][ny] = True
        
        # 빈공간이 아니고 아기상어보다 크기가 작은 물고기만 섭취 가능
        if 0 < space[nx][ny] < shark_size:
          possible.append((dist + 1, nx, ny))
  
  return possible

answer = 0
eating_cnt = 0

while (True):
  current_fish_list = get_possible_fish_list(baby_x, baby_y, baby_size)

  # 엄마 상어 부르기 
  if len(current_fish_list) == 0:
    print(answer)
    exit(0)

  # 조건에 맞게 정렬, 타겟 물고기 좌표 받아오기
  current_fish_list.sort(key = lambda x: (x[0], x[1], x[2]))
  cost, cx, cy = current_fish_list[0]

  # 먹방 후 아기 상어 위치 변경 (1초 소요)
  space[cx][cy] = 0
  baby_x, baby_y = cx, cy
  eating_cnt += 1
  answer += cost

  if baby_size == eating_cnt:
    baby_size += 1
    eating_cnt = 0
