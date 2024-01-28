import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF('boxes.sdf')

# Cube Parameters
length: float = 1
width: float = 1
height: float = 1

# Block Position
x1: float = 0
y1: float = 0
z1: float = 0.5

height_adjustment: float = 0
for i in range(10):
    scalar: float = 0.9 ** i
    for row_idx in range(5):
        for col_idx in range(5):
            pyrosim.Send_Cube(name=f"Box_{row_idx}_{col_idx}",
                              pos=[x1 + row_idx * width, y1 + col_idx * length, z1 + i * height],
                              size=[length * scalar, width * scalar, height * scalar])

pyrosim.End()
