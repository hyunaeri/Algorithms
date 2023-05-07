import sys
read = sys.stdin.readline

N = int(read())
consulting = [ list(map(int, read().rstrip().split())) for _ in range(N) ]

# dp[i] : i번째 상담까지 했을 때 얻을 수 있는 최대 수익
dp = [0] * (N+1)

for i in range(N-1, -1, -1):
    # i일에 상담을 하는 것이 퇴사일을 넘기면 상담을 하지 않는다
    if i + consulting[i][0] > N:
        dp[i] = dp[i+1]

    else:
        dp[i] = max(dp[i+1], consulting[i][1] + dp[i + consulting[i][0]])

print(dp[0])