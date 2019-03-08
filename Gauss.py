#!/usr/bin/env python3
from threading import Thread
from random import random, randint
from functools import reduce


class Matrix(object):

    def __init__(self, size=5):
        self.fill(size)

        # Remove redundant equations.
        if len(self.M) >= len(self.M[0]):
            self.M = self.M[:len(self.M[0]) - 1]

    def gauss(self):
        # Pick an equation.
        for eq in range(0, len(self.M)):
            # Compute over all other equations.
            for op in range(0, len(self.M)):
                if eq == op:
                    continue

                k = self.M[op][eq] / self.M[eq][eq]
                self.M[op][:] = map(
                    lambda e, o: o - e * k,
                    self.M[eq],
                    self.M[op])

            self.M[eq][:] = self.normalize(self.M[eq], eq)

    def gauss_parallel(self):
        raise NotImplementedError

    def fill(self, size=5):
        arguments = [(random() - 0.5) * 20 for x in range(0, size)]
        print(arguments)

        matrix = []
        for i in range(0, size):
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
    # for i in range(0, 100):
    a = Matrix(size=10)
    print(a)
    a.gauss()
    print(a)
