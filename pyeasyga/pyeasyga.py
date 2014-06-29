# -*- coding: utf-8 -*-
import random
import copy
from operator import attrgetter


class GeneticAlgorithm(object):
    def __init__(self,
                 seed_data,
                 population_size=100,
                 generations=300,
                 crossover_probability=0.8,
                 mutation_probability=0.2):
        self.seed_data = seed_data
        self.population_size = population_size
        self.generations = generations
        self.crossover_probability = crossover_probability
        self.mutation_probability = mutation_probability

        self.current_generation = []
        self.elitism = True
        self.maximise_fitness = True
        self.create_individual = None
        self.fitness_function = None
        self.crossover_function = None
        self.mutate_function = None
        self.selection_function = None

    def create_initial_population(
            self, seed_data, population_size, create_individual):
        initial_population = []
        for _ in xrange(population_size):
            genes = create_individual(seed_data)
            individual = Chromosome(genes)
            initial_population.append(individual)
        return initial_population

    def calculate_population_fitness(self, data, population, fitness_function):
        for individual in population:
            individual.fitness = fitness_function(individual.genes, data)

    def rank_population(self, population, maximise_fitness=True):
        population.sort(key=attrgetter('fitness'), reverse=maximise_fitness)

    def create_new_population(
            self, population, crossover, prob_crossover, mutate, prob_mutate,
            selection, elitism):
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
            new_population.append(child_2)

        if elitism:
            new_population[0] = best

        return new_population

    def create_first_generation(
            self, data, population_size, create_individual, fitness_function,
            maximise_fitness=True):
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
        new_population = self.create_new_population(
            population, crossover_function, prob_crossover, mutate_function,
            prob_mutate, selection_function, elitism)
        self.calculate_population_fitness(
            data, new_population, fitness_function)
        self.rank_population(new_population, maximise_fitness)
        return new_population

    def run(self):
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

        for generation in xrange(1, generations):
            next_generation = self.create_next_generation(
                data, self.current_generation, fitness_func, selection,
                crossover, prob_crossover, mutate, prob_mutate, elitism,
                max_fitness)
            self.current_generation = next_generation

    def best_individual(self, population):
        best = population[0]
        return (best.fitness, best.genes)

    def last_generation(self):
        return ((member.fitness, member.genes) for member
                in self.current_generation)


class Chromosome(object):
    def __init__(self, genes):
        self.genes = genes
        self.fitness = 0

    def __repr__(self):
        return repr((self.fitness, self.genes))
