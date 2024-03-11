def solution(num):
    if num < 0:
        return 0

    summa2 = 0
    for i in range(num):
        if i % 3 == 0 or i % 5 == 0:
            summa2 += i

    return summa2