# %%
# importing graph data
from project2 import import_data, node_top  # node_freq, node_top

edges_facebook = import_data('./data/facebook_combined.txt', skip_header=False, sep=' ', cols=2)
print(len(edges_facebook))  # result is 88234

# importing GitHub graph data
edges_github = import_data('./data/git_web_ml/musae_git_edges.csv', skip_header=True, sep=',', cols=2)
print(len(edges_github))

# import btc data
edges_btc = import_data('./data/soc-sign-bitcoinotc.csv', skip_header=False, sep=',', cols=3)
print(len(edges_btc))

a = [[1, 2], [1, 2], [1, 2], [2, 1]]

# The following gives the top 100
fb_100 = node_top(edges_facebook)
gh_100 = node_top(edges_github)
btc_100 = node_top(edges_btc)
