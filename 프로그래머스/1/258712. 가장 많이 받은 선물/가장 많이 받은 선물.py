def solution(friends, gifts):
    answer = [0] * len(friends)
    
    # {이름: 인덱스} 딕셔너리 꼴로
    names = {name : idx for idx, name in enumerate(friends)}
    # print(names)
    
    # 인접 행렬
    gift_matrix = [ [0]*len(friends) for _ in range(len(friends)) ]
    
    # 총 받은 선물 수
    take_presents = [0] * len(friends)
    
    # 총 준 선물 수
    give_presents = [0] * len(friends)
    
    for f in gifts:
        giver, taker = f.split(' ')
        gift_matrix[names[giver]][names[taker]] += 1
        
    #print(gift_matrix)
    
    for i in range(len(friends)):
        give_presents[i] = sum(gift_matrix[i])
        for temp in gift_matrix:
            take_presents[i] += temp[i]
            
    #print(take_presents)
    #print(give_presents)
    
    # 선물 지수
    gift_val = [0] * len(friends)
    for i in range(len(friends)):
        gift_val[i] = give_presents[i] - take_presents[i]
                                                       
    #print(gift_val)                                                
        
    for i in range(len(friends)):
        for j in range(i+1, len(friends)):
            # i가 j 보다 선물을 많이 줬으면
            if gift_matrix[i][j] > gift_matrix[j][i]:
                answer[i] += 1
            elif gift_matrix[j][i] > gift_matrix[i][j]:
                answer[j] += 1
            # 준 선물 수가 서로 같으면
            else:
                if gift_val[i] > gift_val[j]:
                    answer[i] += 1
                elif gift_val[j] > gift_val[i]:
                    answer[j] += 1

    #print(answer)
    return max(answer)
                    
                

    
    
        
    
    
    
    
    
    