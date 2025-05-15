# 2025.05.15 (목)
# 백준 11286 절댓값 힙
# 실버 1

import heapq
import sys
read = sys.stdin.readline

# 연산의 개수
N = int(read())

heap = []
heapq.heapify(heap)

for _ in range(N):
  command = int(read())
  
  if command != 0:
    heapq.heappush(heap, (abs(command), command))
    
  else:
    print(heapq.heappop(heap)[-1] if heap else 0)