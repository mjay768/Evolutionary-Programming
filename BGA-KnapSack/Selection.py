import numpy as np
import random
import Fitness as fit
import Sort
fitness = -1

def tournament_select(generation,pop_size):
    new_generation = []
    while pop_size > len(new_generation):
        individuals = []
        for _ in range(2):
            individuals.append(random.choice(generation))
        if(fit.individual_fitness_func(individuals[0]) > fit.individual_fitness_func(individuals[1])):
            new_generation.append(individuals[0])
        else:
            new_generation.append(individuals[1])
    return new_generation

def proportionate_selection(generation,fitness_values,pop_size):
    generation, fitness_values = Sort.sort(generation, fitness_values)
    new_generation= []
    max = 0
    fitness_values = fit.generation_fitness_func(generation)
    for value in fitness_values:
        max += value
    current = 0
    pick = random.uniform(0, max)
    while pop_size > len(new_generation):
        for individual in range(len(generation)):

            fitness = fit.countOnes(generation[individual]) # countOnes function can calculate fitness for an individual
            current += fitness
            if current > pick:
                new_generation.append(generation[individual])
    return new_generation

def linear_rank_select(generation,fitness_values,pop_size):
    new_generation = []
    sorted_gen,sorted_fitness = Sort.sort(generation,fitness_values)
    ranks = []
    selection_prob = []
    for x in range(len(fitness_values)):
        ranks += [x+1]
    sum_of_ranks = np.sum(ranks)
    #print(sum_of_ranks)
    for x in range(len(ranks)):
        selection_prob += [round(ranks[x] / sum_of_ranks,2)]

    max_range = selection_prob[len(selection_prob)-1]
    #print(max_range)
    while pop_size > len(new_generation):
        rand = round(random.uniform(0, max_range), 2)
        for individual in range(len(sorted_gen)):
            for x in range(len(fitness_values)):
                if selection_prob[x] == rand:
                    new_generation += [sorted_gen[individual]]


    #print(rand)
    #print(selection_prob)
    #print(new_generation)
    return new_generation


fitness_vals = [[24, 80, 80, 35, 1], [80, 1, 26, 30, 35], [24, 35, 35, 24, 30], [26, 26, 33, 26, 33], [33, 33, 26, 33, 33], [33, 33, 33, 33, 33], [33, 33, 33, 33, 33], [33, 33, 33, 33, 33], [33, 33, 33, 33, 33], [36, 36, 36, 36, 36]]
linear_rank_select(fitness_vals,fitness_vals,10)