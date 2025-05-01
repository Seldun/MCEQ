"""
Надеюсь более сложный тип не дадут
 Ʌ_Ʌ
(•.•)
(___)~
"""


f = open("13.txt", "r")
arr = [int(i)for i in f] # заносим элементы из файла в список, превращая их в числа

# цикл для нахождения N - минимальное число в последовательности, НЕ кратное 15.
min_N = 100001 # нам дан диапазон чисел
for N in arr:
    if abs(N) % 15 != 0:
        min_N = min(N, min_N)
count = 0
max_summ = -200002 # - 100 000 * 2 - 2
for i in range(len(arr) - 1): # если 3 последовательности, то range(len(arr) - 2)
    n1 = arr[i]
    n2 = arr[i + 1]
    # если 3 последовательности, то n3 = arr[i + 2]
    if abs(n1) % abs(min_N) == 0 and abs(n2) % abs(min_N) == 0: # очень аккуратно с отрицательными числами
        count += 1
        summ = n1 + n2
        max_summ = max(summ, max_summ)

print(count, max_summ)
