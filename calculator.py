"""Спринт 12. Задача B. Калькулятор."""

"""
Задание связано с обратной польской нотацией. Она используется для парсинга
арифметических выражений. Еще её иногда называют постфиксной нотацией.
В постфиксной нотации операнды расположены перед знаками операций.
В текущей задаче гарантируется, что деления на отрицательное число нет.

Пример:
3 4 +
означает 3 + 4 и равно 7

Формат ввода
В единственной строке дано выражение, записанное в обратной польской нотации.
Числа и арифметические операции записаны через пробел.
На вход могут подаваться операции: +, -, *, / и числа, по модулю не превосходящие 10000.
Гарантируется, что значение промежуточных выражений в тестовых данных по модулю не больше 50000.

Формат вывода
Выведите единственное число — значение выражения.

Пример 1
Ввод	             Вывод
2 1 + 3 *            9

Пример 2
Ввод	             Вывод
7 2 + 4 * 2 +        38.
"""

"""ID 72341446."""

import operator
from typing import Any, List


OPERATORS = {
    '+': operator.add,
    '-': operator.sub,
    '/': operator.floordiv,
    '*': operator.mul
}


class Stack:
    def __init__(self) -> None:
        self.items = []

    def is_empty(self) -> None:
        return len(self.items) == 0

    def push(self, x: Any) -> None:
        """Добавление числа в стек."""
        self.items.append(int(x))

    def pop(self) -> int:
        """Берем число с вершины стека."""
        if self.is_empty():
            return IndexError('Стек пуст.')
        return self.items.pop()


def main(polish_notation: List[str]) -> int:
    """Вычисление выражения с обратной польской нотацией."""
    s = Stack()
    for elem in polish_notation:
        if elem in OPERATORS:
            x, y = s.pop(), s.pop()
            s.push(OPERATORS[elem](y, x))
        else:
            s.push(elem)  
    return s.pop()


if __name__ == '__main__':
    polish_notation = input().split()
    print(main(polish_notation))
