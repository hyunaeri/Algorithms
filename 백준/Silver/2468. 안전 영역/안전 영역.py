# 백준 2468 안전 영역
# DFS

import sys
sys.setrecursionlimit(10**5)
read = sys.stdin.readline

N = int(read().rstrip())
region = [ list(map(int,read().rstrip().split())) for _ in range(N) ]
max_height = 0
answer = 0
for r in region:
    max_height = max(max_height, max(r))


# print(region)

def DFS(x,y,limit):
    visited[x][y] = True

    for dx,dy in [ (-1,0), (1,0), (0,-1), (0,1) ]:
        nx,ny = x + dx, y + dy

        # 그래프의 범위를 벗어남
        if nx < 0 or ny < 0 or nx >= N or ny >= N:
            continue

        if region[nx][ny] > limit and visited[nx][ny] == False :
            visited[nx][ny] = True
            DFS(nx,ny,limit)

for k in range(max_height):
    visited = [ [False]*N for _ in range(N) ]
    cnt = 0

    for i in range(N):
        for j in range(N):
            if region[i][j] > k and visited[i][j] == False :
                cnt += 1
                DFS(i,j,k)

    answer = max(cnt, answer)

print(answer)