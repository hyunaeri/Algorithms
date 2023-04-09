# 백준 1916 최소비용구하기
import sys
import heapq
read = sys.stdin.readline
INF = int(1e9)

# 도시의 개수, 버스의 개수
n = int(read())
m = int(read())
data = [ [] for _ in range(n+1) ]

# 버스 정보 받아오기
for _ in range(m):
    u,v,w = map(int, read().rstrip().split())
    data[u].append((v,w))

# 출발점, 도착점
start, end = map(int,read().rstrip().split())

# 최단 거리 테이블
distance = [INF] * (n+1)

heap = []
def dijkstra(start):
    # 자기자신으로 가는 비용은 0
    distance[start] = 0
    heapq.heappush(heap, (0,start))

    while heap:
        dist, next = heapq.heappop(heap)
        if distance[next] < dist:
            continue

        for next_node, weight in data[next]:
            cost = dist + weight
            if cost < distance[next_node]:
                distance[next_node] = cost
                heapq.heappush(heap, (cost,next_node))

dijkstra(start)
print(distance[end])
