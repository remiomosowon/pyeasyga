# -*- coding: utf-8 -*-
"""
    pyeasyga module

"""

import random
import copy
from operator import attrgetter


class GeneticAlgorithm(object):
    """Genetic Algorithm class.

    This is the main class that controls the functionality of the Genetic
    Algorithm.

    A simple example of usage:

    >>> # Select only two items from the list and maximise profit
    >>> from pyeasyga.pyeasyga import GeneticAlgorithm
    >>> input_data = [('pear', 50), ('apple', 35), ('banana', 40)]
    >>> easyga = GeneticAlgorithm(input_data)
    >>> def fitness (member, data):
    >>>     return sum([profit for (selected, (fruit, profit)) in
    >>>                 zip(member, data) if selected and
    >>>                 member.count(1) == 2])
    >>> easyga.fitness_function = fitness
    >>> easyga.run()
    >>> print easyga.best_individual()

    """

    def __init__(self,
                 seed_data,
                 population_size=50,
                 generations=100,
                 crossover_probability=0.8,
                 mutation_probability=0.2):
        """Instantiate the Genetic Algorithm.

        :param seed_data: input data to the Genetic Algorithm
        :type seed_data: list of objects
        :param int population_size: size of population
        :param int generations: number of generations to evolve
        :param float crossover_probability: probability of crossover operation
        :param float mutation_probability: probability of mutation operation

        """

        self.seed_data = seed_data
        self.population_size = population_size
        self.generations = generations
        self.crossover_probability = crossover_probability
        self.mutation_probability = mutation_probability

        self.current_generation = []
        self.elitism = True
        self.maximise_fitness = True

        def create_individual(seed_data):
            """Create a candidate solution representation.

            e.g. for a bit array representation:

            >>> return [random.randint(0, 1) for _ in xrange(len(data))]

            :param seed_data: input data to the Genetic Algorithm
            :type seed_data: list of objects
            :returns: candidate solution representation as a list

            """
            return [random.randint(0, 1) for _ in xrange(len(seed_data))]

        def crossover(parent_1, parent_2):
            """Crossover (mate) two parents to produce two children.

            :param parent_1: candidate solution representation (list)
            :param parent_2: candidate solution representation (list)
            :returns: tuple containing two children

            """
            index = random.randrange(1, len(parent_1))
            child_1 = parent_1[:index] + parent_2[index:]
            child_2 = parent_2[:index] + parent_1[index:]
            return child_1, child_2

        def mutate(individual):
            """Reverse the bit of a random index in an individual."""
            mutate_index = random.randrange(len(individual))
            individual[mutate_index] = (0, 1)[individual[mutate_index] == 0]

        def random_selection(population):
            """Select and return a random member of the population."""
            return random.choice(population)

        def tournament_selection(population):
            """Select a random number of individuals from the population and
            return the fittest member of them all.

            """
            if self.tournament_size == 0:
                self.tournament_size = 2
            members = random.sample(population, self.tournament_size)
            members.sort(
                key=attrgetter('fitness'), reverse=self.maximise_fitness)
            return members[0]

        self.fitness_function = None
        self.tournament_selection = tournament_selection
        self.tournament_size = self.population_size / 10
        self.random_selection = random_selection
        self.create_individual = create_individual
        self.crossover_function = crossover
        self.mutate_function = mutate
        self.selection_function = self.tournament_selection

    def create_initial_population(
            self, seed_data, population_size, create_individual):
        """Create members of the first population randomly.

        :param seed_data: input data to the Genetic Algorithm
        :type seed_data: list of objects
        :param int population_size: size of population
        :param create_individual: function that creates candidate solutions
        :type create_individual: :func:
        :returns: initial population as a list of candidate solutions

        """
        initial_population = []
        for _ in xrange(population_size):
            genes = create_individual(seed_data)
            individual = Chromosome(genes)
            initial_population.append(individual)
        return initial_population

    def calculate_population_fitness(self, data, population, fitness_function):
        """Calculate the fitness of every member of the given population using
        the supplied fitness_function.

        """
        for individual in population:
            individual.fitness = fitness_function(individual.genes, data)

    def rank_population(self, population, maximise_fitness=True):
        """Sort the population by fitness according to the order defined by
        maximise_fitness.

        """
        population.sort(key=attrgetter('fitness'), reverse=maximise_fitness)

    def create_new_population(
            self, population, crossover, prob_crossover, mutate, prob_mutate,
            selection, elitism):
        """Create a new population using the genetic operators (selection,
        crossover, and mutation) supplied.

        """
        new_population = []
        best = copy.deepcopy(population[0])

        while len(new_population) < len(population):
            parent_1 = copy.deepcopy(selection(population))
            parent_2 = copy.deepcopy(selection(population))

            can_crossover = random.random() < prob_crossover
            can_mutate = random.random() < prob_mutate

            child_1, child_2 = parent_1, parent_2
            child_1.fitness, child_2.fitness = 0, 0

            if can_crossover:
                child_1.genes, child_2.genes = crossover(parent_1.genes,
                                                         parent_2.genes)

            if can_mutate:
                mutate(child_1.genes)
                mutate(child_2.genes)

            new_population.append(child_1)
            if len(new_population) < len(population):
                new_population.append(child_2)

        if elitism:
            new_population[0] = best

        return new_population

    def create_first_generation(
            self, data, population_size, create_individual, fitness_function,
            maximise_fitness=True):
        """Create the first population, calculate the population's fitness and
        rank the population by fitness according to the order specified.

        """
        initial_population = self.create_initial_population(
            data, population_size, create_individual)
        self.calculate_population_fitness(
            data, initial_population, fitness_function)
        self.rank_population(initial_population, maximise_fitness)
        return initial_population

    def create_next_generation(
            self, data, population, fitness_function,
            selection_function, crossover_function, prob_crossover,
            mutate_function, prob_mutate, elitism, maximise_fitness=True):
        """Create subsequent populations, calculate the population fitness and
        rank the population by fitness in the order specified.

        """
        new_population = self.create_new_population(
            population, crossover_function, prob_crossover, mutate_function,
            prob_mutate, selection_function, elitism)
        self.calculate_population_fitness(
            data, new_population, fitness_function)
        self.rank_population(new_population, maximise_fitness)
        return new_population

    def run(self):
        """Run (solve) the Genetic Algorithm."""
        data = self.seed_data
        pop_size = self.population_size
        generations = self.generations
        create_func = self.create_individual
        fitness_func = self.fitness_function
        selection = self.selection_function
        crossover = self.crossover_function
        prob_crossover = self.crossover_probability
        mutate = self.mutate_function
        prob_mutate = self.mutation_probability
        elitism = self.elitism
        max_fitness = self.maximise_fitness

        self.current_generation = self.create_first_generation(
            data, pop_size, create_func, fitness_func, max_fitness)

        for _ in xrange(1, generations):
            next_generation = self.create_next_generation(
                data, self.current_generation, fitness_func, selection,
                crossover, prob_crossover, mutate, prob_mutate, elitism,
                max_fitness)
            self.current_generation = next_generation

    def best_individual(self):
        """Return the individual with the best fitness in the current
        generation.

        """
        best = self.current_generation[0]
        return (best.fitness, best.genes)

    def last_generation(self):
        """Return the members of the last generation in an iterable form (i.e
        a generator.

        """
        return ((member.fitness, member.genes) for member
                in self.current_generation)


class Chromosome(object):
    """ Chromosome class that encapsulates an individual's fitness and solution
    representation.

    """
    def __init__(self, genes):
        """Initialise the Chromosome."""
        self.genes = genes
        self.fitness = 0

    def __repr__(self):
        """Return initialised Chromosome representation in human readable form.

        """
        return repr((self.fitness, self.genes))
