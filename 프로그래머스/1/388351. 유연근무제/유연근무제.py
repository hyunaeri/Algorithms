def solution(schedules, timelogs, startday):
    answer = 0
    
    for idx, s in enumerate(schedules):
        # 출근 데드라인
        h, m = s // 100, (s % 100) + 10
        if m >= 60:
            h += 1
            m -= 60
        
        days = 0
        currentDay = startday
        
        for t in timelogs[idx]:
            # 주말은 고려 X 
            if currentDay == 6 or currentDay == 7:
                currentDay = (currentDay % 7) + 1
                continue
            
            # 실제 출근한 시각
            checkHour, checkMin = t // 100, t % 100
            
            if checkHour < h or (checkHour == h and checkMin <= m):
                days += 1
            else:
                break
                
            currentDay = (currentDay % 7) + 1
            
        # 주말 제외 평일 모두 조건 만족
        if days == 5:
            answer += 1
    
    return answer