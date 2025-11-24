import sys
read = sys.stdin.readline

if __name__ == '__main__':
  answer = 0
  
  # 학생의 수
  N = int(read())
  
  # 학생 번호 정보
  id_info = [ read().rstrip() for _ in range(N) ]
  
  # 각 번호의 길이
  id_length = len(id_info[0])
  
  id_set = set()
  
  for k in range(1, id_length + 1):
    check = True
    
    for id in id_info:
      slice_id = id[id_length - k:]
      
      if slice_id in id_set:
        check = False
        break
      
      id_set.add(slice_id)
      
    if not check:
      id_set = set()
    
    else:
      answer = k
      break
  
  print(answer)