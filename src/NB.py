import numpy as np
import math
import helpers import sample_std, pnorm

class NB:
    def __init__(self):
        self.n_attrs = None

        self.p_yes = None
        self.p_no = None

        self.means_yes = None
        self.stds_yes = None
        self.means_no = None
        self.stds_no = None

    def train(self, data):

        n_rows = len(data)
        self.n_attrs = len(data[0]) - 1

        n_yes = 0
        n_no = 0

        sums_yes = np.zeros(self.n_attrs)
        sums_squared_yes = np.zeros(self.n_attrs)
        sums_no = np.zeros(self.n_attrs)
        sums_squared_no = np.zeros(self.n_attrs)

        for row in data:
            if row[-1] == 'yes\n':
                n_yes += 1
                for i in range(self.n_attrs):
                    sums_yes[i] += float(row[i])
                    sums_squared_yes[i] += float(row[i]) ** 2
            elif row[-1] == 'no\n':
                n_no += 1
                for i in range(self.n_attrs):
                    sums_no[i] += float(row[i])
                    sums_squared_no[i] += float(row[i]) ** 2

        self.p_yes = n_yes / len(data)
        self.p_no = n_no / len(data)

        self.means_yes = sums_yes / n_rows
        self.stds_yes = sample_std(sums_squared_yes, self.means_yes, n_rows)
        self.means_no = sums_no / n_rows
        self.stds_no = sample_std(sums_squared_no, self.means_no, n_rows)

    def test(self, data):

        for row in data:
            p_yes_g_row = 1
            p_no_g_row = 1

            for i in range(self.n_attrs):
                p_yes_g_row *= pnorm(float(row[i]), self.means_yes[i], self.stds_yes[i])
                p_no_g_row *= pnorm(float(row[i]), self.means_no[i], self.stds_no[i])
            p_yes_g_row *= self.p_yes
            p_no_g_row *= self.p_no

            if p_yes_g_row >= p_no_g_row:
                print('yes')
            else:
                print('no')
