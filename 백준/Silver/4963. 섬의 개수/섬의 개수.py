# 백준 4963 섬의 개수
import sys
sys.setrecursionlimit(10**5)
read = sys.stdin.readline

def DFS(x,y):
    visited[x][y] = True

    # 상하좌우 및 대각선
    for dx,dy in [ (-1,0), (1,0), (0,-1), (0,1), (-1,-1), (-1,1), (1, -1), (1,1) ]:
        nx,ny = x+dx, y+dy

        if nx < 0 or ny < 0 or nx >= h or ny >= a:
            continue

        if island[nx][ny] == 1 and visited[nx][ny] == False:
            DFS(nx,ny)

while True:
    a,h = map(int,read().rstrip().split())

    if a == 0 and h == 0:
        break

    # 1은 땅, 0은 바다
    island = [ list(map(int,read().rstrip().split())) for _ in range(h) ]
    visited = [ [False]*a for _ in range(h) ]
    ans = 0

    for i in range(h):
        for j in range(a):
            if island[i][j] == 1 and visited[i][j] == False:
                DFS(i,j)
                ans += 1

    print(ans)
