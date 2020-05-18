import numpy as np

def calc_fitness_static(W,V,population,pop_size,capacity = 30):
    ks_fitnesses = np.empty(len(population))
    sum1=0
    sum2=0
    for individual in range(len(population)):
        sum1 = 0
        sum2 = 0
        for i in range(len(population[individual])):
            sum1 += (population[individual])[i] * V[i]
            sum2 += (population[individual])[i] * W[i]
        if sum2 <= capacity:
            ks_fitnesses[individual] = sum1
        else:
            ks_fitnesses[individual] -= 5

    return ks_fitnesses.astype(int)


def calc_fitness_dynamic(W, V, population, pop_size, capacity=30):
    ks_fitnesses = np.empty(len(population))
    sum1 = 0
    sum2 = 0
    for individual in range(len(population)):
        sum1 = 0
        sum2 = 0
        for i in range(len(population[individual])):
            sum1 += (population[individual])[i] * V[i]
            sum2 += (population[individual])[i] * W[i]
        penalty = 0
        if sum2 <= capacity:
            ks_fitnesses[individual] = sum1
        else:
            sigma = calc_sigma(W,V)
            penalty = calc_penalty(population[individual],W,capacity,sigma)
            ks_fitnesses[individual] -= sum1 - penalty

    return ks_fitnesses.astype(int)


def calc_sigma(W, V):
    result = []
    for i in range(len(V)):
        result += [V[i] / W[i]]
    return max(result)


def calc_penalty(individual, W, C, sigma):
    sum = 0
    for i in range(len(individual)):
        sum = np.sum(individual[i] * W[i] - C)
    # print(sum)
    val = (sigma * sum)
    return val