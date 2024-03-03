"""
robot.py
File containing the robot class used to manage the robotics somulation.

Author: Jordan Bourdeau
Last Modified: 2/25/24
"""

import pybullet as p
import pyrosim.pyrosim as pyrosim
from pyrosim.neuralNetwork import NEURAL_NETWORK

import constants as c
from motor import Motor
from sensor import Sensor

class Robot:
    
    def __init__(self, body_file: str, brain_file: str):
        """
        Class representing a robot in the simulation.

        # Fields:
            * `sensors`: Dictionary mapping sensor names to corresponding objects.
            * `motors`:  Dictionary mapping motor names to corresponding objects.
            * `id`:      ID the robot is categorized as in the simulation.
        """
        self.sensors: dict[str: Sensor] = {}
        self.motors: dict[str: Motor] = {}
        self.id: int = p.loadURDF(body_file)
        self.nn: NEURAL_NETWORK = NEURAL_NETWORK(brain_file)

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
            joint_names: list[str] = [joint_name.decode('ASCII') for joint_name in pyrosim.jointNamesToIndices]
            self.motors = {
                joint_name: Motor(joint_name, 
                                c.FRONT_AMPLITUDE, 
                                c.FRONT_FREQUENCY if joint_name == b'Torso_FrontLeg' else c.FRONT_FREQUENCY / 2, 
                                c.FRONT_PHASE_OFFSET,
                                c.FRONT_MAX_FORCE,
                                c.SIMULATION_STEPS)
                for joint_name in joint_names
            }
        else: 
            self.motors = motors

    def act(self):
        """
        Method which is responsible for activating the robot's motors at a specific time step.
        """
        for neuron_name in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuron_name):
                joint_name: str = self.nn.Get_Motor_Neuron_Joint(neuron_name)
                desired_angle: float = self.nn.Get_Value_Of(neuron_name)
                motor: Motor = self.motors.get(joint_name)
                motor.set_value(self.id, desired_angle) 

    def think(self):
        """
        Method responsible for activating the robot's neural network sensor/motor neurons.
        """
        self.nn.Update()
        self.nn.Print()