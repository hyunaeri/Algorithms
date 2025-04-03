# 2025.04.03 (목)
# 백준 16236 아기 상어
# 골드 3

from collections import deque
import sys
read = sys.stdin.readline

# 공간의 크기 N*N / 공간의 상태
N = int(read())
space = [ list(map(int, read().split())) for _ in range(N) ]
answer = 0

def bfs(x, y, baby_size):
  can_eat_fish_list = []
  visited = [ [False] * N for _ in range(N) ]
  q = deque([(0, x, y)])
  visited[x][y] = True
  
  while q:
    dist, x, y = q.popleft()
    
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
      nx, ny = x + dx, y + dy
      
      # 공간의 범위를 벗어나지 않고, 미 방문한 곳이라면
      if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
        # 빈칸이거나 아기 상어와 크기가 같거나 작은 물고기 방향으로만 이동 가능
        if space[nx][ny] <= baby_size:
          q.append((dist + 1, nx, ny))
          visited[nx][ny] = True
          
          # 빈칸이 아니고, 아기 상어보다 작은 물고기만 먹을 수 있음
          if 0 < space[nx][ny] < baby_size:
            can_eat_fish_list.append((dist + 1, nx, ny))
  
  return can_eat_fish_list

# 초기 아기 상어의 위치, 크기
baby_x, baby_y, baby_size = 0, 0, 2

for i in range(N):
  for j in range(N):
    if space[i][j] == 9:
      baby_x, baby_y = i, j
      space[i][j] = 0
      break

# 먹방 시작
eating_count = 0

while True:
  can_eat_fish_list = bfs(baby_x, baby_y, baby_size)
  
  # 먹을 수 있는 물고기가 없다면 종료
  if not can_eat_fish_list:
    break
  
  # 먹을 수 있는 물고기 중 가장 가까운 물고기 찾기 (거리, x좌표, y좌표)
  can_eat_fish_list.sort(key = lambda x: (x[0], x[1], x[2]))
  dist, fish_x, fish_y = can_eat_fish_list[0]
  
  # 아기 상어의 위치 업데이트
  baby_x, baby_y = fish_x, fish_y
  space[fish_x][fish_y] = 0
  eating_count += 1
  answer += dist
  
  # 아기 상어의 크기 증가
  if baby_size == eating_count:
    baby_size += 1
    eating_count = 0
    
print(answer)