========
Usage
========

To use pyeasyga in a project:

Simple
------

    1. Import the module ::

        from pyeasyga import pyeasyga

    2. Setup your data e.g. ::

        data = [('pear', 50), ('apple', 35), ('banana', 40)]

    3. Initialise the GeneticAlgorithm class with the only required
       parameter: ``data`` ::

        ga = pyeasyga.GeneticAlgorithm(data)

    4. Define a fitness function for the Genetic Algorithm. The function should
       take two parameters: a candidate soultion (an individual in GA speak),
       and the data that is used to help determine the individual's fitness ::

        def fitness (individual, data):
            fitness = 0
            if individual.count(1) == 2:
                for (selected, (fruit, profit)) in zip(individual, data):
                    if selected:
                        fitness += profit
            return fitness

    5. Set the Genetic Algorithm's ``fitness_function`` attribute to your
       defined fitness function ::

        ga.fitness_function = fitness

    6. Run the Genetic Algorithm ::

        ga.run()

    7. Print the best solution ::

        print ga.best_individual()


Advanced
--------

    1. Import the module ::

        from pyeasyga import pyeasyga

    2. Setup your data e.g. ::

        data = [('pear', 50), ('apple', 35), ('banana', 40)]

    3. Initialise the GeneticAlgorithm class with the required ``data``
       parameter, and all or some of the optional parameters ::

        ga = pyeasyga.GeneticAlgorithm(data,
                                       population_size=10,
                                       generations=20,
                                       crossover_probability=0.8,
                                       mutation_probability=0.05,
                                       elitism=True,
                                       maximise_fitness=True,
                                       verbose=False)
                                       

       Or ::

            ga = pyeasyga.GeneticAlgorithm(data, 10, 20, 0.8, 0.05, True, True)

       Or, just initialise the GeneticAlgorithm class with only the required
       ``data`` parameter, if you are content with the default parameters ::
       
            ga = pyeasyga.GeneticAlgorithm(data)

    4. Optionally, define a function to create a representation of a candidate
       solution (an individual in GA speak). This function should take in the 
       data defined in step 1. as a parameter. ::

        def create_individual(data):
            return [random.randint(0, 1) for _ in xrange(len(data))]

    5. Set the Genetic Algorithm's ``create_individual`` attribute to your
       defined function ::

        ga.create_individual = create_individual


    6. Optionally, define and set functions for the Genetic Algorithm's genetic
       operators (i.e. crossover, mutate, selection) ::

        # For the crossover function, supply two individuals (i.e. candidate 
        # solution representations) as parameters,
        def crossover(parent_1, parent_2):
            crossover_index = random.randrange(1, len(parent_1))
            child_1 = parent_1[:index] + parent_2[index:]
            child_2 = parent_2[:index] + parent_1[index:]
            return child_1, child_2

        # and set the Genetic Algorithm's ``crossover_function`` attribute to
        # your defined function
        ga.crossover_function = crossover


        # For the mutate function, supply one individual (i.e. a candidate 
        # solution representation) as a parameter,
        def mutate(individual):
            mutate_index = random.randrange(len(individual))
            if individual[mutate_index] == 0:
                individual[mutate_index] = 1
            else:
                individual[mutate_index] = 0

        # and set the Genetic Algorithm's ``mutate_function`` attribute to
        # your defined function
        ga.mutate_function = mutate

        
        # For the selection function, supply a ``population`` parameter
        def selection(population):
            return random.choice(population)        

        # and set the Genetic Algorithm's ``selection_function`` attribute to
        # your defined function
        ga.selection_function = selection

    7. Define a fitness function for the Genetic Algorithm. The function should
       take two parameters: a candidate solution representation (an individual 
       in GA speak), and the data that is used to help determine the 
       individual's fitness ::

        def fitness (individual, data):
            fitness = 0
            if individual.count(1) == 2:
                for (selected, (fruit, profit)) in zip(individual, data):
                    if selected:
                        fitness += profit
            return fitness

    8. Set the Genetic Algorithm's ``fitness_function`` attribute to your
       defined fitness function ::

        ga.fitness_function = fitness

    9. Run the Genetic Algorithm ::

        ga.run()

    #. Print the best solution::

        print ga.best_individual()

    #. You can also examine all the individuals in the last generation::

        for individual in ga.last_generation():
            print individual


Example of Simple Usage
-----------------------

This simple example uses the default ``pyeasyga.GeneticAlgorithm`` parameters.

The problem is to select only two items from a list (the supplied data) while
maximising the cost of the selected items. *(Solution: Selecting the pear and 
apple gives the highest possible cost of 90.)* :: 

    >>> from pyeasyga.pyeasyga import GeneticAlgorithm
    >>>
    >>> data = [('pear', 50), ('apple', 35), ('banana', 40)]
    >>> ga = GeneticAlgorithm(data)
    >>>
    >>> def fitness (individual, data):
    >>>     fitness = 0
    >>>     if individual.count(1) == 2:
    >>>         for (selected, (fruit, profit)) in zip(individual, data):
    >>>             if selected:
    >>>                 fitness += profit
    >>>     return fitness
    >>>
    >>> ga.fitness_function = fitness
    >>> ga.run()
    >>> print ga.best_individual()


Example of Advanced Usage
-------------------------

This example uses both default and optional ``pyeasyga.GeneticAlgorithm``
parameters.

The problem is to select only two items from a list (the supplied data) while
maximising the cost of the selected items. *(Solution: Selecting the pear and 
apple gives the highest possible cost of 90.)* :: 

    >>> from pyeasyga.pyeasyga import GeneticAlgorithm
    >>>
    >>> data = [('pear', 50), ('apple', 35), ('banana', 40)]
    >>> ga = GeneticAlgorithm(data, 20, 50, 0.8, 0.2, True, True)
    >>>
    >>> def create_individual(data):
    >>>     return [random.randint(0, 1) for _ in xrange(len(data))]
    >>>
    >>> ga.create_individual = create_individual
    >>>
    >>>
    >>> def crossover(parent_1, parent_2):
    >>>     crossover_index = random.randrange(1, len(parent_1))
    >>>     child_1 = parent_1[:index] + parent_2[index:]
    >>>     child_2 = parent_2[:index] + parent_1[index:]
    >>>     return child_1, child_2
    >>>
    >>> ga.crossover_function = crossover
    >>>
    >>>
    >>> def mutate(individual):
    >>>     mutate_index = random.randrange(len(individual))
    >>>     if individual[mutate_index] == 0:
    >>>         individual[mutate_index] = 1
    >>>     else:
    >>>         individual[mutate_index] = 0
    >>>
    >>> ga.mutate_function = mutate
    >>>
    >>>
    >>> def selection(population):
    >>>     return random.choice(population)        
    >>>
    >>> ga.selection_function = selection
    >>>
    >>> def fitness (individual, data):
    >>>     fitness = 0
    >>>     if individual.count(1) == 2:
    >>>         for (selected, (fruit, profit)) in zip(individual, data):
    >>>             if selected:
    >>>                 fitness += profit
    >>>     return fitness
    >>>
    >>> ga.fitness_function = fitness
    >>> ga.run()
    >>> print ga.best_individual()
    >>>
    >>> for individual in ga.last_generation():
    >>>     print individual
