# 백준 13913 숨바꼭질 4
import sys
from collections import deque
read = sys.stdin.readline
MAX_LENGTH = 100001

# 수빈이와 동생의 위치
a, b = map(int,read().split())
hide_and_seek = [-1] * MAX_LENGTH
path = [-1] * MAX_LENGTH

def bfs(x):
    queue = deque()
    queue.append(x)
    hide_and_seek[x] = 0

    while queue:
        x = queue.popleft()
        if x == b:
            print(hide_and_seek[x])
            answer = []

            while x != -1:
                answer.append(x)
                x = path[x]

            answer.reverse()
            print(*answer, sep = ' ')

        for next in [x-1, x+1, 2*x]:
            if 0 <= next < MAX_LENGTH and hide_and_seek[next] == -1:
                hide_and_seek[next] = hide_and_seek[x] + 1
                queue.append(next)
                # 최종 경로 출력 시 이전 위치를 알 수 있게 하기 위함
                path[next] = x

bfs(a)