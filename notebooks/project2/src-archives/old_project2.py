

def import_data(filename, skip_header = False, sep = ',', cols = 2):
    rv = []
    with open(filename, 'rt') as f:
        for line in f:
            if skip_header:
                skip_header = False
                continue
            rv.append(line.strip().split(sep)[0:cols])
            assert len(rv[len(rv) - 1]) == cols

    return rv


def node_frequency(G, directed=False):
    '''attempt with numpy
    this is NOT used....'''
    import numpy as np
    if not directed:  # undirected
        #  this flips the orig and concatenates it again
        a_all = np.concatenate((G, np.flip(G, axis=1)))
    else:
        a_all = G

    unique, counts = np.unique(np.array(a_all)[:, 1], return_counts=True)
    frequencies = np.asarray((unique, counts)).T

    return frequencies

def node_freq(G, directed=False):
    '''faster implementation'''
    rv = {}
    for r in G:
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

def node_top(G, count=100):
    return sorted(
        node_freq(G),
        key = lambda x: x[1], reverse=True)[0:100]
