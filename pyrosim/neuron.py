import math

import pybullet

import pyrosim.pyrosim as pyrosim

import pyrosim.constants as c

from pyrosim.synapse import SYNAPSE

class NEURON: 

    def __init__(self,line):

        self.Determine_Name(line)

        self.Determine_Type(line)

        self.Search_For_Link_Name(line)

        self.Search_For_Joint_Name(line)

        self.Set_Value(0.0)

    def Add_To_Value( self, value ):

        self.Set_Value( self.Get_Value() + value )

    def Get_Joint_Name(self):

        return self.jointName

    def Get_Link_Name(self):

        return self.linkName

    def Get_Name(self):

        return self.name

    def Get_Value(self):

        return self.value

    def Is_Sensor_Neuron(self):

        return self.type == c.SENSOR_NEURON

    def Is_Hidden_Neuron(self):

        return self.type == c.HIDDEN_NEURON

    def Is_Motor_Neuron(self):

        return self.type == c.MOTOR_NEURON

    def Print(self):

        # self.Print_Name()

        # self.Print_Type()

        self.Print_Value()

        # print("")

    def Set_Value(self,value):

        self.value = value

    # Methods for updating sensor and motor neurons respectively
    
    def Update_Sensor_Neuron(self):
        neuron_value: float = pyrosim.Get_Touch_Sensor_Value_For_Link(self.Get_Link_Name())
        self.Set_Value(neuron_value)

    def Update_Hidden_Or_Motor_Neuron(self, neurons: dict[str: ...], synapses: dict[str: SYNAPSE]):
        """
        Method for updating a hidden or motor neuron. Requires access to other parts of the neural network.

        :param neurons: Dictionary containing all the neuron names mapped to neuron objects.
        :param synapses: Dictionary mapping tuples with the source/sink neuron to the synapse object.
        """
        # Initialize value to 0
        self.Set_Value(0)
        # Compute weighted sum
        for presynaptic_neuron, postsynaptic_neuron in synapses.keys():
            # Check if the current neuron is the postsynaptic neuron
            if postsynaptic_neuron == self.Get_Name():
                neuron_weight: float = neurons.get(presynaptic_neuron).Get_Value()
                synapse_weight: float = synapses.get((presynaptic_neuron, postsynaptic_neuron)).Get_Weight()
                self.Allow_Presynaptic_Neuron_To_Influence_Me(neuron_weight, synapse_weight)
        self.Threshold()
        

    def Allow_Presynaptic_Neuron_To_Influence_Me(self, neuron_value: float, synapse_weight: float):
        """
        Method to add the result of multiplying the presynaptic neuron value with the synapse weight.

        :param neuron_value:   Value of the presynaptic neuron connected to the current neuron via a synapse.
        :param synapse_weight: Weight of the synapse connecting the presynaptic neuron to the current one.
        """
        self.Add_To_Value(neuron_value * synapse_weight)


# -------------------------- Private methods -------------------------

    def Determine_Name(self,line):

        if "name" in line:

            splitLine = line.split('"')

            self.name = splitLine[1]

    def Determine_Type(self,line):

        if "sensor" in line:

            self.type = c.SENSOR_NEURON

        elif "motor" in line:

            self.type = c.MOTOR_NEURON

        else:

            self.type = c.HIDDEN_NEURON

    def Print_Name(self):

       print(self.name)

    def Print_Type(self):

       print(self.type)

    def Print_Value(self):

       print(self.value , " " , end="" )

    def Search_For_Joint_Name(self,line):

        if "jointName" in line:

            splitLine = line.split('"')

            self.jointName = splitLine[5]

    def Search_For_Link_Name(self,line):

        if "linkName" in line:

            splitLine = line.split('"')

            self.linkName = splitLine[5]

    def Threshold(self):

        self.value = math.tanh(self.value)
