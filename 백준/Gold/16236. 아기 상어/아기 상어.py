# 백준 16236 아기상어
# 2020 삼성 SW 역량 테스트 기출 문제
import sys
from collections import deque
read = sys.stdin.readline

# 아기 상어가 돌아다니는 공간은 N * N 크기의 정사각형
N = int(read())

# 공간의 상태
# 0: 빈 칸
# 1, 2, 3, 4, 5, 6: 칸에 있는 물고기의 크기
# 9: 아기 상어의 위치
space = [ list(map(int,read().rstrip().split())) for _ in range(N) ]
shark_x, shark_y = 0, 0

# 아기 상어의 위치를 미리 담아줌
for i in range(len(space)):
    for j in range(len(space[i])):
        if space[i][j] == 9:
            space[i][j] = 0
            shark_x, shark_y = i,j
            break
            

# 아기상어의 최초 크기
shark_size = 2
# 아기상어가 먹은 물고기 수
shark_eat = 0

# 먹을 수 있는 물고기들의 거리를 담은 리스트를 반환해주는 함수
def find_eat_fish(x,y):
    global shark_size

    # 방문 여부, 거리, 먹을 수 있는 물고기를 담을 리스트
    visited = [ [False]*N for _ in range(N) ]
    distance = [ [0]*N for _ in range(N) ]
    can_eat_fish = []

    queue = deque()
    queue.append((x,y))

    while queue:
        x,y = queue.popleft()

        # 아기상어는 상하좌우 이동이 가능하다
        for dx, dy in [ (-1,0),(1,0),(0,-1),(0,1) ]:
            nx, ny = x + dx, y + dy

            # 공간을 벗어난 곳을 탐색 시
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue

            # 아기상어보다 작거나 같은 물고기를 만났거나, 빈칸이면 이동이 가능하다
            if space[nx][ny] <= shark_size and not visited[nx][ny]:
                visited[nx][ny] = True
                distance[nx][ny] = distance[x][y] + 1
                queue.append((nx,ny))

                # 물고기를 만났는데 아기상어보다 작다면 먹을 수 있는 물고기이므로 리스트에 담아준다
                if space[nx][ny] != 0 and space[nx][ny] < shark_size:
                    can_eat_fish.append([distance[nx][ny], nx, ny])

    # 탐색이 끝이 나면 조건 순으로 정렬을 해준다
    # 거리가 짧은 순, x좌표가 작은 순, y좌표가 작은 순서로 정렬한다
    can_eat_fish.sort(key = lambda x: (x[0], x[1], x[2]))

    return can_eat_fish

answer = 0

while True:
    # 거리, x, y좌표 순으로 원소가 들어 있음
    can_eat_fish = find_eat_fish(shark_x, shark_y)

    if len(can_eat_fish) == 0:
        print(answer)
        exit(0)

    # 먹을 수 있는 물고기 리스트는 정렬 되어 있기 때문에 맨 앞의 물고기부터 잡아 먹는다
    move_time, shark_x, shark_y = can_eat_fish[0]

    shark_eat += 1
    # 먹다 보니 자신의 크기 만큼 먹었다면 본인의 몸집 크기 증가
    if shark_eat == shark_size:
        shark_size += 1
        shark_eat = 0

    # 물고기를 먹고 지나간 자리는 빈칸 으로 바꾼다
    space[shark_x][shark_y] = 0
    answer += move_time
