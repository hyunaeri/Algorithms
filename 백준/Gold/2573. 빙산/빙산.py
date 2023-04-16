# 백준 2573 빙산
import sys
from collections import deque
read = sys.stdin.readline

# 행의 개수(세로), 열의 개수(가로)
n,m = map(int,read().split())
iceberg = [ list(map(int,read().split())) for _ in range(n) ]

# 빙산의 분리 여부
check = False

# 걸린 시간
year = 0

def ice_melting(x,y):
    q = deque()
    q.append((x,y))
    visited[x][y] = True

    while q:
        x,y = q.popleft()

        for dx, dy in [ (-1,0), (1,0), (0,-1), (0,1) ]:
            nx, ny = x + dx, y + dy

            # 그래프의 범위를 벗어나면 OUT
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            
            # 그래프의 범위 안이면
            else:
                # 이동한 위치에 인접한 빙산이 존재하고, 미 방문 상태이면
                if iceberg[nx][ny] > 0 and visited[nx][ny] == False:
                    q.append((nx,ny))
                    visited[nx][ny] = True

                # 이동한 위치가 바다이면
                elif iceberg[nx][ny] == 0:
                    sea_cnt[x][y] += 1

# 빙산이 분리 될때까지
while True:
    visited = [[False]*m for _ in range(n)]
    cnt = 0
    # 인접한 네 곳 중 바다의 개수
    sea_cnt = [[0]*m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if iceberg[i][j] != 0 and visited[i][j] == False:
                ice_melting(i,j)
                cnt += 1

    for i in range(n):
        for j in range(m):
            iceberg[i][j] -= sea_cnt[i][j]

            # 음수가 되버리면 0으로 고쳐주자
            if iceberg[i][j] < 0:
                iceberg[i][j] = 0

    # 빙산이 다 없어져서 분리 되지 않음
    if cnt == 0:
        break
    
    # 빙산이 2개 이상으로 분리가 됨
    elif cnt >= 2:
        check = True
        break

    year += 1

if check:
    print(year)
else:
    print("0")