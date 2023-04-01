# 백준 16928 뱀과 사다리 게임
# BFS
from collections import deque
import sys
read = sys.stdin.readline

# 일부러 1차원 : 주사위는 1~6칸 이동이니까
game = [0 for _ in range(101)]
visited = [False for _ in range(101)]
ladder = dict()
snake = dict()

# 사다리 수, 뱀의 수
n,m = map(int, read().rstrip().split())

# 사다리 업데이트
for _ in range(n):
    x, y = map(int,read().rstrip().split())
    ladder[x] = y

# 뱀 업데이트
for _ in range(m):
    x, y = map(int,read().rstrip().split())
    snake[x] = y

def BFS(start):
    queue = deque()
    queue.append(start)

    while queue:
        x = queue.popleft()

        if x == 100:
            print(game[x])
            break
        
        # 주사위 굴리면 최소 1칸 ~ 최대 6칸 이동
        for dice in [1,2,3,4,5,6]:
            next = x + dice
            # 다음 칸이 맵을 벗어나지 않고, 미 방문 칸이라면
            if 0 <= next <= 100 and visited[next] == False:
                # 하지만 그 위치에 사다리가 있다면?
                if next in ladder.keys():
                    next = ladder[next]

                # 하지만 그 위치에 뱀이 있다면?
                if next in snake.keys():
                    next = snake[next]

                # 이동할 위치에 아무것도 없다면?
                if visited[next] == False:
                    visited[next] = True
                    # 주사위 굴린 횟수 추가
                    game[next] = game[x] + 1
                    queue.append(next)

BFS(1)


