burger = []
for _ in range(3):  # 3번은 버거가격
    burger.append(int(input()))
    
drink = []
for _ in range(2):  # 2번은 음료가격
    drink.append(int(input()))

min_set = min(burger) + min(drink) - 50  # 세트가격 = 버거가격+음료가격-50
print(min_set)