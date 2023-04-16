# 백준 14503 로봇 청소기
import sys
from collections import deque
read = sys.stdin.readline

# 북/동/남/서
dx = [-1,0,1,0]
dy = [0,1,0,-1]

# 세로, 가로 길이
N,M = map(int, read().split())

# 최초의 로봇청소기 좌표, 바라보고 있는 방향
# 0: 북 
# 1: 동 
# 2: 남 
# 3: 서
r,c,d = map(int, read().split())

# 각 장소의 상태 업데이트
# 0 : 청소되지 않은 빈칸
# 1 : 벽
# 2 : 청소 한 칸
vaccum_map = [ list(map(int, read().split())) for _ in range(N) ]
answer = 0

# 반 시계 방향으로 90도 돌리기
def turn_left(d):
    d = (d+3) % 4
    return d

# 진행 방향의 반대로 돌리기
def back(d):
    d = (d+2) % 4
    return d

def clean(x, y, d):
    global answer
    queue = deque()
    queue.append((x,y,d))
    vaccum_map[x][y] = 2
    answer += 1

    while queue:
        x, y, d = queue.popleft()
        nd = d
        
        for i in range(4):
            nd = turn_left(nd)
            nx, ny = x + dx[nd], y + dy[nd]

            # 맵 범위 내이고, 청소되지 않은 빈 칸인 경우
            if 0 <= nx < N and 0 <= ny < M and vaccum_map[nx][ny] == 0:
                # 청소 처리하고, 탈출
                answer += 1
                vaccum_map[nx][ny] = 2
                queue.append((nx,ny,nd))
                break

            # for문을 돌면서 네 방향을 전부 탐색 했으나 갈 곳이 없는 경우
            if i == 3:
                nd = back(d)
                nx, ny = x + dx[nd], y + dy[nd]
                # 바라보는 방향은 유지하면서 후진 해야됨.
                queue.append((nx,ny,d))

                # 후진 할 곳이 벽이라면
                if vaccum_map[nx][ny] == 1:
                    return answer
                
print(clean(r,c,d))