# 백준 11049 행렬 곱셈 순서
import sys
read = sys.stdin.readline

# 매개변수로 행렬이 담긴 리스트를 받음.
def Chained_Matrix_Multiplication(d):
    # dp[i][j] : i번 행렬에서 j번 행렬 까지의 최소 곱셈 횟수
    dp = [ [-1]*N for _ in range(N) ]

    # 자기 자신을 곱하는 횟수는 0
    for i in range(N):
        dp[i][i] = 0

    # 몇 번째 대각선인지?
    for diagonal in range(1, N):
        # 대각선에서 몇 번째 열?
        for start in range(N - diagonal):
            end = start + diagonal

            # 어떤 행렬의 최소 곱셈 횟수는 분할한 두 행렬의 최소 곱셈 횟수 + 곱셈이 끝난 두 행렬 끼리의 곱셈 횟수
            dp[start][end] = float('INF')
            for cut in range(start, end):
                dp[start][end] = min(dp[start][end], dp[start][cut] + dp[cut+1][end] + (d[start][0] * d[cut][1] * d[end][1]))

    return dp[0][-1]



# 행렬의 개수
N = int(read())
matrix = [list(map(int,read().split())) for _ in range(N)]

print(Chained_Matrix_Multiplication(matrix))