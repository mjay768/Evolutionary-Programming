import random

def random_crossover(generation,ind_length,pop_size):
    new_generation = []
    p1 = []
    p2 = []
    r = random.randint(0,ind_length-1)
    shoudCross = random.uniform(0.0, 1.0)
    rand_vals = random.sample(range(0,round(pop_size/2)),round((pop_size/2)))
    parent_set1 = generation[:round(pop_size/2)][:]
    parent_set2 = generation[round(pop_size/2):][:]
    if shoudCross < 0.8:
        for x in range(round((pop_size)/2)):
            temp = (parent_set1[x])[r:ind_length-1]
            (parent_set1[x])[r:ind_length-1] = (parent_set2[x])[r:ind_length-1]
            (parent_set2[x])[r:ind_length-1] = temp



    new_generation += parent_set1
    new_generation += parent_set2

    return new_generation

