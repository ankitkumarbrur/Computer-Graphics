import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import math as m

def enterMatrix():
    n = int(input("Enter number of vertices : "))
    xpoints = np.empty(n)
    ypoints = np.empty(n)
    zpoints = np.empty(n)

    for i in range(n):
        xpoints[i], ypoints[i], zpoints[i] = map(int, input("Enter co-ordinates of point " + str(i + 1) + ": ").split())

    print(np.vstack((xpoints, ypoints, zpoints, np.ones(n))))
    return np.vstack((xpoints, ypoints, zpoints, np.ones(n)))

def draw(matrix1,matrix2):
    ax = plt.axes(projection='3d')
    if matrix1 is not None:
        x1 = np.append(matrix1[0],matrix1[0,0])
        y1 = np.append(matrix1[1],matrix1[1,0])
        z1 = np.append(matrix1[2],matrix1[2,0])
        ax.plot3D(x1, y1, z1)

    if matrix2 is not None:
        x1 = np.append(matrix2[0],matrix2[0,0])
        y1 = np.append(matrix2[1],matrix2[1,0])
        z1 = np.append(matrix2[2],matrix2[2,0])
        ax.plot3D(x1, y1, z1)

    plt.legend(['Original Object', 'Transformed Object'])
    plt.title('3D Transformation')
    plt.show()

def translation(matrix):
    if matrix is None:
        raise Exception("Create an object first!!!")
    dx = int(input("Enter translation factor along x-axis: "))
    dy = int(input("Enter translation factor along y-axis: "))
    dz = int(input("Enter translation factor along z-axis: "))
    T = np.eye(4)
    print(T)
    T[0, 3] = dx
    T[1, 3] = dy
    T[2, 3] = dz
    print(T)
    return T @ matrix

def scaling(matrix):
    if matrix is None:
        raise Exception("Create an object first!!!")
    dx = int(input("Enter scaling factor along x-axis: "))
    dy = int(input("Enter scaling factor along y-axis: "))
    dz = int(input("Enter scaling factor along z-axis: "))
    T = np.diag((dx,dy,dz,1.0))
    print(T)
    return T @ matrix

def rotation(matrix):
    a = float(input('Enter Rotation Angle(in Degree) : '))
    direction = int(input('Choose Direction of Rotation\n(1)Anticlockwise\n(2)Clockwise\n'))
    axis = int (input('Choose Axis for Rotation\n(1)x-axis\n(2)y-axis\n(3)z-axis\n'))

    rotation_matrix = np.eye(4)
    r = m.radians(a)
    s = m.sin(r)
    c = m.cos(r)

    if axis == 1:
        if direction == 1:
            rotation_matrix[0, :2] = c, -s
            rotation_matrix[1, :2] = s, c
        elif direction == 2:
            rotation_matrix[0, :2] = c, s
            rotation_matrix[1, :2] = -s, c
        else:
            return '\nPlease Choose A Valid Direction For Rotation'

    elif axis == 2:
        if direction == 1:
            rotation_matrix[1, 1:3] = c, -s
            rotation_matrix[2, 1:3] = s, c
        elif direction == 2:
            rotation_matrix[1, 1:3] = c, s
            rotation_matrix[2, 1:3] = -s, c
        else:
            return '\nPlease Choose A Valid Direction For Rotation'

    elif axis == 3:
        if direction == 1:
            rotation_matrix[0, ::2] = c, -s
            rotation_matrix[2, ::2] = s, c
        elif direction == 2:
            rotation_matrix[0, ::2] = c, s
            rotation_matrix[2, ::2] = -s, c
        else:
            return '\nPlease Choose A Valid Direction For Rotation'

    else:
        return '\nPlease Choose A Valid Axis for Rotation'
    
    print('\nObject Matrix After Rotation')
    return rotation_matrix @ matrix

def reflection(matrix):
    pass



matrix = None
matrix_2 = None
flag = False

while not flag :
    print('\n\n', '-'*40, 'transformations' , '-'*40)
    print('0. Exit')
    print('1. Enter a new object')
    print('2. Translate object')
    print('3. Scale Object')
    print('4. Rotate Object')
    print('5. Reflect Object')
    option = input("Select an option : ")

    if option == '0':
        flag = True

    elif option == '1':
        matrix = enterMatrix()
        draw(matrix,None)

    elif option == '2':
        matrix_2 = translation(matrix)
        draw(matrix,matrix_2)
        print('='*90)

    elif option == '3':
        matrix_2 = scaling(matrix)
        draw(matrix,matrix_2)

    elif option == '4':
        matrix_2 = rotation(matrix)
        draw(matrix, matrix_2)
    
    elif option == '5':
        matrix_2 = reflection(matrix)
        draw(matrix, matrix_2)
    
    else:
        print("Enter a valid choice!!")
