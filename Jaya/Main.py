import random
import numpy as np

class JayaAlgorithm():

    best = None
    worst = None
    bestPosition = None
    worstPosition = None
    def initialize_population(self,pop_size,lowerbound,upperbound,vector_length):
        population = []
        for i in range(pop_size):
            temp = np.random.randint(lowerbound,upperbound,vector_length,np.int64)
            population.append(temp)
        population = np.asarray(population)
        return population
    def calc_fitness(self,population):
        fitness = np.empty(population.shape[0])
        sum_of_all = 0
        for individual in population:
            sum_of_all += np.sum(individual)
        for individual in range(population.shape[0]):
            fitness[individual] = np.sum(population[individual])/sum_of_all
        return fitness
    def calc_ind_fitness(self,individual,population):
        sum_of_all = 0
        for individual in population:
         sum_of_all += np.sum(individual)
        fitness= np.sum(individual)/sum_of_all
        return fitness

    def best(self,population,fitness):
        bestPosition = (np.argmax(fitness))
        best = population[np.argmax(fitness)]
        return (best,bestPosition)

    def worst(self,population, fitness):
        worstPosition = np.argmin(fitness)
        worst = population[np.argmin(fitness)]
        return worst,worstPosition
    def old_jaya_pop_update(self,population,max_gens,best,worst,rand_1,rand_2):
        for gen in range(max_gens):
            for individual in range(population.shape[0]):
                new_individual = population[individual] + rand_1*(best - abs(population[individual])) - rand_2*(worst - abs(population[individual]))
                if self.calc_ind_fitness(new_individual,population) >= self.calc_ind_fitness(population[individual],population):
                    population[individual] = new_individual
        return population

    def new_jaya_pop_update(self,population,fitness,max_gens,rand_1,rand_2):
        self.best,bp = self.best(population,fitness)
        self.worst,wp = self.worst(population,fitness)
        for gen in range(max_gens):
            for individual in range(population.shape[0]):
                new_individual = population[individual] + rand_1*(self.best - abs(population[individual])) - rand_2*(self.worst - abs(population[individual]))
                if self.calc_ind_fitness(new_individual,population) >= self.calc_ind_fitness(population[individual],population):
                    population[individual] = new_individual
                    self.best, bp = self.best(population, fitness)
                    self.worst, wp = self.worst(population, fitness)

        return population

    def swap(self,population,individual,worst):
        temp = population
        population[len(population)-1] = worst

    def old_jaya(self):
        max_runs = 30
        best_of_run_fitnesses = []
        avg_best_of_run_fitnesses = []
        solution_vectors = []
        std_best_of_run_fitnesses = []
        pop_size = 5

        #fitness =self.calc_fitness(population)
        # This step is to get the best after
        for r in range(max_runs):
            population = self.initialize_population(pop_size, 5, 10, 15)
            #print(population)
            fitness = self.calc_fitness(population)
            rand_1 = (float("{0:.2f}".format(random.uniform(0, 1),6)))
            rand_2 = (float("{0:.2f}".format(random.uniform(0, 1),6)))
            best = self.best(population,fitness)
            worst = self.worst(population,fitness)
            #print("Best and worst from main():\n{0}\n{1}\n".format(bw[0],bw[1]))
            population = self.old_jaya_pop_update(population,10,best[0],worst[0],rand_1,rand_1)
            fitness = self.calc_fitness(population)
            best_of_run_fitnesses.append(fitness)
            best = self.best(population, fitness)
            solution_vectors.append(best[0])
            #print(np.round(fitness,3))
            avg_best_of_run_fitnesses.append(np.round(np.average(best_of_run_fitnesses),3))
            std_best_of_run_fitnesses.append(np.std(fitness))
        print("For {} runs:".format(max_runs))
        print("Best of run solutions:\n{}\n".format(np.asarray(solution_vectors)))
        print("Best of run Fitnesses:\n{}\n".format(np.asarray(best_of_run_fitnesses)))
        print("Avg of Best of run fitnesses:\n{}\n".format(np.round(avg_best_of_run_fitnesses,3)))
        print("Standard Deviation from fitnesses:\n{}\n------------------------------------------------".format(np.round(std_best_of_run_fitnesses,3)))

    def new_jaya(self):
        max_runs = 30
        pop_size = 5
        best_of_run_fitnesses = []
        avg_best_of_run_fitnesses = []
        solution_vectors = []
        std_best_of_run_fitnesses = []
        population = self.initialize_population(pop_size, 5, 40, 15)
        fitness = self.calc_fitness(population)
        worst, wp = self.worst(population,fitness)
        temp = population[pop_size-1]
        population[pop_size-1] = worst
        population[wp] = temp
        for r in range(max_runs):

            # print(population)
            fitness = self.calc_fitness(population)
            rand_1 = (float("{0:.2f}".format(random.uniform(0, 1), 6)))
            rand_2 = (float("{0:.2f}".format(random.uniform(0, 1), 6)))
            self.best, self.worst,bp,wp = self.best_and_worst(population, fitness)
            # print("Best and worst from main():\n{0}\n{1}\n".format(bw[0],bw[1]))
            population = self.new_jaya_pop_update(population, 20, rand_1, rand_1)
            fitness = self.calc_fitness(population)
            new_bw = self.best_and_worst(population, fitness)
            best_of_run_fitnesses.append(fitness)
            solution_vectors.append(new_bw[0])
            avg = np.average(best_of_run_fitnesses)
            # print(np.round(fitness,3))
            avg_best_of_run_fitnesses.append(np.average(best_of_run_fitnesses))
            std_best_of_run_fitnesses.append(np.std(fitness))

        print("For {} runs:".format(max_runs))
        print("Best of run solutions:\n{}\n".format(np.asarray(solution_vectors)))
        print("Best of run Fitnesses:\n{}\n".format(np.asarray(best_of_run_fitnesses)))
        print("Avg of Best of run fitnesses:\n{}\n".format(avg_best_of_run_fitnesses))
        print("Standard Deviation from fitnesses:\n{}\n------------------------------------------------".format(np.round(std_best_of_run_fitnesses, 3)))


JA = JayaAlgorithm()
JA.old_jaya()