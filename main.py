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
        [1, 1, 1, 12],
        [3, -2, 1, 6],
        [4, -1, 2, 18],
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
        [-1, 1, -1, -4],
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
        # self.fill()
        print(self)
        self.simplify()
        print(self)

    def simplify(self):
        self.gauss()
        print(self)
        self.reverse()
        print(self)
        self.gauss()
        print(self)
        for i, eq in enumerate(self.M):
            self.M[i][:] = self.normalize(eq, i)
        print(self)
        self.reverse()

    def gauss(self):
        for i, equation in enumerate(self.M[:-1]):
            for j, operated in enumerate(self.M[i + 1:], i + 1):
                k = operated[i] / equation[i]
                self.M[j][:] = [op - eq * k
                                for eq, op
                                in zip(equation, operated)]

    def reverse(self):
        self.reverse_h()
        self.reverse_v()

    def reverse_h(self):
        for i, equation in enumerate(self.M):
            self.M[i][:] = equation[-2::-1] + equation[-1:]

    def reverse_v(self):
        self.M[:] = self.M[::-1]

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
            lines = ['{:9.3f}'.format(k) for k in equation]
            matrix.append(' '.join(lines))
        return '\n'.join(matrix) + '\n'


if __name__ == '__main__':
    # for i in range(0, 100):
    Matrix()
