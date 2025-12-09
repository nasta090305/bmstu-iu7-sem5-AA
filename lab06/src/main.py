import numpy as np
import random


#Вариант: орграф, с элитными, с возвратом в первый город.
class AntsAlg:
    def __init__(self, graph, greed_coef, herd_coef, evap_rate, pher_min, t_max):
        self.graph = graph  # Матрица расстояний
        self.n_ants = len(graph)
        self.t_max = t_max
        self.greed_coef = greed_coef
        self.herd_coef = herd_coef
        self.evap_rate = evap_rate
        self.pher_min = pher_min
        self.pher_sum = (np.sum(self.graph) / 2) / len(graph)
        self.n_nodes = len(graph)
        self.pher = np.full((self.n_nodes, self.n_nodes), self.pher_min)  # Матрица уровня ферамонов

    def calculate(self):
        best_path = None
        best_path_length = float('inf')
        for t in range(self.t_max):
            all_paths = []
            for i in range(self.n_ants):
                path, length = self.get_path(i)
                all_paths.append((path, length))
            for path, length in all_paths:
                if length < best_path_length:
                    best_path_length = length
                    best_path = path
            self.update_phers(all_paths, best_path, best_path_length)
        return best_path, best_path_length

    def get_path(self, ant_number):
        visited = set()
        path = []
        current_node = ant_number
        visited.add(current_node)
        path.append(current_node)
        length = 0
        while len(visited) < self.n_nodes:
            next_node = self.choose_next_node(visited, current_node)
            path.append(next_node)
            length += self.graph[current_node][next_node]
            visited.add(next_node)
            current_node = next_node
        length += self.graph[path[-1]][path[0]]
        path.append(path[0])
        return path, length

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

    def update_phers(self, paths, best_path, best_path_length):
        self.pher *= (1 - self.evap_rate)  # Испарение феромона
        for path, length in paths:
            for i in range(len(path) - 1):
                from_node = path[i]
                to_node = path[i + 1]
                if length > 0:
                    self.pher[from_node][to_node] += self.pher_sum / length
        if best_path is not None:
            for i in range(len(best_path) - 1):
                from_node = best_path[i]
                to_node = best_path[i + 1]
                if best_path_length > 0:
                    self.pher[from_node][to_node] += self.pher_sum / best_path_length

from itertools import permutations

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


graph =  np.array([
        [0, 1, 4, 16],
        [1, 0, 9, 25],
        [4, 9, 0, 36],
        [16, 25, 36, 0]
    ])

ant_colony = AntsAlg(graph, greed_coef=1, herd_coef=0, evap_rate=0.5, pher_min=0.1, t_max=1000)
best_path, best_path_length = ant_colony.calculate()

cycle, path_length = brute_force_search(graph)

print("Матрица расстояний:")
for i in graph:
    for j in i:
        print(j, end=' ')
    print()

print("Результат работы алгоритма полного перебора:")
print("Длина оптимального пути: ", path_length)
print("Путь: ", cycle)

print("Результат работы муравьиного алгоритма:")
print("Длина оптимального пути: ", best_path_length)
print("Путь: ", best_path)

graph = np.array([
        [0, 1, 2, 12, 3],
        [3, 0, 4, 43, 5],
        [5, 6, 0, 24, 1],
        [63, 43, 24, 0, 2],
        [3, 6, 14, 4, 0]
    ])

ant_colony = AntsAlg(graph, greed_coef=1, herd_coef=0, evap_rate=0.5, pher_min=0.1, t_max=1000)
best_path, best_path_length = ant_colony.calculate()

cycle, path_length = brute_force_search(graph)

print("Матрица расстояний:")
for i in graph:
    for j in i:
        print(j, end=' & ')
    print('\\\\')

print("Результат работы алгоритма полного перебора:")
print("Длина оптимального пути: ", path_length)
print("Путь: ", cycle)

print("Результат работы муравьиного алгоритма:")
print("Длина оптимального пути: ", best_path_length)
print("Путь: ", best_path)