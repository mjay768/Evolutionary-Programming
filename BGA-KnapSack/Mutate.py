import random

def mutate_old(generation,pm):
    rand = []
    for gen in range(len(generation)):
        rand += [random.randint(0, len(generation))]
        for x in range(len(rand)):
            if random.uniform(0.0,1.0) <= pm:
                for gen in (generation):
                    if gen[rand[x]] == 1:
                        gen[rand[x]] = 0
    return generation

def mutate(generation,pm):
    rand = []
    for _ in range(1):
        rand += [random.randint(0, len(generation) - 1)]
    for x in range(len(rand)):
        shouldMutate = random.uniform(0.0, 1.0)
        if shouldMutate < pm:
            if generation[rand[x]] == 1:
                generation[rand[x]] = 0
            if generation[rand[x]] == 0:
                generation[rand[x]] = 1
    return generation