# 백준 4179 불!

from collections import deque
import sys

read = sys.stdin.readline
runner = deque()
fire = deque()
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def burn():
    len_fire = len(fire)
    for _ in range(len_fire):
        x, y = fire.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            # 미로의 범위 내에서만
            if 0 <= nx < M and 0 <= ny < N:
                if maze[nx][ny] == '.':
                    maze[nx][ny] = 'F'
                    fire.append([nx,ny])

def escape():
    while runner:
        len_runner = len(runner)

        # 현재 큐에 들어있는 길이 만큼만 움직임
        for _ in range(len_runner):
            x, y = runner.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]

                # 미로의 범위 내에서만
                if 0 <= nx < M and 0 <= ny < N:
                    # 빈칸이면서 방문하지 않은 곳 일때만
                    if maze[nx][ny] == '.' and visited[nx][ny] == 0:
                        visited[nx][ny] = visited[x][y] + 1
                        runner.append([nx,ny])

                # 미로의 가장자리 도달 = 탈출! 
                elif nx < 0 or ny <0 or nx == M or ny == N:
                    print(visited[x][y] + 1)
                    return
                
        burn()
    print('IMPOSSIBLE')
    return

# 미로 행의 개수, 열의 개수 = 세로, 가로
M,N = map(int,read().split())

# '#': 벽
# '.': 지나갈 수 있는 공간
# 'J': 지훈이의 미로에서의 초기위치 (지나갈 수 있는 공간)
# 'F': 불이 난 공간
maze = [ list(map(str,read().rstrip())) for _ in range(M) ]
visited = [ [0]*N for _ in range(M) ]

for i in range(M):
    for j in range(N):
        # 지훈이의 초기 위치
        if maze[i][j] == 'J':
            # 초기 위치를 따로 저장해 두었으니, 기존의 초기 위치는 빈칸으로 봐도 무방함
            maze[i][j] = '.'
            runner.append([i,j])
        # 불의 초기 지점
        elif maze[i][j] == 'F':
            fire.append([i,j])

burn()
escape()