"""
constants.py
File containing constants for simulating robotics.

Author: Jordan Bourdeau
Last Modified: 2/25/24
"""

import numpy as np

# Simulation parameters
GRAVITY: float = -9.8
SIMULATION_STEPS: int = 10_000
TIMESTEP: float = 1/600

# Robot parameters
FRONT_AMPLITUDE: float = np.pi / 6
FRONT_FREQUENCY: float = 10.0
FRONT_PHASE_OFFSET: float = np.pi / 4
FRONT_TARGET_ANGLES: np.array = FRONT_AMPLITUDE * np.sin(FRONT_FREQUENCY * np.linspace(0, 2 * np.pi, num=SIMULATION_STEPS) + FRONT_PHASE_OFFSET)
FRONT_MAX_FORCE: float = 20

# File input/output
PLANE_FILE: str = 'plane.urdf'
WORLD_FILE: str = 'world.sdf'
ROBOT_FILE: str = 'body.urdf'
BRAIN_FILE: str = 'brain.nndf'

DATA_DIRECTORY: str = 'data/'
FRONT_TARGET_ANGLES_FILE: str = f'{DATA_DIRECTORY}front_target_angles.npy'
BACK_TARGET_ANGLES_FILE: str = f'{DATA_DIRECTORY}back_target_angles.npy'
BACK_LEG_FILE: str = f'{DATA_DIRECTORY}back_leg_sensor_data.npy'
FRONT_LEG_FILE: str = f'{DATA_DIRECTORY}front_leg_sensor_data.npy'
