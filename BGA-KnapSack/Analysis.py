import numpy as np

def best_of_run(generation,fitness_values):
    bor = (fitness_values[0])[0]
    gen = []
    for each in range(len(fitness_values)):
        for me in range(len(fitness_values[each])):
            if (fitness_values[each])[me] < bor:

                bor = (fitness_values[each])[me]
                gen = [(generation[me])]

    return bor,gen

def mean(fitness_values):
    number_of_vals = len(fitness_values)
    sum = 0
    for each in fitness_values:
        for me in each:
            sum += me
    avg = sum / number_of_vals
    return avg

def standard_dev(fitness_values):
    print(np.std(fitness_values))
    return np.std(fitness_values)


