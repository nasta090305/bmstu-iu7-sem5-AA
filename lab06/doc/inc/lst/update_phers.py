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