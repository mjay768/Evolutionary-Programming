import random
import numpy as np
import Fitness as fit
import Selection as select
import Crossover
import Mutate
import Analysis as analyze
import Sort
import Knapsack

class BinaryGeneticAlgorithm():

    exec_start = 0
    population = []
    generations = 3
    MAX_RUNS = 1
    pm = 0.1
    pc = 0.8
    population_size = 5
    all_run_fitness = []
    best_of_runs = []
    best_individuals = []
    standard_deviations = []
    len_of_ind = 15

    ### Attributes for Knapsack Problem

    ks_fitness_values = []

    test_pop = [[0,0,1,1,0,1],[0,0,0,1,1,1],[0,1,0,1,1,0],[0,1,1,0,0,1],[0,0,1,1,1,1]]
    def initKnapSackVals(self):
        ks_weights = []
        ks_values = []
        for i in range(self.len_of_ind):
            ks_weights += [random.randint(40,60)]
            ks_values += [random.randint(1,30)]
        return ks_weights,ks_values
        #Knapsack.calc_fitness(self.ks_weights,self.ks_values,self.test_pop,self.population_size)

    def createPopulation(self,pop_size,bit_length):
        return [self.createIndividual(bit_length) for x in range(pop_size)]

    def createIndividual(self,length):
        return [random.randint(0,1) for x in range(length)]

    def mutation(self,generation,pm):
        mutated_gen = []
        for gen in range(len(generation)):
            mutated_gen += [Mutate.mutate(generation[gen],pm)]
        return mutated_gen

    def main(self,option):
        overall_bestfit = []
        print("Please enter the  maximum number of runs:")
        maxruns = int(input())
        print("Please enter desired number of generations: ")
        gens = int(input())
        print("Enter Population size")
        self.population_size = int(input())
        capacity = 30
        run_fitnesses = []
        best_ind = []
        ks_run_values = []
        ks_run_weights = []
        ks_run_fitness = []
        for run in range(int(maxruns)):
            # print("Run Number %i" % run)
            generation = self.createPopulation(self.population_size, self.len_of_ind)
            #print(generation)
            run_fitnesses.clear()
            ks_weights, ks_values = self.initKnapSackVals()
            ks_run_weights += [ks_weights]
            ks_run_values += [ks_values]
            ks_final_fitness = []
            for gen in range(int(gens)):
                #print("---------------------------------------------------------------")
                fitness_values = fit.generation_fitness_func(generation)

                # KnapSack part of the problem
                ks_fitness = Knapsack.calc_fitness_dynamic(ks_weights,ks_values,generation,self.population_size,capacity)
                if option == "tournament":
                    generation = select.tournament_select(generation,self.population_size)
                if option == "linear":
                    generation = select.linear_rank_select(generation,fitness_values,self.population_size)
                if option == 'proportionate':
                    generation = select.proportionate_selection(generation,fitness_values,self.population_size)
                generation = Crossover.random_crossover(generation,self.len_of_ind,self.population_size)
                generation = self.mutation(generation,self.pm)
                ks_fitness = Knapsack.calc_fitness_dynamic(ks_weights, ks_values, generation, self.population_size)
                ks_final_fitness = ks_fitness
                #print("Knapsack Fitness Values : \n{0}".format(ks_final_fitness))
            ks_run_fitness += [ks_final_fitness]
        print("-----------------------------------")
        print("Knapsack Capacity is {}".format(capacity))
        print("Weights over {} runs".format(maxruns))
        for i in range(len(ks_run_weights)):
            print(ks_run_weights[i])
        print("Values over {} runs".format(maxruns))
        for i in range(len(ks_run_values)):
            print(ks_run_values[i])
        print("Fitness over {} runs".format(maxruns))
        for i in range(len(ks_run_fitness)):
            print(ks_run_fitness[i])



    def init(self):
        print("Please type in the option")
        print("run - Run the program \nhelp - for available selection methods:\n")
        option = input()
        while option == "help" or option == "Help":
            print("Please enter 'Run' to start the program\nAvailable selection techniques are:\n"
                  "linear - Linear Ranking\n"
                  "tournament - Tournament\n"
                  "proportionate - Proportionate:")
            option = input()
        if option == "run" or option == "Run" :
            print("Please enter the selection technique name:\n")
            option = input()
            self.main(option)



GA = BinaryGeneticAlgorithm()
#GA.main("linear")
GA.initKnapSackVals()
