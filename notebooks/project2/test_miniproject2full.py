# %%
import numpy as np
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
                row[0] = int(row[0])
                row[1] = int(row[1])
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
    def get_connected_nodes(self, directed: bool = None, graph: list = None) -> list:
        if graph is None:
            graph = self.G
        if directed is None:
            directed = False

        cc = [None] * (self.max_id + 1)
        visited = [False] * (self.max_id + 1)
        counts = [0] * (self.max_id + 1)

        for edge in graph:  # edge of (from,to)
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

    # Task 5 parts
    def get_reversed_graph(self, graph=None):
        if graph is None:
            graph = self.G

        self.R = [None] * len(graph)
        for i, edge in enumerate(graph):  # edge of (from,to)
            node_from = edge[0]
            node_to = edge[1]
            self.R[i] = [node_to, node_from]

        return self.R

    def get_scc(self, G=None):
        # if a graph is already imported it is in the
        # [[1,2], [2,3]] format and needs to be connected component instead.
        if G is None:
            G = self.get_connected_nodes(directed=True, graph=self.G)
        else:
            G = self.get_connected_nodes(directed=True, graph=G)

        # this has to be interative as stack overflow on datasets with more than 500 edges.
        n = len(G)
        transposed = [[None]] * n
        order_w = []
        visited = [False] * n
        scc = [None] * n

        # transpose and first DFS with order by weight
        for u in range(n):
            if not visited[u]:
                visited[u] = True
                stack = [u]

                while len(stack) > 0:
                    u = stack[-1]  # peek at last item.
                    done = True
                    # tv = G[u]   # odd bug I can't id.
                    if G[u] is None:
                        break

                    for v in G[u]:
                        if transposed[v][0] is None:
                            transposed[v] = [u]
                        else:
                            transposed[v].append(u)
                        if not visited[v]:
                            visited[v] = True
                            done = False
                            stack.append(v)
                            break
                    if done:
                        stack.pop()
                        order_w.append(u)

        # second DFS on tranposed to build the scc array
        while len(order_w) > 0:
            r = order_w.pop()
            stack = [r]
            if visited[r]:
                visited[r] = False
                scc[r] = r
            while len(stack) > 0:
                u = stack[-1]
                done = True
                if transposed[u][0] is not None:
                    for v in transposed[u]:
                        if visited[v]:
                            done = False
                            visited[v] = False
                            stack.append(v)
                            scc[v] = r
                            break
                if done:
                    stack.pop()

        return scc

    # Task 6 - this i've taken from my HW5 submission.
    def get_adj_matrix(self, data=None, directed=None):
        if data is None:
            data = self.G
        if directed is None:
            directed = False

        data = np.array(data)
        #  get the node list
        nodes = np.unique(data)
        n = len(nodes)
        # create a dict
        node_dict = {n: i for i, n in enumerate(nodes)}

        # inverted to vector
        numdata = np.vectorize(node_dict.get)(data)
        am = np.zeros((n, n),)
        for j, i in numdata:
            am[j, i] = 1
            if not directed:
                am[i, j] = 1

        return am.astype(int)

    # Task 6
    def get_number_paths(self, adj_matrix, source, target, k):
        # give up if K is exhaused (zero or negative.)
        if (k == 0 and source == target):
            return 1
        if (k <= 0):
            return 0

        n = len(adj_matrix)
        steps = 0
        # traverse the adj matrix
        for i in range(n):
            if (adj_matrix[source][i] == 1):  # have a connection.
                # deduct step and recursive call; add to current steps.
                steps += self.get_number_paths(adj_matrix, i, target, k - 1)

        return steps


class test_one(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_steps(self):
        arr = [[0, 1], [1, 0], [1, 2], [2, 0], [2, 3], [2, 4], [3, 4], [4, 5], [5, 6], [6, 4], [7, 6]]
        s = connected_helper(G=arr)
        s.max_id = 7
        adj = s.get_adj_matrix(directed=True)

        act = s.get_number_paths(adj, 0, 1, 1)
        self.assertEqual(1, act, 'path is 1')

        act = s.get_number_paths(adj, 3, 4, 1)
        self.assertEqual(1, act, 'path is 1')

        act = s.get_number_paths(adj, 2, 4, 2)
        self.assertEqual(1, act, 'path is 1')

        act = s.get_number_paths(adj, 4, 5, 3)
        self.assertEqual(0, act, 'path is 1')

    def test_steps_two(self):
        arr = [[0, 1], [0, 3], [0, 2], [1, 3], [2, 3]]
        s = connected_helper(G=arr)
        s.max_id = 3
        adj = s.get_adj_matrix(directed=True)
        act = s.get_number_paths(adj, 0, 3, 2)
        self.assertEqual(2, act, 'path is 1')

    def test_adj_matrix(self):
        arr = [[0, 1], [1, 0], [1, 2], [2, 0], [2, 3], [2, 4], [3, 4], [4, 5], [5, 6], [6, 4], [7, 6]]
        s = connected_helper(G=arr)
        s.max_id = 7

        act = s.get_adj_matrix(directed=True)
        self.assertIsNotNone(act)

    def test_dfs_one(self):
        # arr = [[1, 2], [2, 3], [2, 5], [3, 4], [4, 6], [5, 1], [6, 3]]
        arr = [[0, 1], [1, 0], [1, 2], [2, 0], [2, 3], [2, 4], [3, 4], [4, 5], [5, 6], [6, 4], [7, 6]]
        #  cn_exp = [[1], [0, 2], [0, 3, 4], [4], [5], [6], [4], [6]]
        s = connected_helper(G=arr)
        s.max_id = 7

        act = s.get_scc(arr)
        exp = [0, 0, 0, 3, 4, 4, 4, 7]
        self.assertIsNotNone(act)
        self.assertListEqual(act, exp, 'alg done...')

    def test_reverse(self):
        arr = [['0', '2'], ['0', '3'], ['1', '1']]
        exp = [['2', '0'], ['3', '0'], ['1', '1']]
        s = connected_helper(G=arr)
        s.max_id = 3
        act = s.get_reversed_graph()
        self.assertListEqual(exp, act, 'reverse to orig ok')

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


s_fb = connected_helper()
edges_facebook = s_fb.import_data('./data/facebook_combined.txt', skip_header=False, sep=' ', cols=2)
print(len(edges_facebook))  # result is 88234

fb_100 = s_fb.node_top(edges_facebook)

s_fb.get_connected_nodes()[2]

index, con_nodes = s_fb.get_largest_node_degree()
print('index ID of largest FB: {} with {} total nodes'.format(index, len(con_nodes)))

# %%

rv = s_fb.get_scc()

for i, v in enumerate(rv):
    network = []
    max_print = 10
    ic = 0
    if v == 329:
        network.append([i,v])
        if ic < max_print:
            ic += 1
            print('ID: {} is part of SCC: {}'.format(i,v))
            print(ic)

    

# %%


# %%
