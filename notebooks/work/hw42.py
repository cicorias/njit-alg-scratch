

def sum_target_weights(wg):
    # build a zero start incident matrix
    incident_matrix = [[0 for v in range(len(G))] for s in range(
        len(G))]  # [[0 for v in s] for s in wg]

    for i, r in enumerate(wg):
        for c in r:
            incident_matrix[c[1]][i] += c[2]  # incident_matrix[i][c[1]] + c[2]

    rv = [0] * len(wg)
    for i in range(len(incident_matrix)):
        for j in range(len(incident_matrix[i])):
            # print(incident_matrix[i][j])
            rv[j] += incident_matrix[i][j]

    return rv  # incident_matrix

    
def sum_target_weights_using_dict(wg):
    targets = dict()

    for s in wg:
        for v in s:
            t = v[1]
            w = v[2]
            if t in targets:
                targets[t] += w
            else:
                targets[t] = w

    return targets



#
#


G = [[(0, 1, 1), (0, 2, 5), (0, 3, 11), (0, 4, 8)],
     [(1, 0, 1), (1, 2, 2), (1, 3, 5), (1, 4, 9)],
     [(2, 0, 5), (2, 1, 2), (2, 3, 1), (2, 4, 6)],
     [(3, 0, 11), (3, 1, 5), (3, 2, 1), (3, 4, 8)],
     [(4, 0, 8), (4, 1, 9), (4, 2, 6), (4, 3, 8)]]


print('using dict: {}'.format(sorted(sum_target_weights_using_dict(G).items())))
print('no dict: {}'.format(sum_target_weights(G)))


