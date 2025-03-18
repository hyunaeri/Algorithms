# 입력값 n을 받음 (n을 제곱수들의 합으로 표현하는 최소 개수를 구하는 문제)
import sys
read = sys.stdin.readline

n = int(read())

# dp[i]: i개의 제곱수로 만들 수 있는 숫자 리스트
dp = [set() for _ in range(5)]
dp[0].add(0)

# n 이하의 모든 제곱수를 구함
squares = []
i = 1
while i * i <= n:
    squares.append(i * i)
    i += 1

# DP 테이블 채우기
for count in range(1, 5):
    for num in dp[count - 1]:
        for square in squares:
            new_num = num + square
            if new_num > n:  # 초과하면 스킵
                break
            dp[count].add(new_num)
            
    if n in dp[count]:
        print(count)
        break