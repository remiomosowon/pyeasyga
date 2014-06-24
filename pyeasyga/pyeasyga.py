# -*- coding: utf-8 -*-
from operator import attrgetter


class GeneticAlgorithm(object):
    def __init__(self,
                 seed_data,
                 population_size=100,
                 generations=300,
                 elitism=True,
                 crossover_probability=0.8,
                 mutation_probability=0.2):
        self.seed_data = seed_data
        self.population_size = population_size
        self.generations = generations
        self.elitism = elitism
        self.crossover_probability = crossover_probability
        self.mutation_probability = mutation_probability
        self.current_generation = []

        self.fitness_function = None
        self.crossover_function = None
        self.mutate_function = None
        self.selection_function = None
        self.create_individual = None

    def create_initial_population(self, population_size, create_individual):
        initial_population = []
        for individual_id in xrange(population_size):
            genes = create_individual()
            individual = Chromosome(individual_id, genes)
            initial_population.append(individual)
        return initial_population

    def calculate_population_fitness(self, population, fitness_function):
        for individual in population:
            individual.fitness = fitness_function(individual.genes)

    def rank_population(self, population, maximise_fitness=True):
        self.population.sort(key=attrgetter('fitness'),
                             reversed=maximise_fitness)

    def create_new_population(self, population, crossover, mutate, selection):
        pass

    def create_first_generation(self, population_size, create_individual,
                                fitness_function, maximise_fitness):
        initial_population = self.create_initial_population(population_size,
                                                            create_individual)
        self.calculate_population_fitness(initial_population, fitness_function)
        self.rank_population(initial_population, maximise_fitness)
        return initial_population

    def create_next_generation(self, population, fitness_function,
                               crossover_function, mutate_function,
                               selection_function, maximise_fitness):
        new_population = self.create_new_population(population,
                                                    crossover_function,
                                                    mutate_function,
                                                    selection_function)
        self.calculate_population_fitness(new_population, fitness_function)
        self.rank_population(new_population, maximise_fitness)
        return new_population

    def best_individual(self):
        pass

    def last_generation(self):
        pass


class Chromosome(object):
    def __init__(self, chromosome_id, genes):
        self.chromosome_id = chromosome_id
        self.genes = genes
        self.fitness = 0.0
