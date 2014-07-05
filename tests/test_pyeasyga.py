#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_pyeasyga
----------------------------------

Tests for `pyeasyga` module.
"""

import unittest
import random
import copy
from operator import attrgetter

from pyeasyga import pyeasyga


class TestPyeasyga(unittest.TestCase):

    ''' Test Problem: Assume you can only carry three items to sell in your bag.
        Pick a combination of items that maximises your profit. The profit for
        each item is listed. '''
    def setUp(self):
        self.seed_data = [('apple', 15), ('banana', 10), ('carrot', 12),
                          ('pear', 5), ('mango', 8)]

        member_1 = [0, 1, 0, 1, 1]
        member_2 = [1, 1, 0, 0, 1]
        member_3 = [1, 1, 1, 1, 0]
        member_4 = [0, 1, 1, 1, 1]

        self.population = []
        self.population.append(member_1)
        self.population.append(member_2)
        self.population.append(member_3)
        self.population.append(member_4)

        self.ga = pyeasyga.GeneticAlgorithm(self.seed_data)
        self.ga.population_size = 10
        self.ga.generations = 10

        self.ga.fitness_function = lambda member, data: sum(
            [profit for (selected, (fruit, profit)) in
             zip(member, data) if selected and
             member.count(1) == 3])

        def mutate(individual):
            mutate_index = random.randrange(len(individual))
            individual[mutate_index] = (0, 1)[individual[mutate_index] == 0]

        self.ga.selection_function = self.ga.tournament_selection

    def test_genetic_algorithm_initialisation_1(self):
        ''' Test default initialisation '''
        ga_1 = pyeasyga.GeneticAlgorithm(self.seed_data)

        assert ga_1.population_size == 50
        assert ga_1.generations == 100
        assert ga_1.elitism is True
        assert ga_1.crossover_probability == 0.8
        assert ga_1.mutation_probability == 0.2
        assert "Genetic Algorithm" in str(ga_1)
        assert "('population size', 50)" in str(ga_1)
        assert "('generations', 100)" in str(ga_1)
        assert "('crossover probability', 0.8)" in str(ga_1)
        assert "('muation probability', 0.2)" in str(ga_1)
        assert "('elitism', True)" in str(ga_1)
        assert "('maximise fitness', True)" in str(ga_1)

    def test_genetic_algorithm_initialisation_2(self):
        ''' Test initialisation with specific values '''
        ga_2 = pyeasyga.GeneticAlgorithm(
            self.seed_data, population_size=200, generations=500,
            crossover_probability=0.9, mutation_probability=0.05)
        ga_2.elitism = False
        ga_2.maximise_fitness = False
        fruit, profit = ga_2.seed_data[1]

        assert len(ga_2.seed_data) == 5
        assert (fruit, profit) == ('banana', 10)
        assert ga_2.population_size == 200
        assert ga_2.generations == 500
        assert ga_2.elitism is False
        assert ga_2.maximise_fitness is False
        assert ga_2.crossover_probability == 0.9
        assert ga_2.mutation_probability == 0.05

    def test_chromosome_initialisation_1(self):
        chromosome = pyeasyga.Chromosome(['a', 'b', 'c'])

        assert chromosome.genes == ['a', 'b', 'c']
        assert chromosome.fitness == 0
        assert str(chromosome) == "(0, ['a', 'b', 'c'])"

    def test_chromosome_initialisation_2(self):
        chromosome = pyeasyga.Chromosome(['d', 'e', 'f'])
        chromosome.fitness = 20

        assert chromosome.genes == ['d', 'e', 'f']
        assert chromosome.fitness == 20
        assert str(chromosome) == "(20, ['d', 'e', 'f'])"

    def test_fitness_function(self):
        func = self.ga.fitness_function
        data = self.ga.seed_data

        assert func([0, 1, 0, 1, 1], data) == 23
        assert func([1, 1, 0, 0, 1], data) == 33
        assert func([1, 1, 1, 1, 0], data) == 0
        assert func([0, 1, 1, 1, 1], data) == 0

    def test_crossover_function(self):
        parent_1 = [1, 1, 1, 1, 1]
        parent_2 = [0, 0, 0, 0, 0]
        child_1, child_2 = self.ga.crossover_function(parent_1, parent_2)

        assert child_1 not in [[0, 0, 0, 0, 0], [1, 1, 1, 1, 1]]
        assert child_2 not in [[0, 0, 0, 0, 0], [1, 1, 1, 1, 1]]

    def test_mutate_function(self):
        ''' Check that the individual is not the same after mutation
            Check that only one bit in the individual is changed '''
        individual = [0, 1, 1, 0, 1]
        self.ga.mutate_function(individual)

        res = [x == y for (x, y) in zip(individual, [0, 1, 1, 0, 1])]

        assert individual != [0, 1, 1, 0, 1]
        assert res.count(False) == 1

    def test_selection_function_1(self):
        ''' Test tournament selection '''
        population = []

        member_1 = pyeasyga.Chromosome([0, 1, 0, 1, 1])
        member_2 = pyeasyga.Chromosome([1, 1, 0, 0, 1])
        member_3 = pyeasyga.Chromosome([1, 1, 1, 1, 0])
        member_4 = pyeasyga.Chromosome([0, 1, 1, 1, 1])

        population.append(member_1)
        population.append(member_2)
        population.append(member_3)
        population.append(member_4)

        self.ga.calculate_population_fitness(
            self.ga.seed_data, population, self.ga.fitness_function)
        self.ga.tournament_size = 4
        self.ga.selection_function = self.ga.tournament_selection

        individual = self.ga.selection_function(population)

        assert individual.genes == [1, 1, 0, 0, 1]
        assert individual.fitness == 33
        assert len(individual.genes) == 5
        assert individual in population

    def test_selection_function_2(self):
        ''' Test tournament selection '''
        population = []

        member_1 = pyeasyga.Chromosome([0, 1, 0, 1, 1])
        member_2 = pyeasyga.Chromosome([1, 1, 0, 0, 1])
        member_3 = pyeasyga.Chromosome([1, 1, 1, 1, 0])
        member_4 = pyeasyga.Chromosome([0, 1, 1, 1, 1])

        population.append(member_1)
        population.append(member_2)
        population.append(member_3)
        population.append(member_4)

        self.ga.calculate_population_fitness(
            self.ga.seed_data, population, self.ga.fitness_function)
        self.ga.tournament_size = 0
        self.ga.selection_function = self.ga.tournament_selection

        individual = self.ga.selection_function(population)

        assert len(individual.genes) == 5
        assert individual in population

    def test_selection_function_3(self):
        ''' Test random selection '''
        self.ga.selection_function = self.ga.random_selection
        individual = self.ga.selection_function(self.population)

        assert len(individual) == 5
        assert individual in self.population

    def test_create_individual(self):
        data = self.ga.seed_data
        individual = self.ga.create_individual(data)

        assert len(individual) == 5
        assert all([ind in (0, 1) for ind in individual if ind in (0, 1)])

    def test_create_initial_population(self):
        pop_size = self.ga.population_size
        func = self.ga.create_individual
        data = self.ga.seed_data

        initial_population = self.ga.create_initial_population(
            data, pop_size, func)

        assert len(initial_population) == pop_size
        assert isinstance(initial_population[0],
                          type(pyeasyga.Chromosome([1])))
        assert sum([member.fitness for member in initial_population]) == 0

    def test_calculate_population_fitness(self):
        data = self.ga.seed_data
        pop_size = self.ga.population_size
        create_func = self.ga.create_individual

        population = self.ga.create_initial_population(
            data, pop_size, create_func)

        fitness_func = self.ga.fitness_function
        self.ga.calculate_population_fitness(data, population, fitness_func)

        assert sum([member.fitness for member in population]) > 0

    def test_rank_population(self):
        data = self.seed_data

        pop_size = self.ga.population_size
        create_func = self.ga.create_individual
        fitness_func = self.ga.fitness_function

        population = self.ga.create_initial_population(
            data, pop_size, create_func)
        self.ga.calculate_population_fitness(data, population, fitness_func)

        new_population = copy.deepcopy(population)
        new_population.sort(key=attrgetter('fitness'), reverse=True)

        self.ga.rank_population(population, True)

        assert population[0].fitness == new_population[0].fitness
        assert population[1].fitness == new_population[1].fitness

    def test_create_new_population(self):
        data = self.seed_data

        pop_size = self.ga.population_size
        create_func = self.ga.create_individual
        fitness_func = self.ga.fitness_function

        population = self.ga.create_initial_population(
            data, pop_size, create_func)
        self.ga.calculate_population_fitness(data, population, fitness_func)
        self.ga.rank_population(population, True)

        crossover = self.ga.crossover_function
        prob_crossover = self.ga.crossover_probability
        mutate = self.ga.mutate_function
        prob_mutate = self.ga.mutation_probability
        selection = self.ga.selection_function
        elitism = True

        new_population = self.ga.create_new_population(
            population, crossover, prob_crossover, mutate, prob_mutate,
            selection, elitism)

        assert len(new_population) == self.ga.population_size
        assert new_population[0].fitness == population[0].fitness
        assert new_population[0].genes == population[0].genes

    def test_create_first_generation(self):
        data = self.ga.seed_data
        pop_size = self.ga.population_size
        create_func = self.ga.create_individual
        fitness_func = self.ga.fitness_function
        max_fitness = self.ga.maximise_fitness

        population = self.ga.create_first_generation(
            data, pop_size, create_func, fitness_func, max_fitness)

        assert len(population) == pop_size
        assert isinstance(population[0], type(pyeasyga.Chromosome([1])))

    def test_create_next_generation(self):
        data = self.ga.seed_data
        pop_size = self.ga.population_size
        create_func = self.ga.create_individual
        fitness_func = self.ga.fitness_function
        selection = self.ga.selection_function
        crossover = self.ga.crossover_function
        prob_crossover = self.ga.crossover_probability
        mutate = self.ga.mutate_function
        prob_mutate = self.ga.mutation_probability
        elitism = self.ga.elitism
        max_fitness = self.ga.maximise_fitness

        population = self.ga.create_first_generation(
            data, pop_size, create_func, fitness_func, max_fitness)

        next_gen = self.ga.create_next_generation(
            data, population, fitness_func, selection, crossover,
            prob_crossover, mutate, prob_mutate, elitism, max_fitness)

        assert len(next_gen) == pop_size
        assert isinstance(population[0], type(pyeasyga.Chromosome([1])))

    def test_run(self):
        self.ga.run()
        current_gen = self.ga.current_generation
        last_generation = self.ga.last_generation()

        assert len(current_gen) == self.ga.population_size
        assert isinstance(current_gen[0], type(pyeasyga.Chromosome([1])))
        assert isinstance(last_generation.next(), type((1, [1, 1, 1, 1, 1])))
        assert len(last_generation.next()) == 2
        assert len(last_generation.next()[1]) == 5

    def test_best_individual(self):
        data = self.seed_data
        pop_size = self.ga.population_size
        create_func = self.ga.create_individual
        fitness_func = self.ga.fitness_function
        max_fitness = self.ga.maximise_fitness

        self.ga.current_generation = self.ga.create_first_generation(
            data, pop_size, create_func, fitness_func, max_fitness)

        best_fitness, best_genes = self.ga.best_individual()

        assert best_fitness == self.ga.current_generation[0].fitness
        assert best_genes == self.ga.current_generation[0].genes

    def test_last_generation(self):
        data = self.ga.seed_data
        pop_size = self.ga.population_size
        create_func = self.ga.create_individual
        fitness_func = self.ga.fitness_function
        max_fitness = self.ga.maximise_fitness

        self.ga.current_generation = self.ga.create_first_generation(
            data, pop_size, create_func, fitness_func, max_fitness)
        last_generation = self.ga.last_generation()

        assert isinstance(last_generation.next(), type((1, [1, 1, 1, 1, 1])))
        assert len(last_generation.next()) == 2
        assert len(last_generation.next()[1]) == 5

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
