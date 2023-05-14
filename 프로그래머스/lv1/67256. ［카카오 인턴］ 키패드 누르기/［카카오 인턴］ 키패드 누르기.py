def solution(numbers, hand):
    answer = ''
    key_xy = { 1:[0,0], 2:[0,1], 3:[0,2], 4:[1,0], 
            5:[1,1], 6:[1,2], 7:[2,0], 8:[2,1], 9:[2,2], 0:[3,1]}
    
    # 왼쪽(*), 오른쪽(#) 엄지손가락의 초기 위치
    left_thumb = [3,0]
    right_thumb = [3,2]
    
    for num in numbers:
        if num in [1,4,7]:
            answer += 'L'
            left_thumb = key_xy[num]
        elif num in [3,6,9]:
            answer += 'R'
            right_thumb = key_xy[num]
        else:
            dist_left = abs(left_thumb[0] - key_xy[num][0]) + abs(left_thumb[1] - key_xy[num][1])
            dist_right = abs(right_thumb[0] - key_xy[num][0]) + abs(right_thumb[1] - key_xy[num][1])
            
            if dist_left < dist_right:
                answer += 'L'
                left_thumb = key_xy[num]
            elif dist_left > dist_right:
                answer += 'R'
                right_thumb = key_xy[num]
            else:
                if hand == 'left':
                    answer += 'L'
                    left_thumb = key_xy[num]
                else:
                    answer += 'R'
                    right_thumb = key_xy[num]
            
    return answer