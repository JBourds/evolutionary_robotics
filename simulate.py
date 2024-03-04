"""
simulate.py
File to perform physics engine simulations in for Evolutionary Robotics using pybullet.

Author: Jordan Bourdeau
Last Modified: 2/25/24
"""

import sys

from simulation import Simulation

simulation_mode: str = sys.argv[1]
use_gui: bool = True if simulation_mode.lower() == 'gui' else False

simulation: Simulation = Simulation(use_gui=use_gui)
simulation.run()
simulation.get_fitness()

# np.save(c.FRONT_TARGET_ANGLES_FILE, c.FRONT_TARGET_ANGLES)
# np.save(c.BACK_TARGET_ANGLES_FILE, c.BACK_TARGET_ANGLES)
# np.save(c.BACK_LEG_FILE, back_leg_sensor_values)
# np.save(c.FRONT_LEG_FILE, front_leg_sensor_values)
