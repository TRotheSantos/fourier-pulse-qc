import numpy as np
from matplotlib import pyplot as plt
from src.utils.helpers import *

def plot_bloch_sphere(states):
    bloch_x = []
    bloch_y = []
    bloch_z = []

    for state in states:
        # Bloch coordinates: <sigma_x>, <sigma_y>, <sigma_z>
        bloch_x.append(np.real(state.expectation_value(SIGMA_X)))
        bloch_y.append(np.real(state.expectation_value(SIGMA_Y)))
        bloch_z.append(np.real(state.expectation_value(SIGMA_Z)))

    # final_state = states[-1]
    # print("Final state:", final_state)

    # Plot Bloch sphere trajectory
    fig = plt.figure(figsize=(8, 6))
    fig.suptitle("Keep in mind: The trajectories are usually curves", fontsize=12, color="red")

    ax = fig.add_subplot(111, projection='3d')

    # wireframe
    u = np.linspace(0, 2 * np.pi, 20)
    v = np.linspace(0, np.pi, 20)
    x = np.outer(np.cos(u), np.sin(v))
    y = np.outer(np.sin(u), np.sin(v))
    z = np.outer(np.ones(np.size(u)), np.cos(v))
    ax.plot_wireframe(x, y, z, color='gray', alpha=0.2)

    ax.plot(bloch_x, bloch_y, bloch_z, 'b-', label='Pulse trajectory')
    ax.scatter([bloch_x[0]], [bloch_y[0]], [bloch_z[0]], color='g', label='Initial (|0>)')
    ax.scatter([bloch_x[-1]], [bloch_y[-1]], [bloch_z[-1]], color='r', label='Final (|Ψ>)')

    # axes
    ax.set_xlabel('X (<σx>)')
    ax.set_ylabel('Y (<σy>)')
    ax.set_zlabel('Z (<σz>)')
    ax.set_title('Bloch Sphere Trajectory')
    ax.legend()

    # Set equal aspect ratio
    ax.set_box_aspect([1, 1, 1])
    plt.show()

    ax.view_init(elev=20, azim=45)

    return bloch_x, bloch_y, bloch_z

