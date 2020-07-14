#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

class UnionFind():
    def __init__(self, N):
        self._id = list(range(N))
        self._sz = [1] * N  # size in num of node children

    def find(self, p: int, q: int) -> bool:
        return self.root(p) == self.root(q)

    def root(self, i: int) -> int:
        j = i
        while (j != self._id[j]):
            self._id[j] = self._id[self._id[j]]
            j = self._id[j]
        return j

    def unite(self, p: int, q: int):
        i = self.root(p)
        j = self.root(q)
        if i == j:
            return
        if self._sz[i] < self._sz[j]:
            self._id[i] = j
            self._sz[j] += self._sz[i]
        else:
            self._id[j] = i
            self._sz[i] += self._sz[j]


class basic_tests(unittest.TestCase):
    def test_init(self):
        uf = UnionFind(5)

        self.assertListEqual([0, 1, 2, 3, 4], uf._id)

    def test_find(self):
        uf = UnionFind(10)

        self.assertEqual(uf.find(5, 5), True)
        self.assertEqual(uf.find(5, 4), False)

    def test_unite_1(self):
        iv = [0, 1, 2, 3, 3, 5, 6, 7, 8, 9]
        exp = [0, 1, 2, 3, 3, 5, 6, 7, 8, 3]

        uf = UnionFind(10)
        uf._id = iv

        uf.unite(4, 9)

        self.assertListEqual(uf._id, exp)

    def test_all_1(self):
        uf = UnionFind(10)
        #  use the sample from orig pdf on p33 https://www.cs.princeton.edu/~rs/AlgsDS07/01UnionFind.pdf
        for (p, q) in [(3, 4), (4, 9), (8, 0), (2, 3), (5, 6), (5, 9), (7, 3), (4, 8), (6, 1)]:
            uf.unite(p, q)

        self.assertListEqual(uf._id, [8, 3, 3, 3, 3, 3, 3, 3, 3, 3])

        rv = uf.find(0, 1)
        self.assertTrue(rv)
        self.assertListEqual(uf._id, [3, 3, 3, 3, 3, 3, 3, 3, 3, 3])


def randperm(n, seed=42):
    import random
    random.seed(seed)
    rv = list(range(n))

    for i in range(n):
        ind = random.randint(i, n - 1)
        #  swap
        h = rv[i - 1]
        rv[i - 1] = rv[ind]
        rv[ind] = h

    return rv

def randI(n):
    import random
    import math
    return math.floor(n * random.random())

class test_rand_stuff(unittest.TestCase):

    def test_list_diff(self):
        act = randperm(10)
        exp = list(range(10))

        self.assertNotEqual(act, exp, 'list is equal')

        #  check if every element in act is in exp
        result = all(elem in act for elem in exp)
        self.assertTrue(result, 'missing elements')

        act.sort()
        self.assertListEqual(act, exp, 'same leng and all elem')

if __name__ == '__main__':
    unittest.main(verbosity=1)
