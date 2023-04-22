# 백준 5427 불
# 불이 날 예정인 지점은 상근이는 이동 못함
# 따라서 불을 먼저 이동시키고, 상근이가 이동하는게 논리적으로 맞음

import sys
from collections import deque
read = sys.stdin.readline
dx = [-1,1,0,0]
dy = [0,0,-1,1]

# 테스트 케이스 수
T = int(read())

def burn():
    len_fire = len(fire)
    for _ in range(len_fire):
        x, y = fire.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 빌딩 범위 내에서만 불이 번짐
            if 0 <= nx < h and 0 <= ny < w :
                # 이동한 위치가 빈 공간인 경우
                if building[nx][ny] == '.':
                    building[nx][ny] = '*'
                    fire.append([nx, ny])


def escape_building():
    while queue:
        len_q = len(queue)
    
        # 현재 큐에 들어있는 길이 만큼만 움직임
        for _ in range(len_q):
            x, y = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                # 빌딩 범위 내인 경우
                if 0 <= nx < h and 0 <= ny < w:
                    # 이동한 위치가 빈 공간이면서 미 방문 지역일 경우
                    if building[nx][ny] == '.' and visited[nx][ny] == 0:
                        queue.append([nx,ny])
                        visited[nx][ny] = visited[x][y] + 1

                # 빌딩 범위를 벗어난 경우 = 탈출
                elif nx < 0 or ny < 0 or nx == h or ny == w:
                    print(visited[x][y] + 1)
                    return
                
        burn()
    print('IMPOSSIBLE')
    return


for _ in range(T):
    # 빌딩 지도의 가로, 세로
    w,h = map(int,read().split())

    # '.': 빈 공간
    # '#': 벽
    # '@': 상근이의 시작 위치
    # '*': 불
    building = [ list(read().rstrip()) for _ in range(h) ]
    visited = [ [0] * w for _ in range(h) ]

    # 상근이의 위치, 불의 위치
    queue, fire = deque(), deque()

    # 상근이의 위치와 불길의 위치 업데이트
    for i in range(h):
        for j in range(w):
            if building[i][j] == '@':
                # 빈 칸으로 간주해도 됨. 초기 위치를 따로 저장해두었기에
                building[i][j] = '.'
                queue.append([i,j])

            elif building[i][j] == '*':
                fire.append([i,j])

    burn()
    escape_building()