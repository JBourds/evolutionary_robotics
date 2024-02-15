from matplotlib import pyplot as plt
import numpy as np

from constants import BACK_LEG_FILE, DATA_DIRECTORY, FRONT_LEG_FILE

back_leg_sensor_values: np.ndarray = np.load(f'{DATA_DIRECTORY}{BACK_LEG_FILE}')
front_leg_sensor_values: np.ndarray = np.load(f'{DATA_DIRECTORY}{FRONT_LEG_FILE}')

plt.plot(back_leg_sensor_values, label='Front Leg On the Ground', linewidth=2)
plt.plot(front_leg_sensor_values, label='Back Leg On the Ground')
plt.legend()
plt.show()
