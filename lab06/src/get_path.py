def get_path(self, ant_number):
    visited = set()
    path = []
    current_node = ant_number
    visited.add(current_node)
    path.append(current_node)
    length = 0
    while len(visited) < self.n_nodes:
        next_node = self.choose_next_node(current_node, visited)
        path.append(next_node)
        length += self.graph[current_node][next_node]
        visited.add(next_node)
        current_node = next_node
    length += self.graph[path[-1]][path[0]]
    path.append(path[0])
    return path, length