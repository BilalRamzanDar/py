# import matplotlib.pyplot as plt
# import numpy as np
#
# xpoints = np.array([0, 6])
# ypoints = np.array([0, 250])
#ma
# plt.plot(xpoints, ypoints)
# plt.show()


# import matplotlib.pyplot as plt
# import numpy as np
#
# xpoints = np.array([0, 6])
# ypoints = np.array([0, 250])
#
# plt.plot(xpoints, ypoints)
#
#
# xpoints = np.array([1, 8,12])
# ypoints = np.array([3, 10,18])
#
# plt.plot(xpoints, ypoints, 'o')
# plt.show()


# import matplotlib.pyplot as plt
# import numpy as np
#
# xpoints = np.array([1, 2, 6])
# ypoints = np.array([3, 8, 1, 10])
#
# plt.plot(xpoints, ypoints)
# plt.show()


# import matplotlib.pyplot as plt
# import numpy as np
# xpoints=np.array([2])
# ypoints = np.array([3, 8, 1, 10, 5, 7])
#
# plt.plot(ypoints)
# plt.show()


# import matplotlib.pyplot as plt
# import numpy as np
# xpoints=np.array([4,6,7,9])
# ypoints = np.array([3, 8, 1, 10])
#
#
# plt.plot(xpoints, linestyle = 'dotted')
# plt.plot(ypoints, linestyle = 'dotted')
#
# plt.show()



# import matplotlib.pyplot as plt
# import  numpy as np
#
# x=np.array([2,4,5,7,8])
# y=np.array([1,3,5,7,9])
#
# plt.plot(x,y)
# plt.xlabel('age')
# plt.ylabel('height')
# plt.show()


# import numpy as np
# import matplotlib.pyplot as plt
#
# x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
# y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
#
# plt.title("Sports Watch Data")
# plt.xlabel("Average Pulse")
# plt.ylabel("Calorie Burnage")
#
# plt.plot(x, y)
#
# plt.grid(linestyle='dotted')
#
# plt.show()





import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create a figure and a 3D axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
side_length=6
# Define the coordinates for the cube vertices
vertices = [
    [0, 0, 0],
    [6, 0, 0],
    [6, 6, 0],
    [0, 6, 0],
    [0, 0, 6],
    [6, 0, 6],
    [6, 6, 6],
    [0, 6, 6]
]

# Define the edges connecting the cube vertices
edges = [
    [0, 1],
    [1, 2],
    [2, 3],
    [3, 0],
    [4, 5],
    [5, 6],
    [6, 7],
    [7, 4],
    [0, 4],
    [1, 5],
    [2, 6],
    [3, 7]
]

# Plot the cube
for edge in edges:
    x = [vertices[edge[0]][0], vertices[edge[1]][0]]
    y = [vertices[edge[0]][1], vertices[edge[1]][1]]
    z = [vertices[edge[0]][2], vertices[edge[1]][2]]
    ax.plot(x, y, z, 'b')

# Set the limits of the plot
ax.set_xlim([0, side_length])
ax.set_ylim([0, side_length])
ax.set_zlim([0, side_length])

# Set labels for the axes
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Show the plot
plt.show()