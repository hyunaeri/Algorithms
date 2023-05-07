# 백준 4673 셀프넘버
# set 자료형은 중복이 없고, 순서도 없다.
# 마지막 셀프넘버 set를 만든 후 정렬을 해주어야 함.

natural_numbers = set(range(1, 10001))
remove_set = set()

for num in natural_numbers:
  for n in str(num):
    num += int(n)
  remove_set.add(num)

self_numbers = natural_numbers - remove_set
for self_num in sorted(self_numbers):
  print(self_num)
