# 백준 16234 인구 이동
# BFS
import sys
from collections import deque
read = sys.stdin.readline

N,L,R = map(int,read().rstrip().split())
population = [ list(map(int,read().rstrip().split())) for _ in range(N) ]
# print(population)


# 국경선 여는 함수
def open(x,y):
    queue = deque()
    queue.append((x,y))
    temp = []
    temp.append((x,y))
    visited[x][y] = 1

    while queue:
        x, y = queue.popleft()

        for dx, dy in [ (-1,0), (1,0), (0,-1), (0,1) ]:
            nx, ny = x + dx, y + dy

            if nx < 0 or ny < 0 or nx >= N or ny >= N :
                continue

            if visited[nx][ny] == 0:
                # 국경선을 공유하는 두 나라의 인구 차이가 L명 이상, R명 이하라면, 두 나라가 공유하는 국경선을 오늘 하루 동안 연다.
                # abs함수 : 절댓값 함수
                if L <= abs(population[nx][ny] - population[x][y]) <= R:
                    visited[nx][ny] = 1
                    queue.append((nx,ny))
                    temp.append((nx,ny))

    return temp

# answer : 인구이동이 며칠간 이루어지는가?
answer = 0
while True:
    visited = [ [0]*N for _ in range(N) ]
    check = 0

    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                country = open(i,j)
                # 연합 구축
                if len(country) > 1 : 
                    check = 1
                    # 연합을 이루고 있는 각 칸의 인구수는 (연합의 인구수) / (연합을 이루고 있는 칸의 개수)가 된다. 편의상 소수점은 버린다.
                    p = sum([population[x][y] for x,y in country]) // len(country)

                    for x, y in country:
                        population[x][y] = p

    # 연합이 없으므로 모든 국경선을 닫는다.
    if check == 0:  
        break
    
    answer += 1

print(answer)