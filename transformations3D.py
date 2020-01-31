import numpy as np
import math as m


def translation(matrix, tx, ty, tz):
    print('\nObject Matrix After Translation')
    trans_matrix = np.eye(4)
    trans_matrix[0, 3] = tx
    trans_matrix[1, 3] = ty
    trans_matrix[2, 3] = tz

    return trans_matrix @ matrix


def scaling(matrix, sx, sy, sz):
    print('\nObject Matrix After Scaling')
    scale_matrix = np.eye(4)
    scale_matrix[0, 0] = sx
    scale_matrix[1, 1] = sy
    scale_matrix[2, 2] = sz

    return scale_matrix @ matrix


def rotation(matrix, a, direction, axis):
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


def reflection():
    pass

def shearing():
    pass


v = int(input('Enter number of Vertices in the object : '))
obj_matrix = np.empty((4, v))

for i in range(0, v):
    obj_matrix[0, i] = float(input(f'\nEnter x co-ordinate of {i + 1} vertex of object : '))
    obj_matrix[1, i] = float(input(f'Enter y co-ordinate of {i + 1} vertex of object : '))
    obj_matrix[2, i] = float(input(f'Enter z co-ordinate of {i + 1} vertex of object : '))
    obj_matrix[3, i] = 1

print("\n\nHomogeneous Matrix of object's co-ordinates")
print(obj_matrix)

flag = True

while flag:
    print('\n\n-----Transformation-----')
    print('(1)Translation\n(2)Scaling\n(3)Rotation\n(4)Reflection\n(5)Shearing\n(6)Exit')
    option = int(input('\nWhich transformation do you want to perform : '))

    if option == 1:
        print('\n-----Translation-----')
        x = float(input('Enter translation length along x-axis : '))
        y = float(input('Enter translation length along y-axis : '))
        z = float(input('Enter translation length along z-axis : '))

        result = translation(obj_matrix, x, y, z)
        print(result)

    elif option == 2:
        print('\n-----Scaling-----')
        x = float(input('Enter Scaling factor along x-axis : '))
        y = float(input('Enter Scaling factor along y-axis : '))
        z = float(input('Enter Scaling factor along z-axis : '))

        result = scaling(obj_matrix, x, y, z)
        print(result)

    elif option == 3:
        print('\n-----Rotation-----')
        o = float(input('Enter Rotation Angle(in Degree) : '))
        d = int(input('Choose Direction of Rotation\n(1)Anticlockwise\n(2)Clockwise\n'))
        axis = int (input('Choose Axis for Rotation\n(1)x-axis\n(2)y-axis\n(3)z-axis\n'))

        result = rotation(obj_matrix, o, d, axis)
        print(result)

    elif option == 4:
        print('\n-----Reflection-----')

    elif option == 5:
        print('\n-----Shearing-----')

    elif option == 6:
        print('\nExit')
        flag = False
    else:
        print("\nChoose a Valid Option!")