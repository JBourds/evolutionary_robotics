"""
simulate.py
File to perform physics engine simulations in for Evolutionary Robotics using pybullet.

Author: Jordan Bourdeau
Last Modified: 2/25/24
"""

import sys

from simulation import Simulation

# Parse command line arguments
simulation_mode: str = sys.argv[1]
solution_id: int = sys.argv[2]

use_gui: bool = True if simulation_mode.lower() == 'gui' else False
simulation: Simulation = Simulation(solution_id, use_gui=use_gui)
simulation.run()
simulation.get_fitness()
