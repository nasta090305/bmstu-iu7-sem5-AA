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