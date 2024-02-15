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
import time

from constants import BACK_LEG_FILE, DATA_DIRECTORY, FRONT_LEG_FILE, PLANE_FILE, ROBOT_FILE, WORLD_FILE

# Create the GUI and simulation parameters
physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

# Create world and its parameters
p.setGravity(0, 0, -9.8)
plane_id = p.loadURDF(PLANE_FILE)
p.loadSDF(WORLD_FILE)

# Load the robot into the world
robot_id = p.loadURDF(ROBOT_FILE)



# Run the simulation
backLegSensorValues = np.zeros(1000)
frontLegSensorValues = np.zeros(1000)
pyrosim.Prepare_To_Simulate(robot_id)
for i in range(1000):
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link('BackLeg')
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link('FrontLeg')
    pyrosim.Set_Motor_For_Joint(
        bodyIndex = robot_id,
        jointName = b"Torso_BackLeg",
        controlMode = p.POSITION_CONTROL,
        targetPosition = 0.0,
        maxForce = 500)
    p.stepSimulation()
    time.sleep(1/60)
p.disconnect()

np.save(f'{DATA_DIRECTORY}{BACK_LEG_FILE}', backLegSensorValues)
np.save(f'{DATA_DIRECTORY}{FRONT_LEG_FILE}', frontLegSensorValues)
