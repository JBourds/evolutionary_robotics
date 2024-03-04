"""
hillclimber.py

Class definition for implementing the hill climber algorithm to achieve optimal/near-optimal robot performance.

Author: Jordan Bourdeau
Date Created: 3/3/24
"""

import copy

import constants as c
from solution import Solution

class HillClimber:
    
    def __init__(self):
        """
        Class representing the Hillclimber genetic algorithm implementation.

        # Fields:
            * `parent`: The parent solution. Used for mutation to derive child solution.
            * `child`:  The child solution. Derived from the parent.
        """
        self.parent: Solution = Solution()
        self.child: Solution = None

    def evolve(self):
        """
        Method to evolve the candidate solutions using the parallel hillclimber technique.
        """
        self.parent.evaluate('GUI')
        for generation in range(c.NUMBER_OF_GENERATIONS):
            self.evolve_one_generation()

    def evolve_one_generation(self):
        """
        Method to evolve a single generation with randomly mutated children.
        """
        self.spawn()
        self.mutate()
        self.child.evaluate('direct')
        self.print()
        self.select()

    def spawn(self):
        """
        Method to spawn copies of the parents for the next generation.
        """
        self.child = copy.deepcopy(self.parent)

    def mutate(self):
        """
        Method to select a child or parent solution based on performance to be the parent in the 
        next generation.
        """
        self.child.mutate()

    def select(self):
        """
        Method to select a child or parent solution based on performance to be the parent in the 
        next generation.
        """
        # In this case, lower values correspond to better fitness
        if self.child.fitness < self.parent.fitness:
            self.parent = self.child

    def show_best(self):
        """
        Method to show the best solution after the simulation has completed.
        """
        self.parent.evaluate('GUI')

    def print(self):
        """
        Method to print the fitness values for the child/parent solutions.
        """
        print(f'Parent Fitness: {self.parent.fitness}\t Child Fitness: {self.child.fitness}')