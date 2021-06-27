import matplotlib.pyplot as plt
# Astro Pi Proyect Space3 Team
# IES Granadilla de Abona
# 20/06/2021
# Objetive: Create a graph through a text file for Astro Pi's project
# V.1

import numpy as np
import argparse
import sys

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--sigma', default=100, type=float)
    args = parser.parse_args()
    sigma = args.sigma

    fig = plt.figure()
    ax0 = fig.add_subplot(111, projection='3d')

    f = open('./data01.csv','r')
    lines = f.readlines()
    data = []
    for line in lines[1:]:
        fields = line.split(',')
        data.append([float(i) for i in fields[1:4]])

    data = np.array(data)
    mad = np.std(data, 0)

    mask_shock_x = np.abs(data[:,0]) > sigma * mad[0]
    mask_shock_y = np.abs(data[:,1]) > sigma * mad[1]
    mask_shock_z = np.abs(data[:,2]) > sigma * mad[2]
    shocks = [i for i, x in enumerate(mask_shock_x & mask_shock_y & mask_shock_z) if x]

    shocks_x = [i for i, x in enumerate(mask_shock_x) if x]

    shocks = mask_shock_x & mask_shock_y & mask_shock_z
    ax0.scatter(data[:,0], data[:,1],data[:,2])
    ax0.scatter(data[shocks,0], data[shocks,1],data[shocks,2], marker='^', c='red')
#     ax0.scatter(data[mask_shock_x,0], data[mask_shock_x,1],data[mask_shock_x,2], marker='x', c='green')
#     ax0.scatter(data[mask_shock_y,0], data[mask_shock_y,1],data[mask_shock_y,2], marker='x', c='yellow')
#     ax0.scatter(data[mask_shock_z,0], data[mask_shock_z,1],data[mask_shock_z,2], marker='x', c='black')
    plt.show()

