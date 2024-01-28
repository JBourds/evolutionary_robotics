"""
simulate.py
File to perform physics engine simulations in for Evolutionary Robotics using pybullet.

Author: Jordan Bourdeau
Date: 1/20/24
"""

import pybullet as p
import pybullet_data
import time

# Create the GUI and simulation parameters
physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

# Create world and its parameters
p.setGravity(0, 0, -9.8)
plane_id = p.loadURDF("plane.urdf")
p.loadSDF("world.sdf")

# Load the robot into the world
robot_id = p.loadURDF("body.urdf")

# Run the simulation
for i in range(1000):
    p.stepSimulation()
    time.sleep(1/60)
    print(i)
p.disconnect()