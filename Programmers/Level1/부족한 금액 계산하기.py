def solution(price, money, count):
    total = 0
    for i in range(price, price*count+1, price):
        total += i
    return total-money if money<total else 0