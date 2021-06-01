from Natural_permutation import Natural_permutation
import copy

class NEH_Algorithm (Natural_permutation) :
    def __init__ (self, seed, n, m):
        super().__init__(seed, n, m)
        self.PiNEH = []
        self.Pi_copy = []
        self.Pi_star = []
        self.w = []
        self.W = []
        self.k = 0
        self.PartialCmax = 10000
        self.PartialSecondCmax = 10000


    def DoNEH(self):
        for i in range(0, self.n):
            tmp = 0
            for j in range(0, self.m):
                tmp = tmp + self.P[i][j]
            self.w.append(tmp)
            self.W.append(self.Pi[i])
            Sort_w, Sort_W = zip(*[(x,y)for x, y in sorted(zip(self.w, self.W))])
            self.w=list(Sort_w)
            self.W=list(Sort_W)
            self.w.reverse()
            self.W.reverse()
        #a = copy.deepcopy(self.W[1])
        #self.W[1] = self.W[2]
        #self.W[2] = a
        #print(self.w)
        #print(self.W)
    
        while len(self.W) > 0:
            j_star = self.W[0]
            l = 0
            self.PartialCmax = 10000
            while l <= self.k:
                self.Pi_copy.insert(l ,j_star)
                if self.CalculateCustomCmax(self.Pi_copy) < self.PartialCmax:
                    self.PartialCmax = self.CalculateCustomCmax(self.Pi_copy)
                    self.Pi_star = copy.deepcopy(self.Pi_copy)
                self.Pi_copy.remove(j_star)
                l = l + 1
            #print("Best Cmax: " + str(self.PartialCmax))
            #print("Best Pi: " + str(self.Pi_star))
            self.Pi_copy = copy.deepcopy(self.Pi_star)
            del self.W[0]
            self.k = self.k + 1
        self.Pi = list(self.Pi_star)
        self.CalculateCmax()
        self.CalculateSmax()
        self.UB = copy.deepcopy(self.C[self.n-1][self.m-1])
      
    def __str__(self):
        str1 = "===================================================================\n"
        return str1 + " Pi=" + str(self.Pi) + "\n" + str1 + "\n P=" + str(self.P) + "\n" + str1 + "\n S=" + str(self.S) + "\n" + str1 + "\n C=" + str(self.C) + "\n" + str1 + str(self.UB)


    def DoNEHPlus4(self):
        for i in range(0, self.n):
            tmp = 0
            for j in range(0, self.m):
                tmp = tmp + self.P[i][j]
            self.w.append(tmp)
            self.W.append(self.Pi[i])
            Sort_w, Sort_W = zip(*[(x,y)for x, y in sorted(zip(self.w, self.W))])
            self.w=list(Sort_w)
            self.W=list(Sort_W)
            self.w.reverse()
            self.W.reverse()
        #a = copy.deepcopy(self.W[1])
        #self.W[1] = self.W[2]
        #self.W[2] = a
        #print(self.w)
        #print(self.W)
    
        while len(self.W) > 0:
            j_star = self.W[0]
            l = 0
            self.PartialCmax = 10000
            while l <= self.k:
                self.Pi_copy.insert(l, j_star)
                if self.CalculateCustomCmax(self.Pi_copy) < self.PartialCmax:
                    self.PartialCmax = self.CalculateCustomCmax(self.Pi_copy)
                    self.Pi_star = copy.deepcopy(self.Pi_copy)
                self.Pi_copy.remove(j_star)
                l = l + 1
            self.PartialSecondCmax = 10000
            chosenIndex = 0
            for k in range(0, len(self.Pi_star)):
                if self.Pi_star[k] != j_star:
                    item = self.Pi_star[k]
                    del self.Pi_star[k]
                    if self.CalculateCustomCmax(self.Pi_star) < self.PartialSecondCmax:
                        self.PartialSecondCmax = self.CalculateCustomCmax(self.Pi_star)
                        chosenIndex = k
                    self.Pi_star.insert(k, item)
                #print(self.PartialSecondCmax)
            j_star = copy.deepcopy(self.Pi_star[chosenIndex])
            del self.Pi_star[chosenIndex]
            self.Pi_copy = copy.deepcopy(self.Pi_star)
            #del self.Pi_copy[chosenIndex]
            l = 0
            self.PartialCmax = 10000
            while l <= self.k:
                self.Pi_copy.insert(l, j_star)
                if self.CalculateCustomCmax(self.Pi_copy) < self.PartialCmax:
                    self.PartialCmax = self.CalculateCustomCmax(self.Pi_copy)
                    self.Pi_star = copy.deepcopy(self.Pi_copy)
                self.Pi_copy.remove(j_star)
                l = l + 1
            #print("Best Cmax: " + str(self.PartialCmax))
            #print("Best Pi: " + str(self.Pi_star))
            self.Pi_copy = copy.deepcopy(self.Pi_star)
            del self.W[0]
            self.k = self.k + 1
        self.Pi = list(self.Pi_star)
        self.CalculateCmax()
        self.CalculateSmax()
        self.UB = copy.deepcopy(self.C[self.n-1][self.m-1])


    def DoNEHPlus1(self):
        for i in range(0, self.n):
            tmp = 0
            for j in range(0, self.m):
                tmp = tmp + self.P[i][j]
            self.w.append(tmp)
            self.W.append(self.Pi[i])
            Sort_w, Sort_W = zip(*[(x,y)for x, y in sorted(zip(self.w, self.W))])
            self.w=list(Sort_w)
            self.W=list(Sort_W)
            self.w.reverse()
            self.W.reverse()
        #a = copy.deepcopy(self.W[1])
        #self.W[1] = self.W[2]
        #self.W[2] = a
        #print(self.w)
        #print(self.W)
    
        while len(self.W) > 0:
            j_star = self.W[0]
            l = 0
            self.PartialCmax = 10000
            while l <= self.k:
                self.Pi_copy.insert(l, j_star)
                if self.CalculateCustomCmax(self.Pi_copy) < self.PartialCmax:
                    self.PartialCmax = self.CalculateCustomCmax(self.Pi_copy)
                    self.Pi_star = copy.deepcopy(self.Pi_copy)
                self.Pi_copy.remove(j_star)
                l = l + 1
            maxo, maxoindex, maxotask = self.CalculateCritical(copy.deepcopy(self.Pi_star)) 
            j_star = copy.deepcopy(maxotask)
            del self.Pi_star[maxoindex]
            self.Pi_copy = copy.deepcopy(self.Pi_star)
            #del self.Pi_copy[chosenIndex]
            l = 0
            self.PartialCmax = 10000
            while l <= self.k:
                self.Pi_copy.insert(l, j_star)
                if self.CalculateCustomCmax(self.Pi_copy) < self.PartialCmax:
                    self.PartialCmax = self.CalculateCustomCmax(self.Pi_copy)
                    self.Pi_star = copy.deepcopy(self.Pi_copy)
                self.Pi_copy.remove(j_star)
                l = l + 1
            #print("Best Cmax: " + str(self.PartialCmax))
            #print("Best Pi: " + str(self.Pi_star))
            self.Pi_copy = copy.deepcopy(self.Pi_star)
            del self.W[0]
            self.k = self.k + 1
        self.Pi = list(self.Pi_star)
        self.CalculateCmax()
        self.CalculateSmax()
        self.UB = copy.deepcopy(self.C[self.n-1][self.m-1])

    def CalculateCritical(self, Pi):
        n = len(Pi)
        m = self.m
        C = self.CalculatePartialCmax(Pi)
        maxo = 0
        maxoindex = 0
        maxotask = 0
        Cm = C[n-1][m-1]
        result = 0
        while Cm > C[0][0] :
            #if n > 1 and m > 0:    
            result = Cm - self.P[Pi[n-1]-1][m-1]
            if result == C[n-1][m-2]:
                #print(Cm)
                #print("Numer zadania: " + str(Pi[n-1]))
                #print("Numer maszyny: " + str(m))
                #print("Czas trwania operacji: " + str(self.P[Pi[n-1]-1][m-1]))
                #print("\n")
                if self.P[Pi[n-1]-1][m-1] > maxo:
                    maxo = self.P[Pi[n-1]-1][m-1]
                    maxotask = Pi[n-1]
                    maxoindex = n-1
                Cm = result
                m -= 1
            else:
                #print(Cm)
                #print("Numer zadania: " + str(Pi[n-1]))
                #print("Numer maszyny: " + str(m))
                #print("Czas trwania operacji: " + str(self.P[Pi[n-1]-1][m-1]))
                #print("\n")
                if self.P[Pi[n-1]-1][m-1] > maxo:
                    maxo = self.P[Pi[n-1]-1][m-1]
                    maxotask = Pi[n-1]
                    maxoindex = n-1
                n -= 1
                Cm = C[n-1][m-1]
            #if Cm == C[0][0]:
                #print("Numer zadania: " + str(Pi[n-1]))
                #print("Numer maszyny: " + str(m))
                #print("Czas trwania operacji: " + str(self.P[Pi[n-1]-1][m-1]))
                #print("\n")
        return maxo, maxoindex, maxotask
