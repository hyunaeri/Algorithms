# 2025.05.20 (화)
# 백준 1654 랜선 자르기
# 실버 2

# 이분탐색을 이용하는 Parametric Search
# 주어진 범위 내에서 원하는 값 또는 조건에 가장 일치하는 값을 찾아내는 알고리즘

import sys
read = sys.stdin.readline

# 이미 가지고 있는 랜선 수, 필요한 랜선의 수
K, N = map(int, read().split())
lan = list()

for _ in range(K):
  line = int(read())
  lan.append(line)

def parametric_search(lan, N):
  low, high = 1, max(lan)
  mid = 0
  
  while low <= high:
    mid = (low + high) // 2
    cnt = 0
    
    for l in lan:
      cnt += (l // mid)
    
    # 랜선 N개 이상을 만들 수 있다면, mid 보다 더 크게 잘라도 되는지?
    if cnt >= N:
      low = mid + 1
    
    # N개 미만으로 만들 수 있으면
    else:
      high = mid - 1

  return high

print(parametric_search(lan, N))