#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

#  TODO: weight and compression additions

class UnionFind():
    def __init__(self, N):
        self._id = list(range(N))
        self._sz = [1] * N  # size in num of node children

    def find(self, p: int, q: int) -> bool:
        # return self._id[p] == self._id[q]
        return self.root(p) == self.root(q)

    def root(self, i: int) -> int:
        while i != self._id[i]:
            self._id[i] = self._id[self._id[i]]
            i = self._id[i]
        return i

    def unite(self, p: int, q: int):
        i = self.root(p)
        j = self.root(q)
        self._id[i] = j
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

    def test_root_1(self):
        uf = UnionFind(10)
        iv = [0, 0, 0, 1, 1, 1, 3, 3, 6, 6]
        exp = [0, 0, 0, 0, 1, 1, 0, 3, 6, 0]

        uf._id = iv

        self.assertEqual(len(uf._id), 10)
        self.assertEqual(len(exp), 10)

        #  uf.unite(9, 4)
        rv = uf.root(9)
        self.assertEqual(rv, 0, 'root not match')
        self.assertListEqual(exp, uf._id)

    def test_unite_1(self):
        iv = [0, 1, 2, 3, 3, 5, 6, 7, 8, 9]
        exp = [0, 1, 2, 3, 3, 5, 6, 7, 8, 3]

        uf = UnionFind(10)
        uf._id = iv

        uf.unite(4, 9)

        self.assertListEqual(uf._id, exp)

#  Implement a function randperm that takes as input a number  n,
#  and returns a random permutation of the numbers 0...n-1.
#  This was covered in lecture 7. Your implementation should use  O(1)
#  space in addition to the space needed for the output
#  (Note: you can use any random number generator functions from
#  Python's random module, but you have to give you own implementation for randperm)

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
