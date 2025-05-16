# 2025.05.16 (금)
# 백준 2075 N 번째 큰 수
# 실버 3

import heapq
import sys
read = sys.stdin.readline

# N * N 크기
N = int(read())
PQ = []
heapq.heapify(PQ)

for _ in range(N):
    numbers = list(map(int, read().split()))
    
    for num in numbers:
        if len(PQ) < N:
            heapq.heappush(PQ, num)
        else:
            if num > PQ[0]:
                heapq.heappop(PQ)
                heapq.heappush(PQ, num)

print(PQ[0])