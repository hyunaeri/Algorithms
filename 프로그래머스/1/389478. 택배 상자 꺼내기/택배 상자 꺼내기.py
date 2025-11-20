# 택배 상자 개수, 가로에 놓는 상자의 개수, 꺼내려는 택배 상자의 번호
def solution(n, w, num):
    answer = 0
    
    boxes = []
    
    # 1이면 그대로, -1이면 뒤집어서
    parity = 1
    row = []
    
    for i in range(1, n + 1):
        row.append(i)
        
        if len(row) == w:
            if parity == -1:
                row.reverse()
                
            boxes.append(row)
            row = []   
            parity *= -1
    
    # 남은 택배 상자가 있다면
    cnt = len(row)
    
    if cnt != 0:
        for _ in range(w - cnt):
            row.append(0)
            
        if parity == -1:
            row.reverse()
            
        boxes.append(row)
    
    # for row in boxes:
    #     print(row)
    
    target_row, target_col = 0, 0
    done = False
    
    for i in range(len(boxes)):
        for j in range(w):
            if boxes[i][j] == num:
                target_row, target_col = i, j
                done = True
                break
        
        if done : break
        
    for row in range(i, len(boxes)):
        if boxes[row][j] != 0:
            answer += 1
                  
    return answer