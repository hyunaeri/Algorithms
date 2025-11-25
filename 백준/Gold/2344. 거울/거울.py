# 백준 2344
# 골드 4
# https://www.acmicpc.net/problem/2344

import sys
read = sys.stdin.readline

def solution(x, y, dir):
    global dirs, box
    current_x, current_y = x, y
    
    while True:
        dx, dy = dirs[dir]
        current_x, current_y = current_x + dx, current_y + dy
        
        # 빛이 바깥으로 빠져나간 것
        if current_x == 0 or current_x == N + 1 or current_y == 0 or current_y == M + 1:
            print(box[current_x][current_y], end = ' ')
            return
        
        # 현재 위치가 거울이고, 빛의 방향이 상/하 : 시계 방향 90도 회전
        if box[current_x][current_y] == 1 and dir in [0, 2]:
            dir = (dir + 1) % 4
            continue
        
        # 현재 위치가 거울이고, 빛의 방향이 좌/우 : 반 시계 방향 90도 회전
        if box[current_x][current_y] == 1 and dir in [1, 3]:
            dir = (dir - 1) % 4
            continue

if __name__ == "__main__":
    
    # 방향 정보 (상우하좌)
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    
    # 세로, 가로
    N, M = map(int, read().split())
    
    # 거울이 있으면 1, 없으면 0
    box = [ [0] * (M + 2) for _ in range(N + 2) ]
    input_value = [ list(map(int, read().split())) for _ in range(N) ]
    
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            box[i][j] = input_value[i - 1][j - 1]
    
    # 각 구멍 넘버링
    num = 1
    
    for i in range(1, N + 1):
        box[i][0] = num
        num += 1
    
    for j in range(1, M + 1):
        box[N + 1][j] = num
        num += 1
    
    for i in range(N, 0, -1):
        box[i][M + 1] = num
        num += 1
    
    for j in range(M, 0, -1):
        box[0][j] = num
        num += 1
    
    # 빛을 오른쪽으로 쏘기
    for i in range(1, N + 1):
        solution(i, 0, 1)
    
    # 빛을 위쪽으로 쏘기
    for j in range(1, M + 1):
        solution(N + 1, j, 0)
    
    # 빛을 왼쪽으로 쏘기
    for i in range(N, 0, -1):
        solution(i, M + 1, 3)
    
    # 빛을 아래쪽으로 쏘기
    for j in range(M, 0, -1):
        solution(0, j, 2)
        