import numpy as np

class Topsis():
    ev_matrix = np.array([])
    wei_nomr = np.array([])
    dec_norm = np.array([])
    M = 0   #liczba wierszy
    N = 0   #liczba kolumn

    def __init__(self, ev_matrix, weight, criteria):
        self.ev_matrix = np.array(ev_matrix, dtype= 'float')
        self.row_size = len(self.ev_matrix)
        self.column_size = len(self.ev_matrix[0])

        self.weight = np.array(weight, dtype='float')
        self.weight = self.weight/sum(self.weight)
        self.criteria = np.array(criteria, dtype='float')

    def calc(self):
        self.norm_decision = np.copy(self.ev_matrix)
        sqrd_sum = np.zeros(self.column_size)
        for i in range(self.row_size):
            for j in range(self.column_size):
                sqrd_sum[j] += self.ev_matrix[i, j]**2
        for i in range(self.row_size):
            for j in range(self.column_size):
                self.norm_decision[i, j] = self.ev_matrix[i, j]/(sqrd_sum[j]**0.5)

        self.weight_normalized = np.copy(self.norm_decision)
        for i in range(self.row_size):
            for j in range(self.column_size):
                self.weight_normalized[i, j] *= self.weight[j]

        self.worst_alter = np.zeros(self.column_size)
        self.best_alter = np.zeros(self.column_size)
        for i in range(self.column_size):
            if self.criteria[i]:
                self.worst_alter[i] = min(self.weight_normalized[:, i])
                self.best_alter[i] = max(self.weight_normalized[:, i])
            else:
                self.worst_alter[i] = max(self.weight_normalized[:, i])
                self.best_alter[i] = min(self.weight_normalized[:, i])

        self.worst_dist = np.zeros(self.row_size)
        self.best_dist = np.zeros(self.row_size)

        self.worst_dist_mat = np.copy(self.weight_normalized)
        self.best_dist_mat = np.copy(self.weight_normalized)

        for i in range(self.row_size):
            for j in range(self.column_size):
                self.worst_dist_mat[i][j] = (self.weight_normalized[i][j] - self.worst_alter[j])**2
                self.best_dist_mat[i][j] = (self.weight_normalized[i] [j] - self.best_alter[j])**2

                self.worst_dist[i] += self.worst_dist_mat[i][j]
                self.best_dist[i] += self.best_dist_mat[i][j]

        for i in range(self.row_size):
            self.worst_dist[i] = self.worst_dist[i]**0.5
            self.best_dist[i] = self.best_dist[i]**0.5

        np.seterr(all= 'ignore')
        self.worst_simi = np.zeros(self.row_size)
        self.best_simi = np.zeros(self.row_size)

        for i in range(self.row_size):
            self.worst_simi[i] = self.worst_dist[i] / \
                (self.worst_dist[i]+self.best_dist[i])
            self.best_simi[i] = self.best_dist[i] / \
                (self.worst_dist[i]+self.best_dist[i])

    def ranking(self, data):
        return [i+1 for i in data.argsort()]

    def rank_to_worst_similarity(self):
        return self.ranking(self.worst_simi)

    def rank_to_best_similarity(self):
        return self.ranking(self.best_simi)