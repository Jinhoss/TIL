def solution(price, money, count):
    answer = 0
    total_price =  price * (count * (count + 1))//2
    if total_price > money:
        answer = total_price - money

    return answer