import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def draw_3d_points(_3d_points):
    fig = plt.figure()
    # ax = fig.add_subplot(111, projection='3d')
    ax = Axes3D(fig)
    for x, y, z in _3d_points:
        print(x, y, z)
        ax.scatter(x, y, z)

    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')

    plt.show()


if __name__ == '__main__':
    points = [(25.0, 0, 0), (0, 25.0, 0), (0, 0, 25.0), (0, 0, 0)]
    draw_3d_points(points)
