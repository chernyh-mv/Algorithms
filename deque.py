"""Спринт 12. Задача A. Дек."""

"""
Гоша реализовал структуру данных Дек, максимальный размер которого определяется
заданным числом. Методы push_back(x), push_front(x), pop_back(), pop_front()
работали корректно. Но, если в деке было много элементов, программа работала
очень долго. Дело в том, что не все операции выполнялись за O(1). Помогите Гоше!
Напишите эффективную реализацию.
Внимание: при реализации используйте кольцевой буфер.

Формат ввода
В первой строке записано количество команд n — целое число, не превосходящее 100000.
Во второй строке записано число m — максимальный размер дека. Он не превосходит 50000.
В следующих n строках записана одна из команд:
push_back(value) – добавить элемент в конец дека. Если в деке уже находится
                   максимальное число элементов, вывести «error».
push_front(value) – добавить элемент в начало дека. Если в деке уже находится
                   максимальное число элементов, вывести «error».
pop_front() – вывести первый элемент дека и удалить его. Если дек был пуст,
                   то вывести «error».
pop_back() – вывести последний элемент дека и удалить его. Если дек был пуст,
                   то вывести «error».
Value — целое число, по модулю не превосходящее 1000.

Формат вывода
Выведите результат выполнения каждой команды на отдельной строке. Для успешных
запросов push_back(x) и push_front(x) ничего выводить не надо.

Пример 1
Ввод	                Вывод
4                       861
4                       -819
push_front 861
push_front -819
pop_back
pop_back

Пример 2
Ввод	                Вывод
7                       -855
10                      0
push_front -855         844
push_front 0
pop_back
pop_back
push_back 844
pop_back
push_back 823.
"""

"""ID 72445915."""


class Deque:
    def __init__(self, max_size: int) -> None:
        self.queue = [None] * max_size
        self.max_n = max_size
        self.head = 0
        self.tail = 0
        self.size = 0
            
    def is_empty(self) -> None:
        return self.size == 0

    def push_back(self, value: int) -> None:
        """Добавление числа в конец дека."""
        if self.size == self.max_n:
            raise IndexError('Дек полностью заполнен!')
        self.tail = (self.tail + 1) % self.max_n
        self.queue[self.tail - 1] = value
        self.size += 1

    def push_front(self, value: int) -> None:
        """Добавление числа в начало дека."""
        if self.size == self.max_n:
            raise IndexError('Дек полностью заполнен!')
        self.head = (self.head - 1) % self.max_n
        self.queue[self.head] = value
        self.size += 1

    def pop_back(self) -> int:
        """Вывод последнего значения."""
        if self.is_empty():
            raise IndexError('Дек пуст!')
        self.tail = (self.tail - 1) % self.max_n
        x = self.queue[self.tail]
        self.size -= 1
        return x
 

    def pop_front(self) -> int:
        """Вывод первого значения."""
        if self.is_empty():
            raise IndexError('Дек пуст!')
        self.head = (self.head + 1) % self.max_n
        x = self.queue[self.head - 1]
        self.size -= 1
        return x

def main():
    command_length = int(input())
    max_size = int(input())
    deque = Deque(max_size)
    result = []
    for i in range(command_length):
        try:
            command = input().split()
            if command[0] == 'push_back':
                a = deque.push_back(command[1])
            if command[0] == 'push_front':
                a = deque.push_front(command[1])
            if command[0] == 'pop_back':
                a = deque.pop_back()
            if command[0] == 'pop_front':
                a = deque.pop_front()
            if a is not None:
                print(a)
        except IndexError:
                print('error')
    print

if __name__ == '__main__':
    main()
