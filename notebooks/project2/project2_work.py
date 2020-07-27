# %%
from test_foobar import connected_helper

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
