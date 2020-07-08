
# DFS Recursive implmenentation
# - adjacency list
# listof lists

input = [[2, 3, 4], [3, 1], [1, 2, 4]]  # ....

visited = [0] * len(input)  # ''  # bit vector


def explore(G, u):
    visited[u] = 1
    previsit(u)

    for k in range(len(G[u])):
        if visited[G[u][k]] == 0:
            explore(G, G[u][k])  # neighbor of u


def previsit(n):
    '''TBD for DFS'''
    pass


def postvisit(n):
    '''TBD for DFS'''
    pass
