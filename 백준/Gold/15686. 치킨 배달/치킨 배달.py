# 백준 15686 치킨 배달
from itertools import combinations
import sys
read = sys.stdin.readline

# N*N 크기의 지도, 폐업 시키지 않을 치킨집의 개수
N,M = map(int,read().split())

chicken_map = [ list(map(int,read().split())) for _ in range(N) ]
house = []
chicken = []
result = 999999999

for i in range(N):
    for j in range(N):
        # 집
        if chicken_map[i][j] == 1:
            house.append([i,j])
        # 치킨 집
        elif chicken_map[i][j] == 2:
            chicken.append([i,j])

for chick in combinations(chicken, M):
    # 도시의 치킨 거리
    temp = 0
    for h in house:
        # 각 집마다의 치킨 거리
        chick_len = 9999999
        for i in range(M):
            chick_len = min(chick_len, abs(h[0] - chick[i][0]) + abs(h[1] - chick[i][1]))
        temp += chick_len
    result = min(result, temp)


print(result)