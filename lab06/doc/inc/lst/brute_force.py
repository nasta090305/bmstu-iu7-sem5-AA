def brute_force_search(graph):
    n = len(graph)
    best_path_length = float('inf')
    best_path = None
    perms = permutations(list(range(n)))
    for perm in perms:
        path_length = 0
        for i in range(n - 1):
            path_length += graph[perm[i]][perm[i + 1]]
        path_length += graph[perm[-1]][perm[0]]
        if path_length < best_path_length:
            best_path_length = path_length
            best_path = perm
    best_path = list(best_path)
    best_path.append(best_path[0])
    return best_path, best_path_length