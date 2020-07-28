# %%
def kosaraju(G):

    # postorder DFS on G to transpose the graph and push root vertices to L
    N = len(G)
    T, L, U = [[] for _ in range(N)], [], [False] * N
    for u in range(N):
        if not U[u]:
            U[u], S = True, [u]
            while S:
                u, done = S[-1], True
                for v in G[u]:
                    T[v].append(u)
                    if not U[v]:
                        U[v], done = True, False
                        S.append(v)
                        break
                if done:
                    S.pop()
                    L.append(u)

    # postorder DFS on T to pop root vertices from L and mark SCCs
    C = [None] * N
    while L:
        r = L.pop()
        S = [r]
        if U[r]:
            U[r], C[r] = False, r
        while S:
            u, done = S[-1], True
            for v in T[u]:
                if U[v]:
                    U[v] = done = False
                    S.append(v)
                    C[v] = r
                    break
            if done:
                S.pop()

    return C


arr = [[1, 2], [2, 3], [2, 5], [3, 4], [4, 6], [5, 1], [6, 3]]

arr = [[1], [0, 2], [0, 3, 4], [4], [5], [6], [4], [6]]
rv = kosaraju(arr)

rv


# %%
