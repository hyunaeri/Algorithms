import sys
from collections import deque
read = sys.stdin.readline
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    cnt = 1
    q.append([x,y])
    # 방문 여부는 -1
    trash[x][y] = -1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                # 인접한 곳이 쓰레기 칸 일 경우, 그리고 미 방문 상태
                if trash[nx][ny] == 1:
                    trash[nx][ny] = 2
                    cnt += 1
                    q.append([nx,ny])

    return cnt

# 세로 길이, 가로 길이, 음쓰 개수
N,M,K = map(int,read().split())
trash = [ [0]*M for _ in range(N) ]
q = deque()

# 쓰레기 좌표
for _ in range(K):
    r,c = map(int,read().split())
    trash[r-1][c-1] = 1

# 정답 도출
answer = 0
for i in range(N):
    for j in range(M):
        if trash[i][j] != 0:
            answer = max(answer, bfs(i,j))

print(answer)