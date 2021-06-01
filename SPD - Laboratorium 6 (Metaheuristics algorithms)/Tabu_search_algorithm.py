from Natural_permutation import Natural_permutation
from NEH_Algorithm import NEH_Algorithm 
import random
import copy
import math

class Tabu_search_algorithm(Natural_permutation):
    def __init__ (self, seed, n, m):
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

        self.Cadance = 5
        self.Cbest = self.UB
        self.limit = 100

    def TabuSearch(self):
        for it in range(0, self.limit):
            self.Cbest = self.UB
            for j in range(0, self.n):
                for k in range(j+1, self.n):
                    if self.TabuList[j][k] < it:
                        self.Pi_new = list(self.Move(j,k))
                        if self.CalculateCustomCmax(self.Pi_new) < self.Cbest:
                            self.Cbest = self.CalculateCustomCmax(self.Pi_new)
                            self.j_star = j
                            self.k_star = k
            self.Pi = list(self.Move(self.j_star, self.k_star))
            self.TabuList[self.j_star][self.k_star] = it + self.Cadance
            if self.CalculateCustomCmax(self.Pi) < self.CalculateCustomCmax(self.Pi_star):
                self.Pi_star = list(self.Pi)
        self.Pi = list(self.Pi_star)
        self.CalculateCmax()
        self.CalculateSmax()
        self.UB = self.C[self.n-1][self.m-1]

    def Move(self, i, j):
        Pi = list(self.Pi)
        x = Pi[i]
        del Pi[i]
        Pi.insert(j,x)
        return Pi

    def __str__(self):
        str1 = "===================================================================\n"
        return str1 + " Pi=" + str(self.Pi) + "\n" + str1 + "\n P=" + str(self.P) + "\n" + str1 + "\n S=" + str(self.S) + "\n" + str1 + "\n C=" + str(self.C) + "\n" + str1 + str(self.UB)