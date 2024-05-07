import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create some sample data
x = [1, 2, 3, 4, 5]
y = [5, 4, 3, 2, 1]
z = [0, 0, 0, 0, 0]

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Scatter plot
ax.scatter(x, y, z, c='r', marker='o')

# Set labels
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

# Show the plot
plt.show()
