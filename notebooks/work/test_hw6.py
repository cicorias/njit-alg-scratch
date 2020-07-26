#!/usr/bin/env python
# -*- coding: utf-8 -*-

# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# # **Assignment 6** #
# **Delivery Instructions**:  Similar to previous assignments. See this [**Canvas announcement**](https://njit.instructure.com/courses/11882/discussion_topics/42914) for more details.
#
# ---
# #### **Important Note**: If you want to follow the alternative track, as I explained in a previous discussions, you can skip questions marked with ^^. Please let me know that you do that !
# %% [markdown]
# ---
# ### **Q1. Check BST validity**  ###
# Recall the definition of a the Node class which can be used for implementing binary trees. Write a function that takes as input such a tree $T$, and outputs True if $T$ is a valid BST, or False otherwise.  [Hint: Think recursion]

# %%
# your implementation goes here

import unittest

class Node:
    def __init__(self, key):
        self.key = key
        self.lchild = None
        self.rchild = None

    # @property
    # def key(self):
    #     return self.key

def checkBSTValidity(T: Node) -> bool:
    '''BST rules:
    - every node has at MOST 2 children
    - a node's left child is <= self(parent)
    - a node's right child is >= self(parent)
    '''
    if T.lchild is None and T.rchild is None:
        return True

    if T.lchild is not None and T.lchild.key <= T.key:
        #  venture down
        if checkBSTValidity(T.lchild) and T.rchild is None:
            return True

        return True

    if T.rchild is not None and T.rchild.key >= T.key:
        #  venture down.
        if checkBSTValidity(T.rchild) and T.lchild is None:
            return True

        return True

    return False


#  '''
#         5
#        / \
#       /   \
#      /     \
#     3       8
#    / \     / \
#   2   4   7   10
#  /               \
# 1                12
#  '''

class NodeCollection:
    def __init__(self):
        self.n5 = Node('5')
        self.n3 = Node('3')
        self.n2 = Node('2')
        self.n1 = Node('1')
        self.n4 = Node('4')
        self.n8 = Node('8')
        self.n7 = Node('7')
        self.n10 = Node('10')
        self.n12 = Node('12')

        self.n5.lchild = self.n3
        self.n5.rchild = self.n8
        self.n3.lchild = self.n2
        self.n3.rchild = self.n4
        self.n2.lchild = self.n1
        self.n8.lchild = self.n7
        self.n8.rchild = self.n10
        self.n10.rchild = self.n12

        self.all = [self.n1, self.n2, self.n3, self.n4, self.n5, self.n7, self.n8, self.n10, self.n12]

    @property
    def all_nodes(self):
        return self.all


class test_bst_validity(unittest.TestCase):
    def setUp(self):
        self.nodes = NodeCollection()
        self.all = self.nodes.all_nodes

    def test_all(self):
        for n in self.all:
            self.assertTrue(checkBSTValidity(n), 'failed node in {}'.format(n.key))


# %% [markdown]
# ---
#
#
# ### **Q2. Find the height of a Binary Tree**
#
# Write a function *BT_Height* that takes as input a binary tree and computes its height. [Hint: Again, think recursion]
#
# Side Note: If a BST is fully balanced then its height is exactly $\lceil \log_2 n \rceil$. So, the height computation allows you to check if a tree is fully balanced.

# %%
# your implementation goes here

def BT_Height(T, h=None) -> int:
    if h is None:
        h = 1  # make this 1 if we want to count root as a level????
    else:
        h += 1

    if T.lchild is None and T.rchild is None:
        return h

    rv = 0
    if T.lchild is not None:
        #  venture down
        rv = BT_Height(T.lchild, h)

    if T.rchild is not None:
        #  venture down.
        rv = max(rv, BT_Height(T.rchild, h))

    return rv

class test_bst_height(unittest.TestCase):
    def setUp(self):
        self.nodes = NodeCollection()
        self.all = self.nodes.all_nodes

    def test_height_n5(self):
        exp = 4
        act = BT_Height(self.all[4])  # the root 5
        print('key is {}'.format(self.all[4].key))
        self.assertEqual(exp, act, 'height from root')

    def test_height_n8(self):
        exp = 3
        act = BT_Height(self.all[6])  # node 8
        print('key is {}'.format(self.all[6].key))

        self.assertEqual(exp, act, 'height from root')

    def test_log2height(self):
        import math
        n = len(self.all)
        exp = math.ceil(math.log2(n))
        act = BT_Height(self.all[4])  # the root 5
        self.assertEqual(exp, act, 'log and height')


# %% [markdown]
# ---
#
#
# ### **Q3.  Find the closest leaf**  <br>
#
# Write a function *BT_ClosestLeaf* that takes as input a binary tree and computes the distance of the root to its closest leaf.

# %%
# your code goes here


def BT_ClosestLeaf(T: Node) -> Node:
    #  Base Case
    if T is None:
        return 2**10000
    if T.lchild is None and T.rchild is None:
        return 0

    #  get the min between two downward paths.

    rv = BT_ClosestLeaf(T.lchild)
    rv = min(rv, BT_ClosestLeaf(T.rchild))

    return 1 + rv


