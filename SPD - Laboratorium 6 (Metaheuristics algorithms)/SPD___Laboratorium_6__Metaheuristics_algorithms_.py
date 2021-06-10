from Generator import RandomNumberGenerator
from Natural_permutation import Natural_permutation
from Natural_permutation_no_wait import Natural_permutation_no_wait
from Johnson_algorithm import Johnson_algorithm
from Johnson_algorithm3 import Johnson_algorithm3
from NEH_Algorithm import NEH_Algorithm 
from NEH_Algorithm_no_wait import NEH_Algorithm_no_wait
from Simulated_annealing_algorithm import Simulated_annealing_algorithm
from Tabu_search_algorithm import Tabu_search_algorithm
from Tabu_search_no_wait_algorithm import Tabu_search_no_wait_algorithm
import random
import matplotlib.pyplot as plt


str1 = "==================================================================="

def test(seed, it, task, version, seedit=False):
    for i in range(1, int(it)):
        if seedit == True:
            machines = 5
            tasks = 25
            seed = i * 125
            np_x.append(seed)
            neh_x.append(seed)
            ts_x.append(seed)
        elif task == False:
            machines = i+1
            tasks = 20
            np_x.append(machines)
            neh_x.append(machines)
            ts_x.append(machines)
        elif task == True:
            machines = 3
            tasks = i
            np_x.append(tasks)
            neh_x.append(tasks)
            ts_x.append(tasks)

        print(str1)
        natural_permutation = Natural_permutation_no_wait(int(seed), tasks, machines)
        print("NATURAL PERMUTATION: " + str(natural_permutation.UB))
        np_y.append(natural_permutation.UB)
        
        neh = NEH_Algorithm_no_wait(int(seed), tasks, machines)
        neh.DoNEH()
        print("NEH ALGORITHM NO WAIT: " + str(neh.UB))
        neh_y.append(neh.UB)

        tbnw = Tabu_search_no_wait_algorithm(int(seed), tasks, machines, version)
        tbnw.TabuSearch()
        print("TABU SEARCH NO WAIT: " + str(tbnw.UB))
        ts_y.append(tbnw.UB)

        print("PORÓWNANIE: " + str(round(((tbnw.UB-neh.UB)* 100.0/neh.UB),2 )) + "%")

def test_ts(seed, it, machines):
    for i in range(1, int(it)):
        np_x.append(i)
        ts_x1.append(i)
        ts_x2.append(i)
        ts_x3.append(i)
        ts_x4.append(i)

        print(str1)
        natural_permutation = Natural_permutation_no_wait(int(seed), i, int(machines))
        print("NATURAL PERMUTATION: " + str(natural_permutation.UB))
        np_y.append(natural_permutation.UB)

        tbnw = Tabu_search_no_wait_algorithm(int(seed), i, machines, 1)
        tbnw.TabuSearch()
        print("TABU SEARCH NO WAIT SWAP: " + str(tbnw.UB))
        ts_y1.append(tbnw.UB)

        tbnw = Tabu_search_no_wait_algorithm(int(seed), i, machines, 2)
        tbnw.TabuSearch()
        print("TABU SEARCH NO WAIT INSERT: " + str(tbnw.UB))
        ts_y2.append(tbnw.UB)

        tbnw = Tabu_search_no_wait_algorithm(int(seed), i, machines, 3)
        tbnw.TabuSearch()
        print("TABU SEARCH NO WAIT TWIST: " + str(tbnw.UB))
        ts_y3.append(tbnw.UB)

        tbnw = Tabu_search_no_wait_algorithm(int(seed), i, machines, 4)
        tbnw.TabuSearch()
        print("TABU SEARCH NO WAIT ADJACENT SWAP: " + str(tbnw.UB))
        ts_y4.append(tbnw.UB)

end = 0
seed = 0
tasks = 0
machines = 0
version = 0
it = 0
np_x = []
np_y = []
neh_x = []
neh_y = []
ts_x = []
ts_y = []
ts_x1 = []
ts_y1 = []
ts_x2 = []
ts_y2 = []
ts_x3 = []
ts_y3 = []
ts_x4 = []
ts_y4 = []
while end == 0:
    print("Wybierz jedną z opcji:")
    print("1. Badanie wpływu ilości zadań na rozwiązanie")
    print("2. Badanie wpływu ilości maszyn na rozwiązanie")
    print("3. Badanie wpływu seeda na rozwiązanie")
    print("4. Badanie wpływu rodzaju tabu search na rozwiązanie")
    print("5. Wyjście z programu")
    chosen = input("Twój wybór:")
    version = 0
    while version == 0 and chosen != '4':
        print("Wybierz wersje tabu search:")
        print("1. Swap")
        print("2. Insert")
        print("3. Twist")
        print("4. Adjacent swap")
        version = int(input("Twój wybór:"))
    if chosen == '1':
        tasks = input("Wprowadz liczbę zadań:")
        seed = input("Wprowadz seeda:")
        test(seed, tasks, True, version)
        plt.xlabel('Tasks', fontsize = 16)
        plt.title('Cmax(Tasks)', fontsize = 16)
    elif chosen == '2':
        machines = input("Wprowadz liczbę maszyn:")
        seed = input("Wprowadz seeda:")
        test(seed, machines, False, version)
        plt.xlabel('Machines', fontsize = 16)
        plt.title('Cmax(Machines)', fontsize = 16)
    elif chosen == '3':
        test(0, 20, True, version, True)
        plt.xlabel('Seed', fontsize = 16)
        plt.title('Cmax(Seed)', fontsize = 16)
    elif chosen == '4':
        tasks = input("Wprowadz liczbę zadań:")
        seed = input("Wprowadz seeda:")
        machines = input("Wprowadz liczbę maszyn:")
        test_ts(int(seed), int(tasks), int(machines))
        plt.xlabel('Tasks', fontsize = 16)
        plt.title('Cmax(Tasks)', fontsize = 16)
    elif chosen == '5':
        end = 1
    
    if end != 1:
        if chosen != '4':
            plt.ylabel('Cmax', fontsize = 16)
            plt.plot(np_x, np_y, 'dodgerblue', label = 'Natural permutation', linewidth = 1)
            plt.plot(neh_x, neh_y, 'green', label = 'Neh', linewidth = 1)
            plt.plot(ts_x, ts_y, 'red', label = 'Tabu Search', linewidth = 1)
        if chosen == '4':
            plt.ylabel('Cmax', fontsize = 16)
            plt.plot(np_x, np_y, 'dodgerblue', label = 'Natural permutation', linewidth = 1)
            plt.plot(ts_x1, ts_y1, 'green', label = 'Tabu Search Swap', linewidth = 1)
            plt.plot(ts_x2, ts_y2, 'red', label = 'Tabu Search Insert', linewidth = 1)
            plt.plot(ts_x3, ts_y3, 'blue', label = 'Tabu Search Twist', linewidth = 1)
            plt.plot(ts_x4, ts_y4, 'yellow', label = 'Tabu Search Adjacent swap', linewidth = 1)

        plt.grid(True)
        plt.legend()
        plt.savefig('Line_plot.jpeg', dpi = 400, quality = 100)
        plt.show()
        plt.clf()
    
        np_x.clear()
        np_y.clear()
        neh_x.clear()
        neh_y.clear()
        ts_x.clear()
        ts_y.clear()
        ts_x1.clear()
        ts_y1.clear()
        ts_x2.clear()
        ts_y2.clear()
        ts_x3.clear()
        ts_y3.clear()
        ts_x4.clear()
        ts_y4.clear()