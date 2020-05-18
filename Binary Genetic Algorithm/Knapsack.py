import Fitness
import Selection
import Crossover
import Mutate
import numpy as np

capacity = 90

def calc_fitness(W,V,population,pop_size):
    ks_fitnesses = np.empty(len(population))
    sum1=0
    sum2=0
    for individual in range(len(population)):
        sum1 = 0
        sum2 = 0
        for i in range(len(population[individual])):
            #print(i)
            sum1 += (population[individual])[i] * V[i]
            sum2 += (population[individual])[i] * W[i]
        #print("{0} {1}".format(sum1,sum2))
        if sum2 <= capacity:
            ks_fitnesses[individual] = sum1
        else:
            ks_fitnesses[individual] = 0
    #print(W)
   # print(ks_fitnesses)
    #print(sum1)
    #print(sum2)
    return ks_fitnesses