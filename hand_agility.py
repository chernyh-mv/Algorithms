"""Спринт 11. Задача В. Ловкость рук."""

"""
Игра «Тренажёр для скоростной печати» представляет собой поле из клавиш 4x4.
В нём на каждом раунде появляется конфигурация цифр и точек. На клавише
написана либо точка, либо цифра от 1 до 9. В момент времени t игрок должен
одновременно нажать на все клавиши, на которых написана цифра t. Гоша и
Тимофей могут нажать в один момент времени на k клавиш каждый. Если в момент
времени t нажаты все нужные клавиши, то игроки получают 1 балл.
Найдите число баллов, которое смогут заработать Гоша и Тимофей, если будут
нажимать на клавиши вдвоём.

Формат ввода
В первой строке дано целое число k (1 ≤ k ≤ 5).
В четырёх следующих строках задан вид тренажёра –— по 4 символа в каждой строке.
Каждый символ —– либо точка, либо цифра от 1 до 9. Символы одной строки идут
подряд и не разделены пробелами.

Формат вывода
Выведите единственное число –— максимальное количество баллов, которое смогут
набрать Гоша и Тимофей.

Пример 1
Ввод	          Вывод
3                 2
1231
2..2
2..2
2..2

Пример 2
Ввод	          Вывод
4                 1
1111
9999
1111
9911.
"""

"""ID 71194448."""


def simulator_for_printing(k, matrix):
    simulator = []
    players = k * 2
    win_count = 0
    for i in range(1, 10):
        simulator_count = matrix.count(str(i))
        simulator.append(simulator_count)
    for i in simulator:
        if i == 0:
             continue
        elif i <= players:
             win_count += 1
    return win_count


if __name__ == "__main__":
    k = int(input())
    matrix = "".join([input().strip() for _ in range(4)])
    print(simulator_for_printing(k, matrix))