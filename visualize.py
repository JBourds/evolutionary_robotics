from matplotlib import pyplot as plt
import numpy as np

from constants import BACK_LEG_FILE, BACK_TARGET_ANGLES, DATA_DIRECTORY, FRONT_LEG_FILE, FRONT_TARGET_ANGLES

front_target_angles: np.array = np.load(f'{DATA_DIRECTORY}{FRONT_TARGET_ANGLES}')
back_target_angles: np.array = np.load(f'{DATA_DIRECTORY}{BACK_TARGET_ANGLES}')
back_leg_sensor_values: np.array = np.load(f'{DATA_DIRECTORY}{BACK_LEG_FILE}')
front_leg_sensor_values: np.array = np.load(f'{DATA_DIRECTORY}{FRONT_LEG_FILE}')

plt.figure(1)
plt.title('Target Angles')
plt.plot(front_target_angles, label='Front Target Angles', alpha=0.5, linewidth=3)
plt.plot(back_target_angles, label='Back Target Angles', alpha=0.5)
plt.legend()
plt.show()

plt.figure(2)
plt.plot(back_leg_sensor_values, label='Front Leg On the Ground', linewidth=2)
plt.plot(front_leg_sensor_values, label='Back Leg On the Ground')
plt.legend()
plt.show()
