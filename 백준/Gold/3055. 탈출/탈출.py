# 백준 3055 탈출
import sys
from collections import deque
read = sys.stdin.readline
dx = [-1,1,0,0]
dy = [0,0,-1,1]
queue = deque()
water = deque()

def flow():
    len_water = len(water)
    for _ in range(len_water):
        x,y = water.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < R and 0 <= ny < C:
                # 이동한 위치가 빈 공간인 경우
                if forest[nx][ny] == '.':
                    forest[nx][ny] = '*'
                    water.append([nx,ny])

def escape():
    while queue:
        len_q = len(queue)
        for _ in range(len_q):
            x, y = queue.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                
                if 0 <= nx < R and 0 <= ny < C:
                    if forest[nx][ny] == '.' and visited[nx][ny] == 0:
                        queue.append([nx,ny])
                        visited[nx][ny] = visited[x][y] + 1

                    elif forest[nx][ny] == 'D' and visited[nx][ny] == 0:
                        print(visited[x][y] + 1)
                        return
        flow()
    print("KAKTUS")
    return

# R행 C열
R,C = map(int,read().split())

# '.' : 비어있는 곳
# '*' : 물이 차있는 곳
# 'X' : 돌
# 'D' : 비버의 굴
# 'S' : 고슴도치 위치
forest = [ list(map(str,read().rstrip())) for _ in range(R) ]
visited = [ [0]*C for _ in range(R) ]

for i in range(R):
    for j in range(C):
        if forest[i][j] == 'S':
            queue.append([i,j])
            forest[i][j] = '.'

        elif forest[i][j] == '*':
            water.append([i,j])
            
flow()
escape()