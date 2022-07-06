# Лекция 5. Функции.

## Test

- Что такое список?
    - какими свойствами он обладает?
    - какие методы и функции упрощают работу со списками?
    - что может быть элементом списка?
- Напишите инструкцию как зайти в кабинет с улицы.
    - которую стоит поместить у входа
    - если у меня завязаны глаза
    - самую короткую


## Функции

алгоритм как рецепт [пример инструкций](https://www.youtube.com/watch?v=Ct-lOOUqmyY)
функция как базовый строительный блок

NB: Как засунуть жирафа в холодильник?

Пример полезной функции.
``` python
from typing import List
def input_array() -> List[int]:
    n = int(input("size:"))
    return [int(input("next number:")) for i in range(n)]

def input_array_explicit() -> List[int]:
    n = int(input("size:"))
    result = []
    for i in range(n):
        number = int(input("next number:"))
        result.append(number)
    return result

print(f"Result {input_array()}")
```

у функции могут быть аргументы и результат

NB:
- как вскипятить пустой чайник?
- как вскипятить чайник, в котором уже есть вода?

Функции могут вызывать другие функции.
Напишите функцию которая заполняет двойной список.

``` python
from typing import List
def input_array() -> List[int]:
    n = int(input("size:"))
    return [int(input("next number:")) for i in range(n)]

def input_2d_array() -> List[List[int]]:
    m = int(input("size:"))
    return [input_array() for i in range(n)]
print(f"Result {input_array()}")
```

Функции могут вызывать сами себя

NB: Развернем список
```python
def reverse_print(input: List[int]):
    for item in input[::-1]:
        print item
    
def reverse_print_rec(input: List[int]):
    head, *tail = input
    if(len(tail) != 0):
        reverse_print_rec(tail)
    print(head)

reverse_print([1, 2, 3])
reverse_print_rec([1, 2, 3])
```