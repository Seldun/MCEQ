## 1. Перевод из любой системы счисления в 10

1011,01<sub>2</sub> ⇒ X<sub>10</sub>
``` python
print(int("101101", 2) / 4)
```

24,6<sub>8</sub> ⇒ X<sub>10</sub>
``` python
print(int("246", 8) / 8)
```

24,61<sub>8</sub> ⇒ X<sub>10</sub>
``` python
print(int("2461", 8) / 64)
```
---
## 2. Перевод из 10 в 2, 8, 16 (целую часть программой, а дробную руками)

### Перевод целой части
| A<sub>10</sub> ⇒ B<sub>n</sub>     | Функции |
|------------------------------------|---------|
| 11<sub>10</sub> ⇒ 1011<sub>2</sub> | `bin()` |
| 11<sub>10</sub> ⇒ 8<sub>8</sub>    | `oct()` |
| 11<sub>10</sub> ⇒ B<sub>16</sub>   | `hex()` |

11<sub>10</sub> ⇒ 1011<sub>2</sub>
``` python
print(bin(11)[2:])
```
11<sub>10</sub> ⇒ 8<sub>8</sub>
``` python
print(oct(11)[2:])
```
11<sub>10</sub> ⇒ B<sub>16</sub>
``` python
print(hex(11)[2:])
```
### Полный перевод руками (лучше не стоит алгоритмом)

![Снимок экрана от 2025-04-29 00-41-00](https://github.com/user-attachments/assets/772ba6c3-48cd-402d-9e52-45368fcdb1ac)

