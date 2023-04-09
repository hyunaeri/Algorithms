# 백준 1504 특정한 최단 경로
import sys
import heapq
read= sys.stdin.readline
INF = int(1e9)

# 정점의 개수, 간선의 개수
n,m = map(int,read().rstrip().split())
graph = [ [] for _ in range(n+1) ]

# 간선 정보 업데이트
# 무방향 그래프이므로, 양 방향 모두 추가
for _ in range(m):
    a,b,c = map(int,read().rstrip().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

def dijkstra(start):
    distance = [INF] * (n+1)
    heap = []

    # 자기 자신으로 가는 최소 비용은 0
    distance[start] = 0
    heapq.heappush(heap, (0,start))

    while heap:
        # 탐색할 노드와 거리
        dist, next = heapq.heappop(heap)

        if distance[next] < dist:
            continue

        for next_node, weight in graph[next]:
            cost = dist + weight
            if distance[next_node] > cost:
                distance[next_node] = cost
                heapq.heappush(heap, (cost,next_node))

    return distance

# 반드시 경유해야하는 두 정점
v1, v2 = map(int, read().rstrip().split())

# 출발점이 1, v1, v2 일때의 최단거리 배열
ori_distance = dijkstra(1)
v1_distance = dijkstra(v1)
v2_distance = dijkstra(v2)

v1_path = ori_distance[v1] + v1_distance[v2] + v2_distance[n]
v2_path = ori_distance[v2] + v2_distance[v1] + v1_distance[n]

answer = min(v1_path, v2_path)

if answer < INF:
    print(answer)
else:
    print("-1")


