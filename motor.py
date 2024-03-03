"""
motor.py
File containing the motor class used by robots in the simulation.

Author: Jordan Bourdeau
Last Modified: 2/25/24
"""

import numpy as np
import pybullet as p
import pyrosim.pyrosim as pyrosim

class Motor:

    def __init__(self, joint_name: str, amplitude: float, frequency: float, offset: float, max_force: float, simulation_steps: int):
        """
        Class representing a motor in the robotics simulation.

        :param joint_name:       The string corresponding to the name of the joint in Pyrosim.
        :param amplitude:        The total amplitude of the generated sin wave.
        :param frequency:        The frequency of the generated sin wave.
        :param offset:           The offset of the generated sin wave.
        :param max_force:        The maximum force which the robot can produce.
        :param simulation_Steps: The number of simulation steps to be taken.

        # Class Fields:
            * `joint_name`:   The name of the joint being sensed.
            .
            .
            .
            .
            * `motor_values`: The values generated for the motor at each of the given timesteps.
        """
        self.joint_name: str = joint_name
        self.amplitude: float = amplitude
        self.frequency: float = frequency
        self.offset: float = offset
        self.max_force: float = max_force
        self.motor_values: np.array = amplitude * np.sin(frequency * np.linspace(0, 2 * np.pi, num=simulation_steps) + offset)

    def set_value(self, robot_id: int, desired_angle: float) -> float:
        """
        Set the value for a joint's motor at a given timestep given the robot ID (don't need full Robot object).

        :param robot_id:      Integer value corresponding to the robot ID the motor is for
        :param desired_angle: The angle which is used to control the motor's movement.

        :returns: Motor value at time step.
        """
       
        pyrosim.Set_Motor_For_Joint(
                bodyIndex = robot_id,
                jointName = self.joint_name,
                controlMode = p.POSITION_CONTROL,
                targetPosition = desired_angle,
                maxForce = self.max_force)
        
        return desired_angle
