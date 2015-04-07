Examples
---------

1-Dimensional Knapsack Problem
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``one_dimensional_knapsack.py``

  This example solves the one-dimensional knapsack problem used as the example
  on the Wikipedia page for the `Knapsack problem <http://en.wikipedia.org/wiki/Knapsack_problem>`_. Here is the `problem statement <http://git.io/fa25nw>`_. ::

    from pyeasyga import pyeasyga

    # setup data
    data = [{'name': 'box1', 'value': 4, 'weight': 12},
            {'name': 'box2', 'value': 2, 'weight': 1},
            {'name': 'box3', 'value': 10, 'weight': 4},
            {'name': 'box4', 'value': 1, 'weight': 1},
            {'name': 'box5', 'value': 2, 'weight': 2}]

    ga = pyeasyga.GeneticAlgorithm(data)        # initialise the GA with data

    # define a fitness function
    def fitness(individual, data):
        values, weights = 0, 0
        for selected, box in zip(individual, data):
            if selected:
                values += box.get('value')
                weights += box.get('weight')
        if weights > 15:
            values = 0
        return values

    ga.fitness_function = fitness               # set the GA's fitness function
    ga.run()                                    # run the GA
    print ga.best_individual()                  # print the GA's best solution

  To run::

    $ python one_dimensional_knapsack.py

  Output::

    (15, [0, 1, 1, 1, 1])

  i.e. if you select all boxes except the first one, you get a maximum amount of
  $15 while still keeping the overall weight under or equal to 15kg.


Multi-Dimensional Knapsack Problem
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``multi_dimensional_knapsack.py``
  
  This solves the multidimensional knapsack problem (MKP) seen `here <http://git.io/Wz4jBQ>`_. It is a well-known NP-hard combinatorial optimisation problem. ::

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
    ga.population_size = 200                    # increase population size to 200 (default value is 50)

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

  To run::

    $ python multi_dimensional_knapsack.py

  Output::

    (3531, [0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1])

  i.e. the indicated selection of items satisfies the required weight and volume
  constraints, and gives a total value of 3531. 

  
8 Queens Puzzle
~~~~~~~~~~~~~~~

``8_queens.py``

  This solves the `8 queens puzzle <http://en.wikipedia.org/wiki/Eight_queens_puzzle>`_. ::

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
        individual[mutate_index1], individual[mutate_index2] = individual[mutate_index2], individual[mutate_index1] 

    ga.mutate_function = mutate

    # define and set the GA's selection operation
    def selection(population):
        return random.choice(population)

    ga.selection_function = selection

    # define a fitness function
    def fitness (individual, data):
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
        row_length = num_of_rows    #rows == columns in a chessboard
        
        for row in xrange(num_of_rows):
            print_x_in_row(row_length, board_representation[row])
        
        print_board_bottom(row_length)
        print '\n'

    # print the GA's best solution; a solution is valid only if there are no collisions
    if ga.best_individual()[0] == 0:
        print ga.best_individual()
        print_board(ga.best_individual()[1])
    else:
        print None

  To run::
  
    $ python 8_queens.py 
  
  Output::

    (0, [2, 5, 7, 0, 3, 6, 4, 1])

     --- --- --- --- --- --- --- ---
    |   |   | X |   |   |   |   |   |
     --- --- --- --- --- --- --- ---
    |   |   |   |   |   | X |   |   |
     --- --- --- --- --- --- --- ---
    |   |   |   |   |   |   |   | X |
     --- --- --- --- --- --- --- ---
    | X |   |   |   |   |   |   |   |
     --- --- --- --- --- --- --- ---
    |   |   |   | X |   |   |   |   |
     --- --- --- --- --- --- --- ---
    |   |   |   |   |   |   | X |   |
     --- --- --- --- --- --- --- ---
    |   |   |   |   | X |   |   |   |
     --- --- --- --- --- --- --- ---
    |   | X |   |   |   |   |   |   |
     --- --- --- --- --- --- --- ---
