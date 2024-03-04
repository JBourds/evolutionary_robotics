"""
search.py

Program to alternately generate and simulate robots with different synaptic weights.

Author: Jordan Bourdeau
Date Created: 3/3/24
"""

import os

import constants as c
from parallel_hillclimber import ParallelHillClimber

parallel_hill_climber: ParallelHillClimber = ParallelHillClimber()
parallel_hill_climber.evolve()
parallel_hill_climber.show_best()