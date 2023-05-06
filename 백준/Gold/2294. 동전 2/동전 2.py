# 백준 2294 동전 2
import sys
read = sys.stdin.readline

# 동전의 종류 가짓수, 가치의 합
n,k = map(int,read().split())
coins = []
for _ in range(n):
    coins.append(int(read()))

# dp[i] : i원의 가치를 만드는데 사용한 동전의 최소 개수
dp = [100001] * (k+1)

# 가치 0을 만드는 동전 개수는 0개
dp[0] = 0

for coin in coins:
    for i in range(coin, k+1):
        # coin원 짜리 동전으로 i원 만들기 : i-coin 원을 만든 후 coin을 추가하는 것과 같음
        dp[i] = min(dp[i], dp[i-coin] + 1)

print(dp[k] if dp[k] < 100001 else -1)