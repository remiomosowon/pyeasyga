import random
from pyeasyga import pyeasyga

# setup seed data
seed_data = [0, 1, 2, 3, 4, 5, 6, 7]

# initialise the GA
ga = pyeasyga.GeneticAlgorithm(seed_data,
                               population_size=200,
                               generations=100,
                               crossover_probability=0.8,
                               mutation_probability=0.2,
                               elitism=True,
                               maximise_fitness=False)


# define and set function to create a candidate solution representation
def create_individual(data):
    individual = data[:]
    random.shuffle(individual)
    return individual

ga.create_individual = create_individual


# define and set the GA's crossover operation
def crossover(parent_1, parent_2):
    crossover_index = random.randrange(1, len(parent_1))
    child_1a = parent_1[:crossover_index]
    child_1b = [i for i in parent_2 if i not in child_1a]
    child_1 = child_1a + child_1b

    child_2a = parent_2[crossover_index:]
    child_2b = [i for i in parent_1 if i not in child_2a]
    child_2 = child_2a + child_2b

    return child_1, child_2

ga.crossover_function = crossover


# define and set the GA's mutation operation
def mutate(individual):
    mutate_index1 = random.randrange(len(individual))
    mutate_index2 = random.randrange(len(individual))
    index_val1 = individual[mutate_index1]
    index_val2 = individual[mutate_index2]
    index_val1, index_val2 = index_val2, index_val1

ga.mutate_function = mutate


# define and set the GA's selection operation
def selection(population):
    return random.choice(population)

ga.selection_function = selection


# define a fitness function
def fitness(individual, data):
    collisions = 0
    for item in individual:
        item_index = individual.index(item)
        for elem in individual:
            elem_index = individual.index(elem)
            if item_index != elem_index:
                if item - (elem_index - item_index) == elem \
                        or (elem_index - item_index) + item == elem:
                    collisions += 1
    return collisions

ga.fitness_function = fitness       # set the GA's fitness function
ga.run()                            # run the GA


# function to print out chess board with queens placed in position
def print_board(board_representation):
    def print_x_in_row(row_length, x_position):
        print '',
        for _ in xrange(row_length):
            print '---',
        print '\n|',
        for i in xrange(row_length):
            if i == x_position:
                print '{} |'.format('X'),
            else:
                print '  |',
        print ''

    def print_board_bottom(row_length):
        print '',
        for _ in xrange(row_length):
            print '---',

    num_of_rows = len(board_representation)
    row_length = num_of_rows    # rows == columns in a chessboard

    for row in xrange(num_of_rows):
        print_x_in_row(row_length, board_representation[row])

    print_board_bottom(row_length)
    print '\n'

# print the GA's best solution (valid only if there are no collisions)
if ga.best_individual()[0] == 0:
    print ga.best_individual()
    print_board(ga.best_individual()[1])
else:
    print None
