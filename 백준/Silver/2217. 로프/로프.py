# 백준 2217
# 실버 4
# https://www.acmicpc.net/problem/2217

import sys
read = sys.stdin.readline

if __name__ == '__main__':
  
  # 로프 개수
  N = int(read())
  
  # 각 로프 정보
  rope_info = [ int(read()) for _ in range(N) ]
  rope_info.sort(key = lambda x: -x)
  
  # for rope in rope_info:
  #   print(rope)
  
  # 최대 중량 계산
  answer = 0
  
  # i번째 로프까지, 총 i+1개 사용
  for i in range(N):
      w = rope_info[i] * (i + 1)   # 현재까지 사용 가능한 로프의 최소값 × 개수
      if w > answer:
          answer = w
  
  print(answer)