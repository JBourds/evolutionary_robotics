"""
sensor.py
File containing the sensor class used by robots in the simulation.

Author: Jordan Bourdeau
Last Modified: 2/25/24
"""

import numpy as np
import pyrosim.pyrosim as pyrosim

class Sensor:

    def __init__(self, link_name: str, simulation_steps: int):
        """
        Class representing a sensor in the robotics simulation.

        :param link_name:           The string corresponding to the name of the link in Pyrosim.
        :param simulation_steps:    The total number of simulation steps. Used to initialize the array.

        # Class Fields:
            * `link_name`: The name of the link being sensed.
            * `values`:    The array of sensor values (size 'N') at each simulation timestep.
        """
        self.link_name: str = link_name
        self.values: np.array = np.zeros(simulation_steps)

    def get_value(self, time_step: int) -> float:
        """
        Method to retrieve the sensor value at the specified timestep and store/return it.
        Must be within valid indices of the `values` array.

        :param time_step: The integer value for the time step (index) to retrieve the value for.

        :returns: Returns the retrieves value.
        """

        # Assert it is a valid timestep
        assert 0 <= time_step < len(self.values), f'Invalid timestep for array of length {len(self.values)}.'

        self.values[time_step] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.link_name)

        return self.values[time_step]
    
    def save_values(self, file_path: str):
        """
        Method used to save the sensor values to a file.

        :param file_path: The file path to save sensor values to.
        """
        np.save(file_path, self.values)