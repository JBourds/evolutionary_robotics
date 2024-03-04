"""
Solution.py

Class definition for a Solution which stores synaptic weights for a robot controller

Author: Jordan Bourdeau
Date Created: 3/3/24
"""

import numpy as np
import os
import pyrosim.pyrosim as pyrosim
import random
import time

import constants as c

class Solution:
    
    def __init__(self, id: int):
        """
        Class representing a candidate solution with synaptic weights.
        Neural network is derived from sensor/motor neurons in `constants.py`.

        :param id: Unique integer identifer for the solution.

        # Fields:
            * `id`:      Unique identifier used to refer to solution and avoid file locks.
            * `weights`: Numpy array containing all the synaptic weights for the neural network.
            * `fitness`: Floating point fitness value for a candidate solution.
        """
        self.id: int = id
        num_sensors: int = len(c.SENSOR_NEURONS)
        num_motors: int = len(c.MOTOR_NEURONS)
        self.weights: np.array = 2 * np.random.rand(num_sensors, num_motors) - 1
        self.fitness: float = 0

    def set_id(self, id: int):
        """
        Setter for the ID. Used when a parent is deepcopied to differentiate the child.

        :param id:  New ID for the Solution object.
        """
        self.id = id

    def start_simulation(self, mode: str):
        """
        Method to start the simulation for a candidate solution.

        :param mode: The mode to run in (DIRECT or GUI).
        """
        self.create_world()
        self.generate_body()
        self.generate_brain()
        os.system(f'{c.SIMULATE} {mode} {self.id} &')

    def wait_for_simulation_to_end(self):
        """
        Method to block until a simulation ends and the fitness value can be retrieved.
        """
        fitness_file: str = c.get_fitness_file(self.id)
        while not os.path.exists(fitness_file):
            time.sleep(0.01)
        with open(fitness_file, 'r') as file:
            self.fitness = float(file.read())
        c.delete_fitness_file(self.id)

    def mutate(self):
        """
        Method used to randomly mutate one of the synaptic weights of a solution.
        """
        num_rows, num_cols = self.weights.shape
        row_idx: int = random.randint(0, num_rows - 1)
        col_idx: int = random.randint(0, num_cols - 1)
        self.weights[row_idx, col_idx] = 2 * random.random() - 1

    def create_world(self):
        """
        Method to create the world using predefined parameters.
        """
        # Block Position
        x1: float = 0
        y1: float = 0
        z1: float = 0.5

        pyrosim.Start_SDF(c.WORLD_FILE)
        pyrosim.Send_Cube(name='Box', pos=[x1, y1, z1], size=[c.CUBE_LENGTH, c.CUBE_WIDTH, c.CUBE_HEIGHT])
        pyrosim.End()


    def generate_body(self):
        """
        Method to generate the robot body using predefined parameters.
        """
        pyrosim.Start_URDF(c.ROBOT_FILE)
        # Move it away from the world cube
        x2: float = 1.5
        y2: float = 1.5
        z2: float = 1.5

        # Absolute cube/joint positioning
        pyrosim.Send_Cube(name='Torso', pos=[x2, y2, z2], size=[c.CUBE_LENGTH, c.CUBE_WIDTH, c.CUBE_HEIGHT])
        pyrosim.Send_Joint(name='Torso_FrontLeg', parent='Torso', child='FrontLeg', type='revolute', position=[x2 - 0.5, y2, z2 - 0.5])
        
        # Relative link/joint positioning
        pyrosim.Send_Cube(name='FrontLeg', pos=[-0.5, 0, -0.5], size=[c.CUBE_LENGTH, c.CUBE_WIDTH, c.CUBE_HEIGHT])
        pyrosim.Send_Joint(name='Torso_BackLeg', parent='Torso', child='BackLeg', type='revolute', position=[x2 + 0.5, y2, z2 - 0.5])
        pyrosim.Send_Cube(name='BackLeg', pos=[0.5, 0, -0.5], size=[c.CUBE_LENGTH, c.CUBE_WIDTH, c.CUBE_HEIGHT])

        # End simulation
        pyrosim.End()

    def generate_brain(self):
        """
        Method to generate the neurons and synapses for the robot's controller.
        """
        brain_file: str = c.get_brain_file(self.id)
        pyrosim.Start_NeuralNetwork(brain_file)

        # Sensor Neurons
        pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
        pyrosim.Send_Sensor_Neuron(name=1, linkName="BackLeg")
        pyrosim.Send_Sensor_Neuron(name=2, linkName="FrontLeg")

        # Motor Neurons
        pyrosim.Send_Motor_Neuron(name=3, jointName="Torso_FrontLeg")
        pyrosim.Send_Motor_Neuron(name=4, jointName="Torso_BackLeg")

        # Create fully connected network from sensor neuron to motor neurons
        sensor_neurons: list = list(c.SENSOR_NEURONS.keys())
        motor_neurons: list = list(c.MOTOR_NEURONS.keys())
        for row_idx, sensor_neuron in enumerate(sensor_neurons):
            for col_idx, motor_neuron in enumerate(motor_neurons):
                weight: float = self.weights[row_idx, col_idx]
                pyrosim.Send_Synapse(sourceNeuronName=sensor_neuron, targetNeuronName=motor_neuron, weight=weight)

        # End simulation
        pyrosim.End()