class test_root_closest_leaf(unittest.TestCase):
    def setUp(self):
        self.nodes = NodeCollection()
        self.all = self.nodes.all_nodes

    def test_root(self):
        exp = 2
        act = BT_ClosestLeaf(self.all[4])  # the root 5
        self.assertEqual(exp, act, 'leaf distance')


# %% [markdown]
# ---
#
#
# ### **Q4^^**. Sorted array to BST
#
# In the lecture we briefly discussed that inserting keys in a random order, will give a balanced tree with high probability. However, it's likely that the tree will not be fully balanced. Suppose now that we have already a sorted array of elements $S$ and we want to convert it to a **fully** balanced search tree. Write a function that accomplishes that goal

# %%

#  output should be a Tree.
def sortedToBST(S: list) -> Node:
    ''' I swear we did this before... '''
    if not S:
        return None

    #  get the midpoint as an int
    mid = (len(S)) // 2

    #  mid point is a root candidate.
    root = Node(S[mid])

    #  build out the left which are lt
    root.lchild = sortedToBST(S[:mid])

    #  build out the right which are gt
    root.rchild = sortedToBST(S[mid + 1:])

    return root


class test_sorted_to_bst(unittest.TestCase):
    def setUp(self):
        self.arr_1 = [1, 2, 3, 4, 5, 6, 7]
        self.nodes = NodeCollection()
        self.all = self.nodes.all_nodes
        self.arr = list([i.key for i in sorted(self.all, key=lambda x: x.key)])

#     4
#    / \
#   /   \
#  2     6
# / \   / \
# 1 3  5   7

    def test_one(self):
        act = sortedToBST(self.arr_1)
        rv = checkBSTValidity(act)
        print_bst(act)
        self.assertTrue(rv)
        self.assertEqual(3, BT_Height(act), 'height')

    def test_two(self):
        act = sortedToBST(self.arr)
        rv = checkBSTValidity(act)
        print_bst(act)
        self.assertTrue(rv)
        self.assertEqual(4, BT_Height(act), 'height')

def print_bst(node: Node):
    if not node:
        return

    print(node.key),
    print_bst(node.lchild)
    print_bst(node.rchild)

# %% [markdown]
# ---
# ### **Q5. Find Max in BST**
# Write a function *BST_max* that takes as input a BST and returns the maximum key in it. This function should be iterative.

# %%
def BST_max(T: Node) -> int:
    current = T
    #  always go right....
    while(current.rchild):
        current = current.rchild
    return current.key

class test_find_max_key(unittest.TestCase):
    def setUp(self):
        self.arr_1 = [1, 2, 3, 4, 5, 6, 7]
        self.nodes = NodeCollection()
        self.all = self.nodes.all_nodes
        self.arr = list([i.key for i in sorted(self.all, key=lambda x: x.key)])

    def test_one(self):
        act = BST_max(self.all[6])

        self.assertEqual('12', act, 'bst max')


# %% [markdown]
# ---
# ### **Q6^^**. Check Red-Black Tree Validity
# In the following cell, I give the definition of a class that can be used to build Red-Black Trees. The *color* attribute is assumed to be 1 or 0, where 1 means 'black' and 0 means 'red'.
# Write a function *checkRBTreeValidity* that takes as input a RB Tree $T$ and outputs True if $T$ satisfies all RB properties we discussed in the lecture, and false otherwise.
#
# **Note 1**: As we discussed in the lecture the 'None' children are considered as black nodes without keys.
#
# **Note 2**: Checking if a RB-Tree is a BST is also part of the question, but for it you can use Q1.

# %%
class RBNode:
    def __init__(self, key, color=None):
        self.key = key
        self.lchild = None
        self.rchild = None
        if color is not None:
            self.color = 1  # black 0 = Red


def checkRBValidity(T: Node):
    '''BST rules:
    - every node has at MOST 2 children
    - a node's left child is <= self(parent)
    - a node's right child is >= self(parent)
    RB rules
    - root is black
    - leaves are black
    - parent of red node is black
    - height of x to leaf is always same n black nodes
    '''

    if T is None:  # leaf
        return True

    if T.lchild is None and T.rchild is None:
        return True

    if T.lchild is not None and T.lchild.key <= T.key:
        #  venture down
        if checkBSTValidity(T.lchild) and T.rchild is None:
            return True

        return True

    if T.rchild is not None and T.rchild.key >= T.key:
        #  venture down.
        if checkBSTValidity(T.rchild) and T.lchild is None:
            return True

        return True

    return False


def create_RB_bst():
    root = RBNode(7, color=1)
    root.lchild = RBNode(3, 1)
    root.rchild = RBNode(18, 0)
    root.rchild.lchild = RBNode(10, 1)
    root.rchild.rchild = RBNode(22, 1)
    root.rchild.lchild.lchild = RBNode(8, 0)
    root.rchild.lchild.rchild = RBNode(11, 0)
    root.rchild.rchild.rchild = RBNode(26, 0)

    return root

class test_RB_BST(unittest.TestCase):
    def setUp(self):
        self.tree = create_RB_bst()

    def test_exist(self):
        self.assertIsNotNone(self.tree)
        self.assertTrue(checkRBValidity(self.tree))
    


# %%
if __name__ == '__main__':
    unittest.main(verbosity=1)
