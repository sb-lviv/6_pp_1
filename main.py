#!/usr/bin/env python3
from threading import Thread
from random import random, randint
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
    ]
    args = []
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
        for i in range(0, len(self.M)):
            self.M[i] = self.normalize(self.M[i], i)

    def forward(self):
        for equation in range(0, len(self.M) - 1):
            self.M[equation:] = sorted(self.M[equation:],
                                       key=lambda x: abs(x[equation]),
                                       reverse=True)
            for operated in range(equation + 1, len(self.M)):
                k = self.M[operated][equation] / self.M[equation][equation]
                self.M[operated][:] = map(
                    lambda eq, op: op - eq * k,
                    self.M[equation],
                    self.M[operated])

    def backward(self):
        for equation in range(len(self.M) - 1, 0, -1):
            for operated in range(0, equation):
                k = self.M[operated][equation] / self.M[equation][equation]
                self.M[operated][:] = map(
                    lambda eq, op: op - eq * k,
                    self.M[equation],
                    self.M[operated])


    def reverse(self):
        self.reverse_h()
        self.reverse_v()

    def reverse_h(self):
        for i, equation in enumerate(self.M):
            self.M[i] = equation[-2::-1] + equation[-1:]

    def reverse_v(self):
        self.M = self.M[::-1]

    def fill(self):
        arguments = [(random() - 0.5) * 20 for x in range(0, randint(3, 5))]
        print(arguments)

        matrix = []
        for arg in arguments:
            l = [(random() - 0.5) * 20 for x in arguments]
            s = [arg * k for arg, k in zip(arguments, l)]
            s = reduce((lambda x, y: x + y), s)
            l.append(s)
            matrix.append(l)
        self.M = matrix
        self.args = arguments

    def get_result(self):
        return [equation[-1] for equation in self.M]

    def validate(self):
        for a, b in zip(self.args, self.get_result()):
            if abs(a - b) > 0.000001:
                return False
        return True

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
        print(Matrix().validate())
