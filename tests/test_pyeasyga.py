#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_pyeasyga
----------------------------------

Tests for `pyeasyga` module.
"""

import unittest
import random

from pyeasyga import pyeasyga


class TestPyeasyga(unittest.TestCase):

    ''' Test Problem: Assume you can only carry two items to sell in your bag.
        Pick a combination of items that maximises your profit. The profit for
        each item is listed. '''
    def setUp(self):
        self.seed_data = [('apple', 15), ('banana', 10), ('carrot', 12),
                          ('pear', 5)]

        member_1 = [0, 1, 0, 1]
        member_2 = [1, 1, 0, 0]
        member_3 = [1, 1, 1, 1]
        member_4 = [0, 1, 1, 1]

        self.population = []
        self.population.append(member_1)
        self.population.append(member_2)
        self.population.append(member_3)
        self.population.append(member_4)

    def test_genetic_algorithm_initialisation_1(self):
        ga = pyeasyga.GeneticAlgorithm(self.seed_data)
        assert ga.population_size == 100
        assert ga.generations == 300
        assert ga.elitism is True
        assert ga.crossover_probability == 0.8
        assert ga.mutation_probability == 0.2

    def test_genetic_algorithm_initialisation_2(self):
        ga = pyeasyga.GeneticAlgorithm(
            self.seed_data, population_size=200, generations=500,
            elitism=False, crossover_probability=0.9,
            mutation_probability=0.05)

        fruit, profit = ga.seed_data[1]

        assert len(ga.seed_data) == 4
        assert (fruit, profit) == ('banana', 10)
        assert ga.population_size == 200
        assert ga.generations == 500
        assert ga.elitism is False
        assert ga.crossover_probability == 0.9
        assert ga.mutation_probability == 0.05

    def test_fitness_function(self):
        ga = pyeasyga.GeneticAlgorithm(self.seed_data)
        ga.fitness_function = lambda member: sum(
            [profit for (selected, (fruit, profit)) in
             zip(member, self.seed_data) if selected and
             len(filter(lambda x: x == 1, member)) == 2])

        assert ga.fitness_function(self.population[0]) == 15
        assert ga.fitness_function(self.population[1]) == 25
        assert ga.fitness_function(self.population[2]) == 0
        assert ga.fitness_function(self.population[3]) == 0

    def test_crossover_function(self):
        pass

    def test_mutate_function(self):
        pass

    def test_selection_function(self):
        pass

    def test_create_individual(self):
        ga = pyeasyga.GeneticAlgorithm(self.seed_data)
        ga.create_individual = lambda seed_data: [
            random.randint(0, 1) for _ in seed_data]

        individual = ga.create_individual(self.seed_data)
        assert len(individual) == 4
        assert all([ind in (0, 1) for ind in individual if ind in (0, 1)])

    def test_create_initial_population(self):
        pass

    def test_calculate_population_fitness(self):
        pass

    def test_rank_population(self):
        pass

    def test_create_new_population(self):
        pass

    def test_create_first_generation(self):
        pass

    def test_create_next_generation(self):
        pass

    def test_best_individual(self):
        pass

    def test_last_generation(self):
        pass

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
