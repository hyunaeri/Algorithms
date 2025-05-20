def solution(s):
    if len(s) == 1:
        return 1
    
    answer = float('inf')
    
    # 문자열을 자를 단위 (1개 이상)
    for i in range(1, len(s) // 2 + 1):
        target, cnt = s[0:i], 1
        result = ''
        
        for j in range(i, len(s), i):
            check = s[j:j+i]
            
            # 문자가 반복된 경우
            if target == check:
                cnt += 1
            
            # 문자가 반복되지 않은 경우, 압축 후 변수 초기화
            else:
                result += (str(cnt) if cnt > 1 else '') + target
                target = check
                cnt = 1
        
        # 마지막에 남는 문자열 처리
        result += (str(cnt) if cnt > 1 else '') + target
        
        answer = min(answer, len(result))
    
    return answer