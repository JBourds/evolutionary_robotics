"""
robot.py
File containing the robot class used to manage the robotics somulation.

Author: Jordan Bourdeau
Last Modified: 2/25/24
"""

import pybullet as p
import pyrosim.pyrosim as pyrosim

import constants as c
from motor import Motor
from sensor import Sensor

class Robot:
    
    def __init__(self):
        """
        Class representing a robot in the simulation.

        # Fields:
            * `sensors`: Dictionary mapping sensor names to corresponding objects.
            * `motors`:  Dictionary mapping motor names to corresponding objects.
            * `id`:      ID the robot is categorized as in the simulation.
        """
        self.sensors: dict[str: Sensor] = {}
        self.motors: dict[str: Motor] = {}
        self.id: int = p.loadURDF(c.ROBOT_FILE)

    def prepare_to_sense(self):
        """
        Method to load in all the sensors from Pyrosim.
        """
        self.sensors = {link_name: Sensor(link_name, c.SIMULATION_STEPS) for link_name in pyrosim.linkNamesToIndices}

    def sense(self, time_step: int):
        """
        Method which retrieves sensor values for all the robot's sensors at a time step.

        :param time_step: The integer value for the time step/index to retrieve a value for.
                          Must be a valid index for all sensors (within specified simulation steps).
        """
        for sensor_name, sensor in self.sensors.items():
            sensor.get_value(time_step)

    def prepare_to_act(self, motors: dict[str: Motor] = None):
        """
        Method to load in all the motors from Pyrosim.
        """
        if motors is None:
            self.motors = {
                joint_name: Motor(joint_name, 
                                c.FRONT_AMPLITUDE, 
                                c.FRONT_FREQUENCY if joint_name == b'Torso_FrontLeg' else c.FRONT_FREQUENCY / 2, 
                                c.FRONT_PHASE_OFFSET,
                                c.FRONT_MAX_FORCE,
                                c.SIMULATION_STEPS)
                for joint_name in pyrosim.jointNamesToIndices
            }
        else: 
            self.motors = motors

    def act(self, time_step: int):
        """
        Method which is responsible for activating the robot's motors at a specific time step.

        :param time_step: Integer value corresponding to the time step/index used by the motors.
        """
        for motor_name, motor in self.motors.items():
            motor.set_value(self.id, time_step)