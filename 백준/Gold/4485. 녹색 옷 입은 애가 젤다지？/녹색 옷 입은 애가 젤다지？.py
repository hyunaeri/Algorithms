# 백준 4485 초록색 옷 입은 애가 젤다지?
import sys
import heapq
read = sys.stdin.readline
INF = int(2e9)
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dijkstra():
    global count
    queue = []
    heapq.heappush(queue, [cave[0][0], 0,0])

    distance = [ [INF]*N for _ in range(N) ]
    distance[0][0] = cave[0][0]

    while queue:
        cost, x, y = heapq.heappop(queue)

        if x == N-1 and y == N-1:
            print("Problem {}: {}".format(count, distance[x][y]))
            break

        for i in range(4):
            nx,ny = x + dx[i], y + dy[i]

            if 0 <= nx < N and 0 <= ny < N:
                new_cost = cost + cave[nx][ny]

                if new_cost < distance[nx][ny]:
                    distance[nx][ny] = new_cost
                    heapq.heappush(queue, [new_cost, nx, ny])


count = 1

while True:
    # 동굴의 크기
    N = int(read())

    # 0*0 이면 탈출
    if N == 0:
        break

    # 도둑 루피의 크기
    cave = [ list(map(int,read().rstrip().split())) for _ in range(N) ]
    dijkstra()
    count += 1