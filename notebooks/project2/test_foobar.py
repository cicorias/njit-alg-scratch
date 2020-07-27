# %%
import unittest

# from project2 import import_data

# from project2 import import_data

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

    # Task 4 alternative method but an adjacency list as dict.
    def get_connected_counts_alt(self):
        '''alternative implementation'''
        from collections import defaultdict
        # adj_list = defaultdict(lambda: defaultdict(lambda: 0))
        # adj_list = defaultdict(lambda: defaultdict(int))

        # this alleviates need to pre-alloc an array of n items
        # and discovering the ID's of all the unique nodes.
        mysum = defaultdict(int)
        for start, end in edges:
            # adj_list[start][end] += 1
            mysum[start] += 1
            mysum[end] += 1

        self.connected_counts_alt = mysum
        return mysum


s_fb = connected_helper()
edges_facebook = s_fb.import_data('./data/facebook_combined.txt', skip_header=False, sep=' ', cols=2)
print(len(edges_facebook))  # result is 88234

# importing GitHub graph data
s_gh = connected_helper()
edges_github = s_gh.import_data('./data/git_web_ml/musae_git_edges.csv', skip_header=True, sep=',', cols=2)
print(len(edges_github))

# import btc data
s_btc = connected_helper()
edges_btc = s_btc.import_data('./data/soc-sign-bitcoinotc.csv', skip_header=False, sep=',', cols=3)
print(len(edges_btc))

a = [[1, 2], [1, 2], [1, 2], [2, 1]]

# The following gives the top 100
fb_100 = s_fb.node_top(edges_facebook)
gh_100 = s_gh.node_top(edges_github)
btc_100 = s_btc.node_top(edges_btc)


s = connected_helper()

edges = s.import_data('./data/sample.txt')
# edges = [('a', 'b'), ('b', 'a'), ('a', 'c')]

print(s.get_connected_counts())
s.get_connected_counts_alt()

# %%








# %%
