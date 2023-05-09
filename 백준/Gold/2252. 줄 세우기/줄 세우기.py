# 백준 2252 줄 세우기
import sys
from collections import deque
read = sys.stdin.readline

def topology_sort():
    queue = deque()
    result = []

    # 진입차수가 0인 모든 노드를 큐에 넣음.
    for i in range(1, N+1):
        if indegree[i] == 0:
            queue.append(i)
            result.append(i)

    while queue:
        current_student = queue.popleft()

        # 현재 학생보다 뒤에 서야 하는 학생들의 진입차수 1씩 빼기
        for next_student in students[current_student]:
            indegree[next_student] -= 1

            if indegree[next_student] == 0:
                queue.append(next_student)
                result.append(next_student)

    return result


# 학생의 수, 키 비교 횟수
N,M = map(int,read().split())
indegree = [0] * (N+1)
students = [ [] for _ in range(N+1) ]

for _ in range(M):
    # 학생 A가 B보다 앞에 서야한다.
    A,B = map(int,read().split())
    students[A].append(B)
    
    # 학생 B의 진입차수 1 증가
    indegree[B] += 1

answer = topology_sort()
print(*answer, sep = ' ')
