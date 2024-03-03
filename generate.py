import pyrosim.pyrosim as pyrosim

import constants as c

# Cube Parameters
length: float = 1
width: float = 1
height: float = 1

# Block Position
x1: float = 0
y1: float = 0
z1: float = 0.5


def create_world():
    pyrosim.Start_SDF(c.WORLD_FILE)
    pyrosim.Send_Cube(name='Box', pos=[x1, y1, z1], size=[length, width, height])
    pyrosim.End()


def generate_body():
    pyrosim.Start_URDF(c.ROBOT_FILE)
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

def generate_brain():
    pyrosim.Start_NeuralNetwork(c.BRAIN_FILE)

    # Sensor Neurons
    pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
    pyrosim.Send_Sensor_Neuron(name=1, linkName="BackLeg")
    pyrosim.Send_Sensor_Neuron(name=2, linkName="FrontLeg")

    # Motor Neurons
    pyrosim.Send_Motor_Neuron(name=3, jointName="Torso_FrontLeg")
    pyrosim.Send_Motor_Neuron(name=4, jointName="Torso_BackLeg")

    # Synapses
    pyrosim.Send_Synapse(sourceNeuronName=1, targetNeuronName=3, weight=1)
    pyrosim.Send_Synapse(sourceNeuronName=2, targetNeuronName=3, weight=.5)

    pyrosim.Send_Synapse(sourceNeuronName=1, targetNeuronName=4, weight=2)
    pyrosim.Send_Synapse(sourceNeuronName=2, targetNeuronName=4, weight=1)

    # Best Weights
    # pyrosim.Send_Synapse(sourceNeuronName=1, targetNeuronName=3, weight=1)
    # pyrosim.Send_Synapse(sourceNeuronName=2, targetNeuronName=3, weight=-0.5)

    # pyrosim.Send_Synapse(sourceNeuronName=1, targetNeuronName=4, weight=-0.5)
    # pyrosim.Send_Synapse(sourceNeuronName=2, targetNeuronName=4, weight=0.25)

    # End simulation
    pyrosim.End()


def create_robot():
    ...


create_world()
generate_body()
generate_brain()
