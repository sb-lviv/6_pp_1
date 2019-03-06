#!/usr/bin/env python3
from threading import Thread
from random import randint
from functools import reduce


class Matrix(object):

    # M = [
    #     [2, 1, -1, 8],
    #     [-3, -1, 2, -11],
    #     [-2, 1, 2, -3],
    # ]

    M = [
        [2, 1, -1, 8],
        [-3, -1, 2, -11],
        [-2, 1, 2, -3],
    ]
    """ fixme """
    """
    M = [
        [10, -9, 4, 2],
        [0, -2, 5, -10],
        [-7, 2, 4, -15],
    ]
    """
    """ fixme """
    """
    M = [
        [3, 3, 3, 36],
        [-2, 1, -1, -7],
        [1, -1, 2, 9],
        [-3, -2, 1, -12],
    ]
    """
    """ fixme """
    """
    M = [
        [1, 1, 1, 12],
        [3, -2, 1, 6],
    ]
    """

    def __init__(self):
        self.fill()
        print(self)
        self.run()
        print(self)

    def run(self):
        if len(self.M) >= len(self.M[0]):
            self.M = self.M[:len(self.M[0]) - 1]
        self.gauss()

    def gauss(self):
        self.forward()
        self.backward()

    def forward(self):
        for i, equation in enumerate(self.M[:-1]):
            for j, operated in enumerate(self.M[i + 1:], i + 1):
                k = operated[i] / equation[i]
                self.M[j][:] = map(
                    lambda eq, op: op - eq * k,
                    equation,
                    operated)

    def backward(self):
        for i, equation in reversed(list(enumerate(self.M[1:], 1))):
            for j, operated in enumerate(self.M[:i]):
                k = operated[i] / equation[i]
                self.M[j][:] = map(
                    lambda eq, op: op - eq * k,
                    equation,
                    operated)

    def reverse(self):
        self.reverse_h()
        self.reverse_v()

    def reverse_h(self):
        for i, equation in enumerate(self.M):
            self.M[i] = equation[-2::-1] + equation[-1:]

    def reverse_v(self):
        self.M = self.M[::-1]

    def fill(self):
        arguments = [randint(-10, 10) for x in range(0, randint(3, 5))]
        print(arguments)

        matrix = []
        for arg in arguments:
            l = [randint(-10, 10) for x in arguments]
            s = [arg * k for arg, k in zip(arguments, l)]
            s = reduce((lambda x, y: x + y), s)
            l.append(s)
            matrix.append(l)
        self.M = matrix

    @staticmethod
    def normalize(equation, position):
        k = 1 / equation[position]
        return [x * k for x in equation]

    def __str__(self):
        matrix = []
        for equation in self.M:
            line = ' '.join(['{:9.3f}'.format(k) for k in equation])
            matrix.append(line)
        return '\n'.join(matrix) + '\n'


if __name__ == '__main__':
    for i in range(0, 100):
        Matrix()
