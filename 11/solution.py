"""
Kак строится начало цикла:
    Нам дано выражение: 154x312 + 1x36512

    Сначала смотрим 1 ли у нас переменная, у нас только "x"
    Потом смотрим совпадают ли системы счисления, у нас совпадает и равна 12

    Если переменная 1, но системы счислеия не совпадают, то мы находим наименьшую систему счисления и заносим её значение в range()
    Если переменных 2, они стоят в разных цифрах и системы счисления совпадают, то мы просто пишем цикл в цикле
    for x inn range(система счисления):
        for y in range(система счисления):

    Более сложные типы онии навряд ли дадут
    ВАЖНО!!!
    Если цифра начинается с неизвестной ( y04x5(11) ), то в range(1,11) , так как не может быть 0"""
for x in range(12):
    a = 1* 12**4 + 5 * 12**3 + 4 * 12**2 + x * 12**1 + 3 * 12**0
    b = 1 * 12**4 + x * 12**3 + 3 * 12**2 + 6 * 12 + 5
    c = a + b
    if c % 13 == 0:
        print(c//13)
