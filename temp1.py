import numpy as np
import pyny3d.geoms as pyny

polygon = np.array([[0,0,0], [7,0,0], [7,10,2], [0,10,2]])

pyny.Polygon(polygon)


pyny.Polygon.verify = False

pyny.Polygon(polygon)

pyny.Polygon.verify = True

surface_poly = [np.array([[0,0,0], [7,0,0], [7,10,2], [0,10,2]]),
                np.array([[0,10,2], [7,10,2], [3,15,3.5]]),
                np.array([[0,10,2], [3,15,3.5], [0,15,3.5]]),
                np.array([[7,10,2], [15,10,2], [15,15,3.5], [3,15,3.5]])]

pyny.Place(surface_poly)

pyny.Polygon.verify = False

pyny.Place(surface_poly)
polygon = pyny.Polygon(np.array([[0,0,0], [7,0,0], [7,10,2], [0,10,2]]))
polygon.get_parametric(True, tolerance=0.01)
array([0, 14, -70, 0])

non_polygon = pyny.Polygon(np.array([[0,0,-99], [7,0,0], [7,10,2], [0,10,2]]))
non_polygon.get_parametric(True, tolerance=0.01)
# ValueError: Polygon not plane:
# [[0  0 -99]
#  [7  0  0]
#  [7 10  2]
#  [0 10  2]]

import matplotlib.pyplot as plt
polygon = pyny.Polygon(np.array([[0,0,0], [5,0,0], [2.5,2.5,99]]))
polygon.plot2d()

polygon.to_2d().plot2d()
plt.axis('equal')

points = np.array([[0, 0], [2, -0.1], [2, 2], [5, 5], [5.1, 0]])

polygon.get_path().contains_points(points, radius=0.001)
array([True, False, True, False, False], dtype=bool)

polygon.contains(points, True)
array([True, False, True, False, False], dtype=bool)