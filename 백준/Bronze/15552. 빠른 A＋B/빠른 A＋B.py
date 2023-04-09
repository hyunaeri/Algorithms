# 백준 15552 빠른 입출력
# https://velog.io/@yeseolee/Python-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9E%85%EB%A0%A5-%EC%A0%95%EB%A6%ACsys.stdin.readline 참고
# sys.stdin.readline 사용

import sys

T = int(sys.stdin.readline())

for i in range(T):
  a, b = map(int, sys.stdin.readline().split())
  print(a+b)