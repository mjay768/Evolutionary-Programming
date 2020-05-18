import random
import numpy as np
import Fitness as fit
import Selection as select
import Crossover
import Mutate
import Analysis as analyze


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
    len_of_ind = 45

    def createPopulation(self,pop_size,bit_length):
        return [self.createIndividual(bit_length) for x in range(pop_size)]

    def createIndividual(self,length):
        return [random.randint(0,1) for x in range(length)]

    def extract_genes(self,population):
        x1 = []
        x2 = []
        x3 = []
        for g in range(len(population)):
            generation = population[g]
            item = []
            item.clear()
            for gene in range(len(generation)):
                item += [generation[gene]]
            x1 += [item[:][:10]]
            x2 += [item[:][10:24]]
            x3 += [item[:][24:44]]
        return x1,x2,x3

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

        run_fitnesses = []
        best_ind = []
        for run in range(int(maxruns)):
           # print("Run Number %i" % run)
            generation = self.createPopulation(self.population_size, self.len_of_ind)
            print(generation)
            run_fitnesses.clear()
            for gen in range(int(gens)):
                print("---------------------------------------------------------------")

                #Genetic Algorithm part
                x1,x2,x3 = self.extract_genes(generation)
                fit_value = fit.calc_fitness_value(x1,x2,x3)
                run_fitnesses.append(fit_value)
                fitness_values = fit.generation_fitness_func(generation)


                if option == "tournament":
                    generation = select.tournament_select(generation,self.population_size)
                if option == "linear":
                    generation = select.linear_rank_select(generation,fitness_values,self.population_size)
                if option == 'proportionate':
                    generation = select.proportionate_selection(generation,fitness_values,self.population_size)
                generation = Crossover.random_crossover(generation,self.len_of_ind,self.population_size)
                generation = self.mutation(generation,self.pm)

            bor,vector = analyze.best_of_run(generation,run_fitnesses)
            self.best_of_runs += [bor]
            self.best_individuals += vector

            print("Best of run is %i" % bor)
            if self.exec_start == 0:
                overall_bestfit = bor
                self.exec_start = 1
            if bor < overall_bestfit:
                overall_bestfit = bor

        print("Best fitness over all runs is %i" % overall_bestfit)
        avg = analyze.mean(run_fitnesses)
        print("Average of all runs is %f" % avg)
        print("Best of run values:")
        print(self.best_of_runs)
        print("Standard deviation from {0} independent runs is {1}".format(maxruns,np.std(self.best_of_runs)))
        print("Best individuals: ")
        for each in range(len(self.best_individuals)):
            print(self.best_individuals[each])

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
GA.main("linear")
#GA.initKnapSackVals()
