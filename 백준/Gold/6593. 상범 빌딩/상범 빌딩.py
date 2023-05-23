# 백준 6593 상범 빌딩
import sys
from collections import deque
read = sys.stdin.readline
dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dz = [0,0,0,0,-1,1]

def bfs(z, x, y):
    q = deque()
    q.append([z,x,y])
    visited[z][x][y] = 0

    while q:
        z, x, y = q.popleft()

        # 탈출!
        if z == end_z and x == end_x and y == end_y:
            return 'Escaped in %d minute(s).' % visited[z][x][y]

        for i in range(6):
            nz, nx, ny = z + dz[i], x + dx[i], y + dy[i]
            
            # 빌딩의 범위를 벗어나지 않는다면
            if 0 <= nz < L and 0 <= nx < R and 0 <= ny < C:
                # 미 방문인 빈칸을 만난다면
                if building[nz][nx][ny] == '.' and visited[nz][nx][ny] == -1:
                    q.append([nz,nx,ny])
                    visited[nz][nx][ny] = visited[z][x][y] + 1

    return 'Trapped!'

while True:
    # 빌딩의 층 수, 한층의 행과 열의 개수
    L,R,C = map(int,read().split())
    building = [ []*R for _ in range(L) ]
    visited = [ [ [-1]*C for _ in range(R) ] for _ in range(L) ]

    if L == 0 and R == 0 and C == 0:
        break

    # 빌딩의 정보
    # '#' : 금으로 막혀 지나갈 수 없는 칸
    # '.' : 비어있는 칸
    # 'S' : 나의 시작 지점
    # 'E' : 출구
    for i in range(L):
        for j in range(R):
            building[i].append(list(map(str,read().rstrip())))
        read()

    # 초기 좌표 얻어 두기
    start_x, start_y, start_z, end_x, end_y, end_z = 0, 0, 0, 0, 0, 0

    for i in range(L):
        for j in range(R):
            for w in range(C):
                if building[i][j][w] == 'S':
                    start_z, start_x, start_y = i,j,w
                    building[i][j][w] = '.'

                elif building[i][j][w] == 'E':
                    end_z, end_x, end_y = i,j,w
                    building[i][j][w] = '.'

    print(bfs(start_z, start_x, start_y))
