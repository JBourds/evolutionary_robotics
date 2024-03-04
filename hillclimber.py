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
        self.parent: Solution = Solution()
        self.child: Solution = None

    def evolve(self):
        self.parent.evaluate('GUI')
        for generation in range(c.NUMBER_OF_GENERATIONS):
            self.evolve_one_generation()
        self.show_best()

    def evolve_one_generation(self):
        self.spawn()
        self.mutate()
        self.child.evaluate('direct')
        self.print()
        self.select()

    def spawn(self):
        self.child = copy.deepcopy(self.parent)

    def mutate(self):
        self.child.mutate()

    def select(self):
        # In this case, lower values correspond to better fitness
        if self.child.fitness < self.parent.fitness:
            self.parent = self.child

    def show_best(self):
        self.parent.evaluate('GUI')

    def print(self):
        print(f'Parent Fitness: {self.parent.fitness}\t Child Fitness: {self.child.fitness}')