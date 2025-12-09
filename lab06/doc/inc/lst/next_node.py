def choose_next_node(self, visited, current_node):
    probabilities = []
    total = 0
    for next_node in range(self.n_nodes):
        if next_node not in visited:
            pher = self.pher[current_node][next_node] ** self.herd_coef
            visibility = (1 / self.graph[current_node][next_node]) ** self.greed_coef
            value = pher * visibility
            total += value
            probabilities.append((next_node, value))
    if total == 0:
        probabilities = [(node, 1 / len(probabilities)) for node, _ in probabilities]
    else:
        probabilities = [(node, value / total) for node, value in probabilities]
    r = random.random()
    cumulative = 0
    for node, prob in probabilities:
        cumulative += prob
        if r <= cumulative:
            return node
    return probabilities[-1][0]