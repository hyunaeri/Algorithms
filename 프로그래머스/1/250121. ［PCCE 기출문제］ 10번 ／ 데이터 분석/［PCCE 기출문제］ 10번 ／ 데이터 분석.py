def solution(data, ext, val_ext, sort_by):  
    answer = []
    standard = ['code', 'date', 'maximum', 'remain']
    ext_idx = standard.index(ext)
    sort_idx = standard.index(sort_by)
    
    for idx, d in enumerate(data):
        if d[ext_idx] < val_ext :
            answer.append(d)
                
    # 데이터 오름차순 정렬
    answer.sort(key = lambda x : x[sort_idx])

    return answer


