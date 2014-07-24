from pyeasyga import pyeasyga

# setup data
data = [(821, 0.8, 118), (1144, 1, 322), (634, 0.7, 166), (701, 0.9, 195),
        (291, 0.9, 100), (1702, 0.8, 142), (1633, 0.7, 100), (1086, 0.6, 145),
        (124, 0.6, 100), (718, 0.9, 208), (976, 0.6, 100), (1438, 0.7, 312),
        (910, 1, 198), (148, 0.7, 171), (1636, 0.9, 117), (237, 0.6, 100),
        (771, 0.9, 329), (604, 0.6, 391), (1078, 0.6, 100), (640, 0.8, 120),
        (1510, 1, 188), (741, 0.6, 271), (1358, 0.9, 334), (1682, 0.7, 153),
        (993, 0.7, 130), (99, 0.7, 100), (1068, 0.8, 154), (1669, 1, 289)]

ga = pyeasyga.GeneticAlgorithm(data)        # initialise the GA with data
ga.population_size = 200                    # increase population size to 200


# define a fitness function
def fitness(individual, data):
    weight, volume, price = 0, 0, 0
    for (selected, item) in zip(individual, data):
        if selected:
            weight += item[0]
            volume += item[1]
            price += item[2]
    if weight > 12210 or volume > 12:
        price = 0
    return price

ga.fitness_function = fitness               # set the GA's fitness function
ga.run()                                    # run the GA
print ga.best_individual()                  # print the GA's best solution
