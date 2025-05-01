"""
Это  программа, в которой строка строится с n количеством каких-то символов
"""
for n in range(4,10000):
    s = '5' + n*'2'

    while '72' in s or '522' in s or '2222' in s: # очерёдность if очень важна!!! см алоритм в задании
        if '72' in s:
            s = s.replace('72','2',1)
        if '522' in s:
            s = s.replace('522','27',1)
        if '2222' in s:
            s = s.replace('2222','5',1)

    summ = sum(int(i) for i in s) # сумма цифр в строке
    if summ == 63:
        print(n)
