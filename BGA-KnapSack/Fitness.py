
def calc_fitness_value(x,y,z):
    fitnessvalues = []
    x = generation_fitness_func(x)
    y = generation_fitness_func(y)
    z = generation_fitness_func(z)

    for p in range(len(x)):
        fitnessvalues += [(x[p]*x[p])+(y[p]*y[p])+(z[p]*z[p])]

    return fitnessvalues

    #fitness_value = x*x + y*y + z*z
def generation_fitness_func(generation):
    fitness_values = []
    for gene in range(len(generation)):
        fitness_values += [countOnes(generation[gene])]
    return fitness_values

def individual_fitness_func(individual):
    return [countOnes(individual)]

def countOnes(gene):
    count = 0
    for x in range(len(gene)):
        if(gene[x]) == 1:
            count += 1
    return count

