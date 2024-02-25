"""
simulate.py
File to perform physics engine simulations in for Evolutionary Robotics using pybullet.

Author: Jordan Bourdeau
Date: 1/20/24
"""

import numpy as np
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import random
import time

from constants import BACK_LEG_FILE, BACK_TARGET_ANGLES, DATA_DIRECTORY, FRONT_LEG_FILE, FRONT_TARGET_ANGLES, PLANE_FILE, ROBOT_FILE, WORLD_FILE

# Create the GUI and simulation parameters
physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

# Create world and its parameters
p.setGravity(0, 0, -9.8)
plane_id = p.loadURDF(PLANE_FILE)
p.loadSDF(WORLD_FILE)

# Load the robot into the world
robot_id = p.loadURDF(ROBOT_FILE)

simulation_steps: int = 1_000

# Variables for controlling motor movement
front_amplitude: float = np.pi / 2
front_frequency: float = 10
front_phase_offset: float = 0
front_target_angles: np.array = front_amplitude * np.sin(front_frequency * np.linspace(0, 2 * np.pi, num=simulation_steps) + front_phase_offset)

back_amplitude: float = np.pi / 8
back_frequency: float = 10
back_phase_offset: float = 0
back_target_angles: np.array = back_amplitude * np.sin(back_frequency * np.linspace(0, 2 * np.pi, num=simulation_steps) + back_phase_offset)

# Run the simulation
back_leg_sensor_values = np.zeros(simulation_steps)
front_leg_sensor_values = np.zeros(simulation_steps)
pyrosim.Prepare_To_Simulate(robot_id)
for i in range(simulation_steps):
    back_leg_sensor_values[i] = pyrosim.Get_Touch_Sensor_Value_For_Link('BackLeg')
    front_leg_sensor_values[i] = pyrosim.Get_Touch_Sensor_Value_For_Link('FrontLeg')
    pyrosim.Set_Motor_For_Joint(
        bodyIndex = robot_id,
        jointName = b"Torso_FrontLeg",
        controlMode = p.POSITION_CONTROL,
        targetPosition = front_target_angles[i],
        maxForce = 25)
    pyrosim.Set_Motor_For_Joint(
        bodyIndex = robot_id,
        jointName = b"Torso_BackLeg",
        controlMode = p.POSITION_CONTROL,
        targetPosition = back_target_angles[i],
        maxForce = 25)
    p.stepSimulation()
    time.sleep(1/600)
p.disconnect()

np.save(f'{DATA_DIRECTORY}{FRONT_TARGET_ANGLES}', front_target_angles)
np.save(f'{DATA_DIRECTORY}{BACK_TARGET_ANGLES}', back_target_angles)
np.save(f'{DATA_DIRECTORY}{BACK_LEG_FILE}', back_leg_sensor_values)
np.save(f'{DATA_DIRECTORY}{FRONT_LEG_FILE}', front_leg_sensor_values)
