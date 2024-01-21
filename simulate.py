"""
simulate.py
File to perform physics engine simulations in for Evolutionary Robotics using pybullet.

Author: Jordan Bourdeau
Date: 1/20/24
"""

import pybullet as p
import time

physicsClient = p.connect(p.GUI)

p.loadSDF("box.sdf")
for i in range(1000):
    p.stepSimulation()
    time.sleep(1/60)
    print(i)
p.disconnect()