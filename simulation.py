"""
simulation.py
File containing the simulation class used to manage the robotics somulation.

Author: Jordan Bourdeau
Last Modified: 2/25/24
"""

import numpy as np
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import time

import constants as c
from robot import Robot
from world import World

class Simulation:

    def __init__(self):
        """
        Class responsible for running the Pyrosim simulation

        # Fields:
            * `physics_engine`: The pybullet physics engine being used.
            * `world`:          The simulation world being used.
            * `robot`:          The robot being simulated.
        """
        self.physics_engine = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0, 0, c.GRAVITY)

        self.world: World = World()
        self.robot: Robot = Robot(c.ROBOT_FILE, c.BRAIN_FILE)

        # Initialize robot
        pyrosim.Prepare_To_Simulate(self.robot.id)

        # Initialize the robot's sensors and motors
        self.robot.prepare_to_sense()
        self.robot.prepare_to_act()

    def __del__(self):
        """
        Destructor which disconnects from the physics engine.
        """
        p.disconnect()

    def run(self):
        """
        Method to actually run the simulation.
        """
        for time_step in range(c.SIMULATION_STEPS):
            self.robot.sense(time_step)
            self.robot.think()
            self.robot.act()
            p.stepSimulation()
            time.sleep(c.TIMESTEP)
        p.disconnect()