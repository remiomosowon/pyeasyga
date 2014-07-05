========
Usage
========

To use pyeasyga in a project::

	from pyeasyga import pyeasyga

A Simple Example
----------------

Here is a simple example using the default ``pyeasyga.GeneticAlgorithm`` parameters.

The problem is to select only two items from a list while
maximising the cost of the selected items. *Selecting the pear
and apple gives the maximum cost of 90.* :: 

    >>> from pyeasyga.pyeasyga import GeneticAlgorithm
    >>>
    >>> data = [('pear', 50), ('apple', 35), ('banana', 40)]
    >>> ga = GeneticAlgorithm(data)
    >>>
    >>> def fitness (individual, data):
    >>>     return sum([profit for (selected, (fruit, profit)) in
    >>>                 zip(individual, data) if selected and
    >>>                 individual.count(1) == 2])
    >>>
    >>> ga.fitness_function = fitness
    >>> ga.run()
    >>> print ga.best_individual()

.. include:: ../examples/README.rst
