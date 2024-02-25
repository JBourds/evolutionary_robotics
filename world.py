"""
world.py
File containing the world class used to manage the robotics somulation.

Author: Jordan Bourdeau
Last Modified: 2/25/24
"""

import pybullet as p

import constants as c

class World:

    def __init__(self):
        """
        Class representing the world being simulated in the physics engine.

        # Fields:
            * `plane_id`: The integer for the plane ID used in the simulation.
        """
        self.plane_id: int = p.loadURDF(c.PLANE_FILE)
        p.loadSDF(c.WORLD_FILE)