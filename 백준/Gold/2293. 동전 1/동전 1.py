# 백준 2293 동전 1
import sys
read = sys.stdin.readline

# 동전의 종류 가짓수, 가치의 합
n,k = map(int,read().split())
coins = []
for _ in range(n):
    coins.append(int(read()))
dp = [0] * (k+1)

# 가치 0을 만드는 가짓수는 1가지(아무것도 선택 안하는 것)
dp[0] = 1

for coin in coins:
    for i in range(coin, k+1):
        # coin원 짜리 동전으로 i원 만들기 : i-coin 원을 만든 후 coin을 추가하는 것과 같음
        dp[i] += dp[i-coin]

print(dp[k])
