# 백준 1753 최단 경로
# 다익스트라 알고리즘 : 시작점으로 부터 나머지 정점까지의 최단 경로 구하기
import sys
import heapq
read = sys.stdin.readline
INF = int(1e9)

# 정점의 개수, 간선의 개수
V,E = map(int, read().rstrip().split())
# 시작 정점의 번호
start = int(read())

# u에서 v로 가는 가중치 w
data = [ [] for _ in range(V+1) ]
for _ in range(E):
    u,v,w = map(int,read().rstrip().split())
    data[u].append((v,w))

# 최단거리
distance = [INF] * (V+1)

# 힙은 리스트에서 굴리는 것
heap = []
def dijkstra(start):
    # 자기 자신으로 가는 최소 비용은 0
    distance[start] = 0
    heapq.heappush( heap,(0,start) )

    while heap:
        dist, next = heapq.heappop(heap)
        for next_node, weight in data[next]:
            cost = dist + weight
            if cost < distance[next_node]:
                distance[next_node] = cost
                heapq.heappush( heap,(cost,next_node) )

dijkstra(start)

for i in distance[1:]:
    if i != INF:
        print(i)
    else:
        print("INF")
