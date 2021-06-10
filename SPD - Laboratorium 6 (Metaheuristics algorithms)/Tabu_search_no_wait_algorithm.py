from Natural_permutation_no_wait import Natural_permutation_no_wait
import random
import copy
import math

class Tabu_search_no_wait_algorithm(Natural_permutation_no_wait):
    def __init__ (self, seed, n, m, version):
        super().__init__(seed, n, m)
        
        self.Pi_star = list(self.Pi)
        self.T = self.UB
        self.Tend = 0.1 * self.UB
        self.Pi_new=[]  
        self.j_star = 0  
        self.k_star = 0  

        self.TabuList = []
        for i in range(0, self.n):
            a = [0] * self.n
            self.TabuList.append(a)

        self.Cadance = math.floor(math.sqrt(self.n))
        self.Cbest = self.UB
        self.limit = 100
        self.version = version

    def TabuSearch(self):
        for it in range(0, self.limit):
            self.Cbest = 100000
            for j in range(0, self.n):
                for k in range(j+1, self.n):
                    if self.TabuList[j][k] <= it:
                        self.Pi_new = list(self.Move(j,k,self.version))
                        if self.CalculateCustomCmax(self.Pi_new) < self.Cbest:
                            self.Cbest = self.CalculateCustomCmax(self.Pi_new)
                            self.j_star = j
                            self.k_star = k
            self.Pi = list(self.Move(self.j_star, self.k_star,self.version))
            self.TabuList[self.j_star][self.k_star] = it + self.Cadance
            if self.CalculateCustomCmax(self.Pi) < self.CalculateCustomCmax(self.Pi_star):
                self.Pi_star = list(self.Pi)
        self.Pi = list(self.Pi_star)
        self.CalculateCmax(self.Pi)
        self.CalculateSmax()
        self.UB = self.C[self.n-1][self.m-1]

    def Move(self, i, j, version):
        Pi = list(self.Pi)
        if version == 1:
            x = Pi[i]
            Pi[i] = Pi[j]
            Pi[j] = x
        elif version == 2:
            x = Pi[i]
            del Pi[i]
            Pi.insert(j,x)
        elif version == 3:
            tmp = []
            tmp_index = 0
            if i < j:
                tmp_index = i
                while i < j:
                    tmp.append(Pi[i])
                    i = i + 1
            else:
                tmp_index = j
                while j < i:
                    tmp.append(Pi[j])
                    j = j + 1
            tmp.reverse()
            b = 0
            while tmp_index < i:
                Pi[tmp_index] = tmp[b]
                b = b + 1
                tmp_index = tmp_index +1
        elif version == 4:
            x = Pi[i]
            if i < (self.n - 1):
                Pi[i] = Pi[i+1]
                Pi[i+1] = x
            else:
                Pi[i] = Pi[i-1]
                Pi[i-1] = x
        return Pi

    def __str__(self):
        str1 = "===================================================================\n"
        return str1 + " Pi=" + str(self.Pi) + "\n" + str1 + "\n P=" + str(self.P) + "\n" + str1 + "\n S=" + str(self.S) + "\n" + str1 + "\n C=" + str(self.C) + "\n" + str1 + str(self.UB)