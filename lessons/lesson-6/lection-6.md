## Тест

- Обьясните что написано `def find(xs:List[int], k: int = 10) -> int`
- Напишите функцию которая получает на вход число n, а возвращает список чисел по порядку от 0 до n.
- Напишите функцию которая получает на вход числа `a, b, k`, а возвращает k случайных чисел из интервала a, b.

Поиск минимального элемента
check find.py
```python
def find_minimal(xs: List[int]) -> int:
  pass

def find_2_minimal(xs: List[int]) -> List[int]:
  pass
```

## Сложность

Функции различаются по тому как долго они будут считаться.
Хорошим примером подсчета является сколько простых операций нужно функции, чтобы выполниться.

усложнение функции:
- вывести букву
- вывести слово
- вывести строчку
- вывести страницу
- вывести книгу

Сортировка на время (раздаточный материал, квадратики с числами до 100).
- Найдите 42
- Разделите на две кучки, до 42 и больше
- Отсортируйте по порядку

- Какая из задач самая сложная/простая?
- Была бы задача сложнее если бы чисел было 200?

Давайте займемся [пузырями](./bubbles.py)

## Домашнее задание
- Написать функцию которая возвращает два самых маленьких элемента
`def find_max(xs: List[int]) -> List[int]`

- Написать функцию которая возвращается индекс заданного элемента в списке, либо -1.
`def index(xs: List[int], elem: int) -> Optional[int]`

- написать программу которая рисует случайное дерево
  - у дерева есть ствол
  - от ствола случайно отходят ветки
  - от каждой ветки могут отходить ветки по меньше
  - каждая ветка заканчивается листом

