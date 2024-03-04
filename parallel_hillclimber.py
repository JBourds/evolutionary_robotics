"""
parallel_hillclimber.py

Class definition for the paralellized version of the hillclimber algorithm.

Author: Jordan Bourdeau
Date Created: 3/3/24
"""

import copy

import constants as c
from solution import Solution

class ParallelHillClimber:
    
    def __init__(self):
        """
        Class representing the parallelized Hillclimber genetic algorithm implementation.

        # Fields:
            * `parents`: The parent solutions.
        """

        # Delete any remnant files
        c.delete_all_brain_files()
        c.delete_all_fitness_files()

        self.next_available_id: int = 0
        
        self.parents: dict[int: Solution] = {}
        for i in range(c.POPULATION_SIZE):
            self.parents[i] = Solution(self.next_available_id)
            self.next_available_id += 1
        self.children: dict[int: Solution] = {}

    def evolve(self):
        """
        Method to evolve the candidate solutions using the parallel hillclimber technique.
        """
        self.evaluate(self.parents.values())
        for _ in range(c.NUMBER_OF_GENERATIONS):
            self.evolve_one_generation()
        self.show_best()

    def evolve_one_generation(self):
        """
        Method to evolve a single generation with randomly mutated children.
        """
        self.spawn()
        self.mutate()
        self.evaluate(self.children.values())
        self.print()
        self.select()

    def evaluate(self, solutions: list[Solution]):
        """
        Method to evaluate a list of candidate solutions by simulating them and retrieving fitness values.
        """
        for solution in solutions:
            solution.start_simulation('DIRECT')
        for solution in solutions:
            solution.wait_for_simulation_to_end()

    def spawn(self):
        """
        Method to spawn copies of the parents for the next generation.
        """
        for i, parent in self.parents.items():
            self.children[i] = copy.deepcopy(parent)
            self.next_available_id += 1

    def mutate(self):
        """
        Method to randomly mutate all of the children by editing a single weight.
        """
        for child in self.children.values():
            child.mutate()

    def select(self):
        """
        Method to select a child or parent solution based on performance to be the parent in the 
        next generation.
        """
        for idx, (parent, child) in enumerate(zip(self.parents.values(), self.children.values())):
            # In this case, lower values correspond to better fitness
            if child.fitness < parent.fitness:
                self.parents[idx] = child

    def show_best(self):
        """
        Method to show the best solution after the simulation has completed.
        """
        # Get the parent with the "best" (lowest) fitness value, starting with the first one
        best: Solution = min(self.parents.values(), key=lambda parent: parent.fitness)
        best.start_simulation('GUI')

    def print(self):
        """
        Method to print the fitness values for all child/parent solutions.
        """
        print(f'\nFitness')
        for idx, (parent, child) in enumerate(zip(self.parents.values(), self.children.values())):
            print(f'Parent {idx}: {parent.fitness}\t Child {idx}: {child.fitness}')