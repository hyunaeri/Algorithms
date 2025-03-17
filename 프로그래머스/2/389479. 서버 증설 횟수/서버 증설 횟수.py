def solution(players, m, k):
    # 현재 증설된 서버의 수 (24시간)
    currentExpandedServer = [0] * 24
    expandedServerCount = 0
    
    for i in range(24):
        # 현 시각대에 필요한 서버 수
        neededServer = players[i] // m
        
        # 추가 증설해야 할 서버 수
        additionalServer = max(0, neededServer - currentExpandedServer[i])
        
        # 서버 증설
        if additionalServer > 0:
            expandedServerCount += additionalServer
            for j in range(k):
                if i + j < 24:
                    currentExpandedServer[i+j] += additionalServer
                
    return expandedServerCount