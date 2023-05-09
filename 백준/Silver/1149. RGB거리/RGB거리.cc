#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#define MAX 1000*1000

int input[1001][4];
int dp[1001][4];

int min(int x, int y) {
	return x < y ? x : y;
}

int main() {
	int N;
	scanf("%d", &N);
	
	// 입력
	for (int i = 1; i <= N; i++)
		for (int j = 1; j <= 3; j++)
			scanf("%d", &input[i][j]);
	
	// dp 배열 채우기
	dp[1][1] = input[1][1];
	dp[1][2] = input[1][2];
	dp[1][3] = input[1][3];

	for (int i = 2; i <= N; i++) {
		dp[i][1] = min(dp[i - 1][2], dp[i - 1][3]) + input[i][1];
		dp[i][2] = min(dp[i - 1][1], dp[i - 1][3]) + input[i][2];
		dp[i][3] = min(dp[i - 1][1], dp[i - 1][2]) + input[i][3];
	}

	printf("%d", min(min(dp[N][1], dp[N][2]), dp[N][3]));
	return 0;
}