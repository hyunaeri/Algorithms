# 백준 14502 연구소
# BFS
from collections import deque
import sys
from copy import deepcopy
read = sys.stdin.readline

# 지도의 세로, 가로 크기
n,m = map(int, read().rstrip().split())

# 빈 칸:0 
# 벽:1 
# 바이러스:2
lab = [ list(map(int,read().rstrip().split())) for _ in range(n) ]
answer = 0

def bfs():
    queue = deque()
    test_lab = deepcopy(lab)

    for i in range(n):
        for j in range(m):
            # 바이러스가 있는 곳(2)은 미리 큐에 저장
            if test_lab[i][j] == 2:
                queue.append((i,j))

    while queue:
        x,y = queue.popleft()
        # 상하좌우
        for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx,ny = x+dx, y+dy

            # 연구소의 범위를 벗어났거나 벽을 만난 경우
            if nx < 0 or ny < 0 or nx >= n or ny >= m or test_lab[nx][ny] == 1 :
                continue

            # 그렇지 않은 경우 : 빈 칸
            if test_lab[nx][ny] == 0:
                queue.append((nx,ny))
                test_lab[nx][ny] = 2

    global answer
    count = 0
    for i in range(n):
        for j in range(m):
            # 벽이랑 바이러스 칸이 아닌 경우
            if test_lab[i][j] == 0:
                count += 1

    answer = max(answer, count)

def makeWall(count):
    if count == 3:
        bfs()
        return
    
    for i in range(n):
        for j in range(m):
            if lab[i][j] == 0:
                lab[i][j] = 1
                makeWall(count + 1)
                lab[i][j] = 0

makeWall(0)
print(answer)