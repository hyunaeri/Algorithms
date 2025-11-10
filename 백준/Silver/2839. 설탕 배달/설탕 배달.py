# 백준 2839
# 실버 4
# https://www.acmicpc.net/problem/2839

import sys
read = sys.stdin.readline

if __name__ == '__main__':
  
  # N kg 의 설탕
  N = int(read())
  
  bag_5 = N // 5
  bag_3 = 0
  remain = N % 5
  
  while True:
    # 남은 설탕이 3으로 나누어 떨어지면
    if remain % 3 == 0:
      bag_3 = remain // 3
      print(bag_3 + bag_5)
      exit(0)
    
    if bag_5 == 0:
      print(-1)
      exit(0)
      
    remain += 5
    bag_5 -= 1