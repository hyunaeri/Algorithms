# 백준 7562 나이트의 이동
# BFS
from collections import deque
import sys
read = sys.stdin.readline

def BFS(a,b):
    queue = deque()
    queue.append((a,b))
    chess[a][b] = 1

    while queue:
        x, y = queue.popleft()
        # 이동하고자 하는 칸에 도달
        if x == result_x and y == result_y:
            print(chess[x][y] - 1)
            break

        # 나이트가 움직일 수 있는 8방향
        for dx,dy in [ (-1,-2),(-2,-1),(-2,1),(-1,2),(1,2),(2,1),(2,-1),(1,-2) ]:
            nx = x + dx
            ny = y + dy

            # 체스판 범위 내에서 이동했고, 미 방문 지점이라면
            if 0 <= nx < board and 0 <= ny < board and chess[nx][ny] == 0:
                queue.append((nx,ny))
                chess[nx][ny] = chess[x][y] + 1


# 테스트 케이스 수
T = int(read())
for _ in range(T):
    # 체스판 한 변의 길이
    board = int(read())
    chess = [ [0]*board for _ in range(board) ]

    # 나이트가 현재 있는 칸
    knight_x, knight_y = map(int, read().rstrip().split())
    # 나이트가 이동하려고 하는 칸
    result_x, result_y = map(int, read().rstrip().split())

    # BFS
    BFS(knight_x, knight_y)



