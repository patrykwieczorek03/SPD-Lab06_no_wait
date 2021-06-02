from Generator import RandomNumberGenerator
from Natural_permutation import Natural_permutation
from Natural_permutation_no_wait import Natural_permutation_no_wait
from Johnson_algorithm import Johnson_algorithm
from Johnson_algorithm3 import Johnson_algorithm3
from NEH_Algorithm import NEH_Algorithm 
from Simulated_annealing_algorithm import Simulated_annealing_algorithm
from Tabu_search_algorithm import Tabu_search_algorithm
from Tabu_search_no_wait_algorithm import Tabu_search_no_wait_algorithm
import random

seed = 78
tasks = 3
machines = 3

str1 = "===================================================================\n"
#print (str1 + "NATURAL PERMUTATION")
#natural_permutation = Natural_permutation(seed, tasks, machines)
#print(natural_permutation)
#print(natural_permutation.UB)

#print (str1 + "JOHNSON ALGORITHM")
#johnson3 = Johnson_algorithm3(seed, tasks, machines)
#print(johnson3)

#print (str1 + "NEH ALGORITHM")
#neh = NEH_Algorithm(seed, tasks, machines)
#neh.DoNEH()
#print(neh)
#print(neh.UB)

#print (str1 + "NEH PLUS 4 ALGORITHM")
#neh = NEH_Algorithm(seed, tasks, machines)
#neh.DoNEHPlus4()
#print(neh)

#print (str1 + "NEH PLUS 1 ALGORITHM")
#neh = NEH_Algorithm(seed, tasks, machines)
#neh.DoNEHPlus1()
#print(neh)

#print (str1 + "SIMULATED ANNEALING")
#sa = Simulated_annealing_algorithm(seed, tasks, machines)
#sa.SimulatedAnnealing()
#print(sa)
#print(sa.UB)

#print (str1 + "TABU SEARCH")
#tb = Tabu_search_algorithm(seed, tasks, machines)
#tb.TabuSearch()
#print(tb)
#print(tb.UB)

#print (str1 + "PORÓWNANIA")
#print("SIMULATED ANNEALING: " + str (round(((sa.UB-neh.UB)* 100.0/neh.UB),2)) + "%")
#print("TABU SEARCH: " + str (round(((tb.UB-neh.UB)* 100.0/neh.UB),2 )) + "%")

#############################################################

print (str1 + "NATURAL PERMUTATION")
natural_permutation = Natural_permutation_no_wait(seed, tasks, machines)
print(natural_permutation)
#print(natural_permutation.UB)

print (str1 + "TABU SEARCH")
tbnw = Tabu_search_no_wait_algorithm(seed, tasks, machines)
tbnw.TabuSearch()
print(tbnw)
#print(tbnw.UB)

#############################################################