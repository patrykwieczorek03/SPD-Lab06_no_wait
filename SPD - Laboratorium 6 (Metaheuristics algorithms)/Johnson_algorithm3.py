from Johnson_algorithm import Johnson_algorithm

import copy

class Johnson_algorithm3 (Johnson_algorithm) : 
    def __init__ (self, seed, n, m):
        super().__init__(seed, n, m)

        self.P_virtual = []
        self.johnson2 = Johnson_algorithm(seed, self.n, 2)

        for a in range(0, n):
            a = [None] * 2
            self.P_virtual.append(a)

        for j in range(0,n):
            self.P_virtual[j][0] = copy.deepcopy(self.P_Copy[j][0])
            self.P_virtual[j][1] = copy.deepcopy(self.P_Copy[j][self.m-1])
        self.Johnson3()

    def __str__(self):
        str1 = "===================================================================\n"
        return str1 + " Pi=" + str(self.Pi) + "\n" + str1 + "\n P=" + str(self.P) + "\n" + str1 + "\n S=" + str(self.S) + "\n" + str1 + "\n C=" + str(self.C) + "\n" + str1 + str(self.UB)

    def Johnson3(self):
        self.johnson2.P = copy.deepcopy(self.P_virtual)
        self.johnson2.P_Copy = copy.deepcopy(self.P_virtual)
        self.johnson2.Johnson()
        self.Pi = self.johnson2.Pi
        self.CalculateCmax()
        self.CalculateSmax()
        self.UB = copy.deepcopy(self.C[self.n-1][self.m-1])
