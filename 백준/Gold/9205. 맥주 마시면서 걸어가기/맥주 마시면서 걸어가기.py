# 백준 9205 맥주 마시면서 걸어가기
import sys
from collections import deque
read = sys.stdin.readline

T = int(read())

def go_festival(x,y):
    queue = deque()
    queue.append((x,y))

    while queue:
        x,y = queue.popleft()
        # 현재 위치와 페스티벌 장 사이의 거리가 맥주 20병으로 해결이 된다면
        if abs(festival_x - x) + abs(festival_y - y) <= 1000:
            print("happy")
            return
        
        # 편의점들 확인
        for i in range(n):
            # 미 방문 상태라면
            if not visited[i]:
                store_x, store_y = store[i]
                # 편의점까지 맥주 20병으로 이동이 가능하다면
                if (abs(store_x - x) + abs(store_y - y)) <= 1000:
                    queue.append((store_x, store_y))
                    visited[i] = True

    print("sad")
    return


for _ in range(T):
    # 편의점의 개수
    n = int(read())
    store = []

    # 집(1), 편의점(2), 락 페스티벌(3) 좌표 값
    house_x , house_y = map(int, read().split())
    for _ in range(n):
        store.append(list(map(int, read().split())))
    festival_x, festival_y = map(int, read().split())

    # 편의점 방문 여부
    visited = [ False for _ in range(n+1) ]

    go_festival(house_x, house_y)