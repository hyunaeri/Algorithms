def solution(triangle):
    answer = 0
    
    dp = [ [0]*len(row) for row in triangle ]
    
    # 초기화
    dp[0][0] = triangle[0][0]
    
    # 점화식 적용
    for i in range(len(triangle) - 1): 
        for j in range(len(triangle[i])):
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j] + triangle[i + 1][j])
            dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + triangle[i + 1][j + 1]) 
                
    # for d in dp:
    #     print(d)

    answer = max(dp[-1])
    
    return answer