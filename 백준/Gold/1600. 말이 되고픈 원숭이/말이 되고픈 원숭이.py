# 백준 1600 말이 되고픈 원숭이
import sys
from collections import deque
read = sys.stdin.readline

# 상하좌우 : 원숭이 
dx = [-1,1,0,0]
dy = [0,0,-1,1]

# 대각선 8방향(체스의 나이트 이동 방향) : 나이트
ddx = [-2,-1,1,2,2,1,-1,-2]
ddy = [-1,-2,-2,-1,1,2,2,1]

def bfs(x,y):
    q = deque()
    q.append([x,y,K])
    visited[x][y][K] = 0

    while q:
        x,y,cnt = q.popleft()

        # 도착점 도달
        if x == M-1 and y == N-1 :
            return visited[x][y][cnt]
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            # 격자판의 범위를 벗어나지 않으면서 원숭이로 움직이기
            if 0 <= nx < M and 0 <= ny < N:
                if board[nx][ny] == 0 and visited[nx][ny][cnt] == -1:
                    q.append([nx,ny,cnt])
                    visited[nx][ny][cnt] = visited[x][y][cnt] + 1

        # 나이트 처럼 움직일 수 있는 카운트가 남은 경우
        if cnt > 0:
            for i in range(8):
                nx, ny = x + ddx[i], y + ddy[i]

                # 격자판의 범위를 벗어나지 않으면서 나이트로 움직이기
                if 0 <= nx < M and 0 <= ny < N:
                    if board[nx][ny] == 0 and visited[nx][ny][cnt-1] == -1:
                        q.append([nx,ny,cnt-1])
                        visited[nx][ny][cnt-1] = visited[x][y][cnt] + 1

    # 다 돌았는데도 도착점을 도달하지 못한 것, -1 리턴
    return -1

# 나이트처럼 움직일 수 있는 횟수
K = int(read())

# 격자판의 가로, 세로
# '0' : 아무것도 없는 평지
# '1' : 장애물
N,M = map(int,read().split())
board = [ list(map(int,read().split())) for _ in range(M) ]
visited = [ [ [-1]*(K+1) for _ in range(N)] for _ in range(M) ]

print(bfs(0,0))