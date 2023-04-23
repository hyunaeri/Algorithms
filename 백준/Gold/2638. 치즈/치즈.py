# 백준 2638 치즈
from collections import deque
import sys
read = sys.stdin.readline
dx = [-1,1,0,0]
dy = [0,0,-1,1]

# 세로, 가로
M, N = map(int,read().split())

# 치즈 : 1 
# 빈공간 : 0
cheese = [ list(map(int,read().split())) for _ in range(M) ]

# 모든 치즈가 녹았는지?
check = False

# 정답
result = 0

def melt(x,y):
    queue = deque()
    queue.append([x,y])
    
    visited[x][y] = 1
    temp = []

    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx,ny = x+dx[i], y+dy[i]

            if 0 <= nx < M and 0 <= ny < N:
                # 이동한 칸이 빈 칸(외부공기) 일 경우 큐에 추가
                if cheese[nx][ny] == 0 and visited[nx][ny] == 0:
                    queue.append([nx,ny])
                    visited[nx][ny] = 1
                # 이동한 칸이 치즈 일 경우
                elif cheese[nx][ny] == 1:
                    # 한 변이 외부공기와 만나고 있으므로 1 더하기
                    air[nx][ny] += 1
    
    # 이번 사이클에 녹을 치즈 업데이트
    for i in range(M):
        for j in range(N):
            if air[i][j] >= 2:
                temp.append([i,j])
    
    return temp

# 치즈가 완전히 녹을 때 까지
while True:
    visited = [ [0]*N for _ in range(M) ]
    air = [ [0]*N for _ in range(M) ]

    melting_list = melt(0,0)

    # 녹일 치즈가 없다면 이미 다 녹은 것
    if len(melting_list) == 0:
        check = True
        break

    # 치즈 녹이기
    for x,y in melting_list:
        cheese[x][y] = 0

    result += 1

if check:
    print(result)