# 백준 14940 쉬운 최단거리
# https://www.acmicpc.net/problem/14940

from collections import deque
import sys
read = sys.stdin.readline

# 상하좌우 이동
dx = [-1,1,0,0]
dy = [0,0,-1,1]

# 지도의 크기 n,m (세로, 가로)
n,m = map(int, read().split())

# 0 : 갈 수 없는 땅
# 1 : 갈 수 있는 땅
# 2 : 목표지점
input_map = []
answer = [ [0]*m for _ in range(n) ]

def bfs(x, y):
    q = deque()
    q.append([x,y,0])
    visited = [[0]*m for _ in range(n)]
    visited[x][y] = 1
    
    while q:
        x, y, count = q.popleft()
        
        # if input_map[x][y] == 2:
        #     return count
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            
            # 갈 수 없는 땅이 아니고, 미 방문 지역이라면?
            if input_map[nx][ny] != 0 and visited[nx][ny] == 0:
                q.append([nx,ny, count + 1])
                visited[nx][ny] = 1
                answer[nx][ny] = count + 1

            

for _ in range(n):
    input_map.append(list(map(int, read().split())))
    
# 목표 지점 좌표 미리 받아놓기
goal_x, goal_y = 0, 0
check = False

for i in range(n):
    for j in range(m):
        if input_map[i][j] == 2:
            goal_x, goal_y = i, j
            check = True
            break
        
    if check == True:
        break
    
# 탐색 시작
bfs(goal_x, goal_y)

for i in range(n):
    for j in range(m):
        if input_map[i][j] == 1 and answer[i][j] == 0:
            answer[i][j] = -1

for an in answer:
    print(*an)
