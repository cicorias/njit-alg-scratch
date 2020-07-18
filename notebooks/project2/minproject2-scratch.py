# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
print('hello')


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

edges = import_data('./data/facebook_combined.txt', skip_header=False, sep=' ', cols=2)
print(len(edges))  # result is 88234


# %%
# importing GitHub graph data
edges_github = import_data('./data/git_web_ml/musae_git_edges.csv', skip_header=True, sep=',', cols=2)
print(len(edges_github))


# %%
# import btc data
edges_btc = import_data('./data/soc-sign-bitcoinotc.csv', skip_header=False, sep=',', cols=3)
print(len(edges_btc))




# %%
