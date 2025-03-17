def solution(N, number):
    dp = [ [] for _ in range(9) ]
    
    for i in range(1, 9):
        # N과 사칙연산의 결과로 가능한 값들 (중복 제거)
        valueSet = set()
        
        # N이 cnt개 연속된 수
        valueSet.add(int(str(N) * i))
        
        for j in range(1, i):
            for op1 in dp[i-j]:
                for op2 in dp[j]:
                    # 사칙연산 결과
                    for result in [op1 + op2, op1 - op2, op1 * op2, op1 / op2]:
                        if result > 0:
                            valueSet.add(result)
                            
        
        # 목표가 집합에 포함되어 있으면 해당 개수 리턴
        if number in valueSet:  
            return i
        
        # 아니면 DP 테이블에 추가
        else:
            for value in valueSet:
                dp[i].append(value)
    
    return -1