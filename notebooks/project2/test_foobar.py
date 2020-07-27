# %%

import unittest

class connected_helper:
    def __init__(self, G: list = None):
        if G is not None:
            self.G = G

        self.max_id = 0

    # Task 2
    def import_data(self, filename,
                    skip_header = False,
                    sep = ',',
                    cols = 2) -> list:
        rv = []
        with open(filename, 'rt') as f:
            for line in f:
                if skip_header:
                    skip_header = False
                    continue
                row = line.strip().split(sep)[0:cols]
                self.max_id = max(self.max_id, int(row[0]), int(row[1]))  # needed later.
                rv.append(row)
                assert len(rv[len(rv) - 1]) == cols

        self.G = rv
        return rv

    # Task 3 implementation
    def node_freq(self, directed=False):
        '''faster implementation'''
        rv = {}
        for r in self.G:
            if not directed:
                if not r[0] in rv:
                    rv[r[0]] = 1
                else:
                    rv[r[0]] += 1
                if not r[1] in rv:
                    rv[r[1]] = 1
                else:
                    rv[r[1]] += 1
            else:
                if not r[1] in rv:
                    rv[r[1]] = 1
                else:
                    rv[r[1]] += 1

        #  return rv
        return list(rv.items())  # list of tuples

    # Task 3 - alternative and crappy way
    def node_frequency(self, directed=False):
        '''attempt with numpy
        this is NOT used....'''
        import numpy as np
        if not directed:  # undirected
            #  this flips the orig and concatenates it again
            a_all = np.concatenate((self.G, np.flip(self.G, axis=1)))
        else:
            a_all = self.G

        unique, counts = np.unique(np.array(a_all)[:, 1], return_counts=True)
        frequencies = np.asarray((unique, counts)).T

        return frequencies

    # Task 3
    def node_top(self, count=100):
        return sorted(
            self.node_freq(self.G),
            key = lambda x: x[1], reverse=True)[0:100]

    # Task 4 implementation.
    def get_connected_counts(self) -> list:
        '''this just has to count each time a node
        appears. This doesn't have to report connected
        component structure...'''
        # visited = [False] * self.max_id
        cc = [0] * (self.max_id + 1)

        for edge in self.G:  # this is an edge (from,to)
            for node in edge:  # each node
                cc[int(node)] += 1

        self.connected_counts_alt = cc
        return cc

    # Task 4 implemeentation -- proper one
    #  returns an array where offset is the ID and each
    # element is the connected nodes as a sublist.
    def get_connected_nodes(self, directed=False) -> list:
        cc = [None] * (self.max_id + 1)
        visited = [False] * (self.max_id + 1)
        counts = [0] * (self.max_id + 1)

        for edge in self.G:  # edge of (from,to)
            node_from = edge[0]
            node_to = edge[1]

            if not visited[int(node_from)]:
                cc[int(node_from)] = [node_to]
                visited[int(node_from)] = True
                #  counts[int(node_from)] = 1
            else:
                cc[int(node_from)] = cc[int(node_from)] + [node_to]

            counts[int(node_from)] += 1

            if not directed:
                if not visited[int(node_to)]:
                    cc[int(node_to)] = [node_from]
                    visited[int(node_to)] = True
                    #  counts[int(node_to)] = 1
                else:
                    cc[int(node_to)] = cc[int(node_to)] + [node_from]

                counts[int(node_to)] += 1

        self.connected_nodes = cc
        self.connected_counts = counts
        return cc

    def get_largest_node_degree(self):
        if self.G is None:
            raise 'Must iomport data first'

        _ = self.get_connected_nodes()
        max_index = self.connected_counts.index(max(self.connected_counts))

        return max_index, self.connected_nodes[max_index]

    #  def dfs_util(self, node, visited):
    #     visited[int(node)

    # Task 4 alternative method but an adjacency list as dict.
    def get_connected_counts_alt(self):
        '''alternative implementation'''
        from collections import defaultdict
        # adj_list = defaultdict(lambda: defaultdict(lambda: 0))
        # adj_list = defaultdict(lambda: defaultdict(int))

        # this alleviates need to pre-alloc an array of n items
        # and discovering the ID's of all the unique nodes.
        mysum = defaultdict(int)
        for start, end in self.G:
            # adj_list[start][end] += 1
            mysum[start] += 1
            mysum[end] += 1

        self.connected_counts_alt2 = mysum
        return mysum


# %%

class test_one(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_one(self):
        arr = [['0', '2'], ['0', '3'], ['1', '1']]
        s = connected_helper(G=arr)
        s.max_id = 3
        cn = s.get_connected_nodes()

        self.assertIsNotNone(cn)

    def test_with_fb(self):
        s_fb = connected_helper()
        s_fb.import_data('notebooks/project2/data/facebook_combined.txt', skip_header=False, sep=' ', cols=2)
        cn = s_fb.get_connected_nodes()
        cn_2 = s_fb.get_connected_counts()
        self.assertIsNotNone(cn)
        self.assertListEqual(cn_2, s_fb.connected_counts_alt, 'two connected counts')

    def test_larget_node(self):
        s_fb = connected_helper()
        s_fb.import_data('notebooks/project2/data/facebook_combined.txt', skip_header=False, sep=' ', cols=2)
        index, con_nodes = s_fb.get_largest_node_degree()

        print('larget node has {}'.format(len(con_nodes)))

        self.assertIsNotNone(con_nodes)
        self.assertEqual(1045, len(con_nodes), 'length of connections')
        self.assertEqual(107, index, 'index of larget node')
        self.assertEqual(s_fb.connected_counts[107], len(con_nodes))




        

# %%
