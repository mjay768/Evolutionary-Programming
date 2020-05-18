
def sort(generation,fitness_values):
    temp = []
    temp1 = 0
    #if(type == "ascending"):
    i = 0;
    while i < (len(fitness_values)):
        j = 0
        while j < (len(fitness_values)-1):
            if fitness_values[i] < fitness_values[j]:
                temp = generation[i]
                generation[i] = generation[j]
                generation[j] = temp
            j += 1
        i += 1
    i = 0
    while i < (len(fitness_values)):
        j = 0
        while j < (len(fitness_values)-1):
            if fitness_values[i] < fitness_values[j]:
                temp = fitness_values[i]
                fitness_values[i] = fitness_values[j]
                fitness_values[j] = temp
            j += 1
        i += 1
    return generation,fitness_values