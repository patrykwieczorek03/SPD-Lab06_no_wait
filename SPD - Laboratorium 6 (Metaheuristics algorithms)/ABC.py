from Natural_permutation import Natural_permutation
import random
import copy
import math

class ABC(Natural_permutation):
    def __init__ (self, seed, n, m):
        super().__init__(seed, n, m)

        self.FoodSource = 100
        self.D = self.n
        #LB
        #UB
        self.max.iteration = 100
        self.N = self.FoodSource/2
        self.limit = self.N * self.D
        self.trial = []
        for i in range(0, self.N):
            self.trial.append(i)



    def __str__(self):
        str1 = "===================================================================\n"
        return str1 + " Pi=" + str(self.Pi) + "\n" + str1 + "\n P=" + str(self.P) + "\n" + str1 + "\n S=" + str(self.S) + "\n" + str1 + "\n C=" + str(self.C) + "\n" + str1 + str(self.UB)