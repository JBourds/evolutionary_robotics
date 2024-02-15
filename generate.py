import pyrosim.pyrosim as pyrosim

from constants import ROBOT_FILE, WORLD_FILE

# Cube Parameters
length: float = 1
width: float = 1
height: float = 1

# Block Position
x1: float = 0
y1: float = 0
z1: float = 0.5


def create_world():
    pyrosim.Start_SDF(WORLD_FILE)
    pyrosim.Send_Cube(name='Box', pos=[x1, y1, z1], size=[length, width, height])
    pyrosim.End()


def create_robot():
    pyrosim.Start_URDF(ROBOT_FILE)
    # Move it away from the world cube
    x2: float = 1.5
    y2: float = 1.5
    z2: float = 1.5

    # Absolute cube/joint positioning
    pyrosim.Send_Cube(name='Torso', pos=[x2, y2, z2], size=[length, width, height])
    pyrosim.Send_Joint(name='Torso_FrontLeg', parent='Torso', child='FrontLeg', type='revolute', position=[x2 - 0.5, y2, z2 - 0.5])
    # Relative link/joint positioning
    pyrosim.Send_Cube(name='FrontLeg', pos=[-0.5, 0, -0.5], size=[length, width, height])
    pyrosim.Send_Joint(name='Torso_BackLeg', parent='Torso', child='BackLeg', type='revolute', position=[x2 + 0.5, y2, z2 - 0.5])
    pyrosim.Send_Cube(name='BackLeg', pos=[0.5, 0, -0.5], size=[length, width, height])
    # End simulation
    pyrosim.End()


create_world()
create_robot()
