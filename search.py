"""
search.py

Program to alternately generate and simulate robots with different synaptic weights.

Author: Jordan Bourdeau
Date Created: 3/3/24
"""

import os

import constants as c
from hillclimber import HillClimber

# for _ in range(c.NUM_SIMULATIONS):
#     os.system(c.GENERATE)
#     os.system(c.SIMULATE)

hill_climber: HillClimber = HillClimber()
hill_climber.evolve()