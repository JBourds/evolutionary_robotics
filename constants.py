"""
constants.py
File containing constants for simulating robotics.

Author: Jordan Bourdeau
Last Modified: 2/25/24
"""

import numpy as np
import os

# Automating search
NUMBER_OF_GENERATIONS: int = 10
POPULATION_SIZE: int = 10
PYTHON: str = 'python'
GENERATE: str = f'{PYTHON} generate.py'
SIMULATE: str = f'{PYTHON} simulate.py'

# Simulation parameters
GRAVITY: float = -9.8
SIMULATION_STEPS: int = 10_000
TIMESTEP: float = 1/6000

# Cube parameters
CUBE_LENGTH: float = 1
CUBE_WIDTH: float = 1
CUBE_HEIGHT: float = 1

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
DATA_DIRECTORY: str = 'data/'
PLANE_FILE: str = f'plane.urdf'
WORLD_FILE: str = f'{DATA_DIRECTORY}world.sdf'
ROBOT_FILE: str = f'{DATA_DIRECTORY}body.urdf'

def get_brain_file(solution_id: int) -> str:
    """
    Function used to get the correct brain file based on a solution ID.

    :param solution_id: Integer value corresponding to the solution ID.

    :returns: String for the directory location with the neural network file.
    """
    brain_file: str = f'{DATA_DIRECTORY}brain_{solution_id}.nndf'
    return brain_file

def delete_brain_file(solution_id: int):
    """
    Function used to delete a brain file after it has been used.

    :param solution_id: Integer value corresponding to the solution ID.
    """
    try:
        os.remove(f'{DATA_DIRECTORY}brain_{solution_id}.nndf')
    except Exception as e:
        print(e)

def delete_all_brain_files():
    """
    Function used to delete any remnant brain files in the data directory.
    """
    os.system(f'rm {DATA_DIRECTORY}brain*.nndf >/dev/null 2>&1')

def get_fitness_file(solution_id: int) -> str:
    """
    Function used to get the correct fitness file based on a solution ID.

    :param solution_id: Integer value corresponding to the solution ID.

    :returns: String for the directory location with the neural network file.
    """
    fitness_file: str = f'{DATA_DIRECTORY}fitness_{solution_id}.txt'
    return fitness_file

def delete_fitness_file(solution_id: int):
    """
    Function used to delete a fitness file after it has been used.

    :param solution_id: Integer value corresponding to the solution ID.
    """
    try:
        os.remove(f'{DATA_DIRECTORY}fitness_{solution_id}.txt')
    except Exception as e:
        print(e)

def delete_all_fitness_files():
    """
    Function used to delete any remnant fitness files in the data directory.
    """
    os.system(f'rm {DATA_DIRECTORY}fitness*.nndf >/dev/null 2>&1')
