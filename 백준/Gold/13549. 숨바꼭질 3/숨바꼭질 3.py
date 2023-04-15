# 백준 13549 숨바꼭질3
# 0-1 BFS 테크닉
# 가중치가 0,1 말고도 여러개라면, 다익스트라를 쓰자
# 가중치에 음수도 포함되어 있다면, 벨만-포드를 쓰자

import sys
from collections import deque
read = sys.stdin.readline

# 수빈이가 있는 위치, 동생이 있는 위치
N,K = map(int, read().rstrip().split())

def BFS(x):
    hide_and_seek = [0] * 100001

    queue = deque()
    queue.append(x)

    while queue:
        x = queue.popleft()
        if x == K:
            print(hide_and_seek[x])
            break
        for nx in [ x-1, x+1, 2*x ]:
            if 0 <= nx < 100001 and hide_and_seek[nx] == 0 :
                
                # 가중치가 0인 이동이기 때문에 deque의 앞에 넣어야 된다. 최단거리니까 당연한 것
                if nx == 2*x and x != 0:
                    queue.appendleft(nx)
                    hide_and_seek[nx] = hide_and_seek[x]
                else:
                    queue.append(nx)
                    hide_and_seek[nx] = hide_and_seek[x] + 1

BFS(N)
