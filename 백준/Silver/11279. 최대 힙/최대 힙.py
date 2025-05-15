# 2025.05.15 (목)
# 백준 11279 최대 힙
# 실버 2

import heapq
import sys
read = sys.stdin.readline

# 연산의 개수
N = int(read())
heap = []
heapq.heapify(heap)

for _ in range(N):
  command = int(read())
  
  # 0 : 출력
  if command == 0:
    if len(heap) == 0:
      print(0)
    else:
      result = -heapq.heappop(heap)
      print(result)
  
  # 나머지 자연수 : 힙에 추가
  else:
    heapq.heappush(heap, -command)