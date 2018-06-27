import matplotlib.pyplot as plt
import numpy as np
import os
from mpl_toolkits.mplot3d import Axes3D

BASE_DIR = os.path.dirname(__file__)


def _get_full_model_points(filename=os.path.join(BASE_DIR, '../data/face_68_model.txt')):
    """Get all 68 3D model points from file"""
    raw_value = []
    with open(filename) as file:
        for line in file:
            raw_value.append(line)
    model_points = np.array(raw_value, dtype=np.float32)
    model_points = np.reshape(model_points, (3, -1)).T
    # model_points *= 4
    # model_points[:, -1] *= -1

    return model_points


def draw_3d_points(_3d_points):
    fig = plt.figure()
    # ax = fig.add_subplot(111, projection='3d')
    ax = Axes3D(fig)
    # For each set of style and range settings, plot n random points in the box
    # defined by x in [23, 32], y in [0, 100], z in [zlow, zhigh].
    for x, y, z in _3d_points:
        print(x, y, z)
        ax.scatter(x, y, z)

    # for c, m, zlow, zhigh in [('r', 'o', -50, -25), ('b', '^', -30, -5)]:
    #     xs = randrange(n, 23, 32)
    #     ys = randrange(n, 0, 100)
    #     zs = randrange(n, zlow, zhigh)
    #     ax.scatter(xs, ys, zs, c=c, marker=m)

    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')

    plt.show()


def draw_2d_points(_2d_points):
    fig = plt.figure()
    ax = fig.add_subplot(111, aspect='equal')
    ax.cla()
    for x, y in _2d_points:
        ax.add_artist(plt.Circle((x, y), 0.2, color='r'))
    plt.show()


if __name__ == '__main__':
    # points = [[0, 0, 0], [0, 1, 0], [1, 0, 0], [0, 0, 1]]
    points = _get_full_model_points()
    # points = [
    #     (0.0, 0.0, 0.0),  # Nose tip
    #     (0.0, -330.0, -65.0),  # Chin
    #     (-225.0, 170.0, -135.0),  # Left eye left corner
    #     (225.0, 170.0, -135.0),  # Right eye right corne
    #     (-150.0, -150.0, -125.0),  # Left Mouth corner
    #     (150.0, -150.0, -125.0)  # Right mouth corner
    #
    # ]
    print(points)
    # print(len(points))
    # points = [
    #     (0.0, 0.0, 0.0),  # Nose tip
    #     (0.0, -330.0, -65.0),  # Chin
    #     (-225.0, 170.0, -135.0),  # Left eye left corner
    #     (225.0, 170.0, -135.0),  # Right eye right corne
    #     (-150.0, -150.0, -125.0),  # Left Mouth corner
    #     (150.0, -150.0, -125.0)  # Right mouth corner
    #
    # ]
    draw_3d_points(points)
    # draw_2d_points([[1, 1], [10, 10]])
