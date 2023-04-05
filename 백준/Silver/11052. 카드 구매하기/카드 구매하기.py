# 백준 11052 카드 구매하기
import sys
read = sys.stdin.readline

# 카드팩 수 = 구매 하고자하는 카드 수
n = int(read().rstrip())
cardpack = [0] + list(map(int,read().rstrip().split()))
dp = [0 for _ in range(n+1)]
dp[1] = cardpack[1]

for i in range(2,n+1):
    for k in range(1, i+1):
        dp[i] = max(dp[i], cardpack[k] + dp[i-k])

print(dp[n])