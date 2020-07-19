# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'

# %%
# importing graph data
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

edges_facebook = import_data('./data/facebook_combined.txt', skip_header=False, sep=' ', cols=2)
print(len(edges_facebook))  # result is 88234

# importing GitHub graph data
edges_github = import_data('./data/git_web_ml/musae_git_edges.csv', skip_header=True, sep=',', cols=2)
print(len(edges_github))

# import btc data
edges_btc = import_data('./data/soc-sign-bitcoinotc.csv', skip_header=False, sep=',', cols=3)
print(len(edges_btc))

# %%
a = [[1, 2], [1, 2], [1, 2], [2, 1]]

def node_frequency(G, directed=False):
    '''attempt with numpy'''
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


# %% [markdown]
# The following gives the top 100
# %%
fb_100 = node_top(edges_facebook)
gh_100 = node_top(edges_github)
btc_100 = node_top(edges_btc)

# %%
