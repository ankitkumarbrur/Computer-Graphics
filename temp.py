from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import matplotlib.pyplot as plt

fig = plt.figure()
ax = Axes3D(fig)

x = [0,4,4,0,0,0,4,4]
y = [0,0,4,4,4,0,0,4]
z = [0,0,0,0,4,4,4,4]


ax.plot3D(x, y, z)
plt.show()