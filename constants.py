"""
constants.py
File containing constants for simulating robotics.

Author: Jordan Bourdeau
Last Modified: 2/25/24
"""

import numpy as np

# Automating search
NUM_SIMULATIONS: int = 5
PYTHON: str = 'python'
GENERATE: str = f'{PYTHON} generate.py'
SIMULATE: str = f'{PYTHON} simulate.py'

# Simulation parameters
GRAVITY: float = -9.8
SIMULATION_STEPS: int = 1_000
TIMESTEP: float = 1/6000

# Robot parameters
FRONT_AMPLITUDE: float = np.pi / 6
FRONT_FREQUENCY: float = 10.0
FRONT_PHASE_OFFSET: float = np.pi / 4
FRONT_TARGET_ANGLES: np.array = FRONT_AMPLITUDE * np.sin(FRONT_FREQUENCY * np.linspace(0, 2 * np.pi, num=SIMULATION_STEPS) + FRONT_PHASE_OFFSET)
FRONT_MAX_FORCE: float = 20

SENSOR_NEURONS: dict[int: str] = {
    0: 'Torso',
    1: 'BackLeg',
    2: 'FrontLeg',
}

MOTOR_NEURONS: dict[int: str] = {
    3: 'Torso_FrontLeg',
    4: 'Torso_BackLeg',
}

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
