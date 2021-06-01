from Natural_permutation import Natural_permutation
import copy

class Johnson_algorithm (Natural_permutation) : 
    def __init__ (self, seed, n, m):
        super().__init__(seed, n, m)
        #Początek permutacji
        self.l = 0
        #Koniec permutacji
        self.k = len(self.P) - 1

    def __str__(self):
        str1 = "===================================================================\n"
        return str1 + " Pi=" + str(self.Pi) + "\n" + str1 + "\n P=" + str(self.P) + "\n" + str1 + "\n S=" + str(self.S) + "\n" + str1 + "\n C=" + str(self.C) + "\n" + str1 + str(self.UB)

    def FindMinimum(self):
        min_value = self.P_Copy[0][0]
        j_star = 0
        n = 0
        for j in self.P_Copy:
            for i in j:
                if min_value > i:
                    min_value = i
                    j_star = n
            n = n + 1
        #j_star jako indeks
        return j_star
         
    def Johnson(self):
        while len(self.P_Copy) > 0:
            # wywołanie
            j_star = self.FindMinimum()
            if self.P_Copy[j_star][0] < self.P_Copy[j_star][1]:
                self.Pi[self.l] = self.Nr_Copy[j_star]
                self.l = self.l + 1
            else:
                self.Pi[self.k] = self.Nr_Copy[j_star]
                self.k = self.k - 1
            del self.P_Copy[j_star]
            del self.Nr_Copy[j_star]
        self.CalculateCmax()
        self.CalculateSmax()
        self.UB = copy.deepcopy(self.C[self.n-1][self.m-1])
        return self.Pi



    


