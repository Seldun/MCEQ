"""
Сначала подставляем известные значения p и q в формулу f(n) = (p – 1)·(q – 1)
и находим f(n). В программе это значение функции будет обозначино как f

Далише подставляем уже известное значение е и пишем цикл для перебора всех значений d

if нужен для отображения подходящих значений, а именно в каких случиях (d·e) % f(n)
будет равно 1
"""
f = (5 - 1) * (7 - 1)
for d in range(40):
    if ((d * 11) % f) == 1:
        print(d) # наибольшее число - 35