#!/usr/bin/env python3
import multiprocessing as mp
from random import random
from functools import reduce


class Matrix(object):

    NUMBER_OF_THREADS = 4

    def __init__(self, size=5):
        self.fill(size)

        # Remove redundant equations.
        if len(self.M) >= len(self.M[0]):
            self.M = self.M[:len(self.M[0]) - 1]

    def gauss(self):
        self.simplify_column(0, len(self.M))

    def gauss_parallel(self):
        pool = mp.Pool(self.NUMBER_OF_THREADS)
        length = len(self.M) // self.NUMBER_OF_THREADS
        res = [pool.apply_async(self.simplify_column,
                                (eq * length, (eq + 1) * length))
               for eq
               in range(0, self.NUMBER_OF_THREADS)]

        [r.get() for r in res]

    def fill(self, size=5):
        arguments = [(random() - 0.5) * 20 for x in range(0, size)]

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

    def simplify_column(self, start, end):
        # Pick an equation.
        for eq in range(start, end):
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

    def __str__(self):
        matrix = []
        for equation in self.M:
            line = ' '.join(['{:9.3f}'.format(k) for k in equation])
            matrix.append(line)
        return '\n'.join(matrix) + '\n'


if __name__ == '__main__':
    a = Matrix(size=10)
    print(a)
    a.gauss()
    # a.gauss_parallel()
    print(a)
