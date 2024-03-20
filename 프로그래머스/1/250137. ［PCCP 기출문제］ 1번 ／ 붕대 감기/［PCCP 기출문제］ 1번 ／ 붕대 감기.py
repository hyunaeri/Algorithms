def solution(bandage, health, attacks):
    # 기술 시전 시간, 초당 회복량, 추가 회복량
    t, x, y = bandage
    
    # 현재 연속 성공 시간, 현재 체력
    cur_time, cur_health, max_health = 0, health, health
       
    # 마지막 공격 시간
    end_attack_time = attacks[-1][0]
    
    # attacks 딕셔너리 (시간 : 피해량)
    attacks = {att[0] : att[1] for att in attacks}
    
    for time in range(end_attack_time + 1):
        # 공격 당함
        if time in attacks:
            cur_time = 0
            cur_health -= attacks[time]
            
            # 체력 0 이하 = 사망
            if cur_health <= 0 :
                return -1
            
            continue
            
        # 공격 당하지 않음
        cur_time += 1
        cur_health += x
        
        # 추가 회복
        if cur_time == t :
            cur_health += y
            cur_time = 0
        
        cur_health = min(cur_health, max_health)
        
    return cur_health
