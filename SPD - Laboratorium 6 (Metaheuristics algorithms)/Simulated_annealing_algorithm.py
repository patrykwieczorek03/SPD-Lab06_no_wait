from Natural_permutation import Natural_permutation
from NEH_Algorithm import NEH_Algorithm 
import random
import copy
import math

class Simulated_annealing_algorithm(Natural_permutation):
    def __init__ (self, seed, n, m):
        super().__init__(seed, n, m)

        #Algorytm neh jako start
        #neh = NEH_Algorithm(seed, n, m)
        #neh.DoNEH()
        #self.Pi  = list(neh.Pi)
        #self.Pi_star  = list(neh.Pi)
        #self.T = neh.UB
        #self.Tend = 0.01 * neh.UB
        #Permutacja naturalna jako start
        self.Pi_star = list(self.Pi)
        self.T = self.UB
        self.Tend = 0.1 * self.UB
        self.Pi_new=[]  

        self.alpha = 0.99
        self.era = 100

    def SimulatedAnnealing(self):
        while(self.T > self.Tend):
            for k in range(0,self.era):
                i = random.randint(0, self.n-1)
                j = random.randint(0, self.n-1)
                self.Pi_new = list(self.Move(i, j))
                if self.CalculateCustomCmax(self.Pi_new) > self.CalculateCustomCmax(self.Pi):
                    self.r = random.random()
                    if r >= math.exp((self.CalculateCustomCmax(self.Pi) - self.CalculateCustomCmax(self.Pi_new))/T):
                        self.Pi_new=copy.deepcopy(self.Pi)
                self.Pi = list(self.Pi_new)
                if self.CalculateCustomCmax(self.Pi) < self.CalculateCustomCmax(self.Pi_star):
                    self.Pi_star = list(self.Pi_new)
            self.ReduceTemperature()
        self.Pi = list(self.Pi_star)
        self.CalculateCmax()
        self.CalculateSmax()
        self.UB = self.C[self.n-1][self.m-1]

    def ReduceTemperature(self):
        self.T = copy.deepcopy(self.T*self.alpha)

    def Move(self, i, j):
        a = random.randint(1, 4)
        if a == 1:
            x = self.Pi[i]
            self.Pi[i] = self.Pi[j]
            self.Pi[j] = x
        elif a == 2:
            x = self.Pi[i]
            del self.Pi[i]
            self.Pi.insert(j,x)
        elif a == 3:
            tmp = []
            tmp_index = 0
            if i < j:
                tmp_index = i
                while i < j:
                    tmp.append(self.Pi[i])
                    i = i + 1
            else:
                tmp_index = j
                while j < i:
                    tmp.append(self.Pi[j])
                    j = j + 1
            tmp.reverse()
            b = 0
            while tmp_index < i:
                self.Pi[tmp_index] = tmp[b]
                b = b + 1
                tmp_index = tmp_index +1
        elif a == 4:
            x = self.Pi[i]
            if i < (self.n - 1):
                self.Pi[i] = self.Pi[i+1]
                self.Pi[i+1] = x
            else:
                self.Pi[i] = self.Pi[i-1]
                self.Pi[i-1] = x
        return self.Pi

    def __str__(self):
        str1 = "===================================================================\n"
        return str1 + " Pi=" + str(self.Pi) + "\n" + str1 + "\n P=" + str(self.P) + "\n" + str1 + "\n S=" + str(self.S) + "\n" + str1 + "\n C=" + str(self.C) + "\n" + str1 + str(self.UB)