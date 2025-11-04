# 백준 20546
# 실버 5
# https://www.acmicpc.net/problem/20546

import sys
read = sys.stdin.readline

# 준현, 성민 보유 현금
init_cash = int(read())

# 주가 정보
stock_info = list(map(int, read().rstrip().split()))

def j_investment(current_cash):
  cash = current_cash
  stock_inventory = 0
  
  for i in range(14):
    price = stock_info[i]
    
    # 보유 현금보다 현재 주가가 높으면
    if cash < price:
      continue
    
    # 아니면 구매
    buy = cash // price
    stock_inventory += buy
    cash -= (buy * price)
  
  return cash, stock_inventory

def s_investment(current_cash):
  cash = current_cash
  stock_inventory = 0
  increase_cnt, decrease_cnt = 0, 0
  
  for i in range(1, 14):
    today, yesterday = stock_info[i], stock_info[i-1]
    
    # 전날보다 주가 상승
    if today > yesterday:
      increase_cnt += 1
      decrease_cnt = 0
    
    # 전날보다 주가 하락
    elif today < yesterday:
      decrease_cnt += 1
      increase_cnt = 0
    
    # 변동 없음
    else:
      increase_cnt = 0
      decrease_cnt = 0
    
    # 3일 연속 주가 상승, 전량 매도
    if increase_cnt == 3:
      cash += (today * stock_inventory)
      stock_inventory = 0
    
    # 3일 연속 주가 하락, 전량 매수
    if decrease_cnt == 3:
      buy = cash // today
      stock_inventory += buy
      cash -= (buy * today)
    
  return cash, stock_inventory

j_cash, j_stock_inventory = j_investment(init_cash)
s_cash, s_stock_inventory = s_investment(init_cash)

# 보유 주식 현금으로 환산
total_j_cash = j_cash + (j_stock_inventory * stock_info[-1])
total_s_cash = s_cash + (s_stock_inventory * stock_info[-1])
  
if total_j_cash > total_s_cash: print("BNP")
elif total_j_cash < total_s_cash: print("TIMING")
else: print("SAMESAME")