# 백준 7785 회사에 있는 사람
import sys
read = sys.stdin.readline

# 출입 로그의 수
n = int(read())
people = {}

for _ in range(n):
    name, command = read().rstrip().split()
    if command == 'enter':
        people[name] = 'enter'

    elif command == 'leave':
        if people[name]:
            del people[name]
            
# 딕셔너리에서 키를 역 사전순으로 정렬           
people = sorted(people.keys(), reverse=True)
# 이 출력 방식은 딕셔너리에서 키만 출력됨
print(*people, sep='\n')