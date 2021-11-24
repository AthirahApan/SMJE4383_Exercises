import numpy as np
import laspy as lp
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

input_path="/home/athirah/Desktop/SMJE4383_Exercises/assign1/"
dataname="Ngombak.las"
output_path="Output/"
point_cloud = lp.file.File(input_path+dataname, mode="r")

points = np.vstack((point_cloud.x, point_cloud.y, point_cloud.z)).transpose()
colors = np.vstack((point_cloud.red, point_cloud.green, point_cloud.blue)).transpose()

factor=160
decimated_points= points[::factor]

decimated_colors = colors[::factor]
ax = plt.axes(projection='3d')
ax.scatter(decimated_points[:,0], decimated_points[:,1], decimated_points[:,2], c = decimated_colors/65535, s=0.01)

plt.show()

#np.savetxt(output_path+dataname+"_voxel-best_point_%s.poux" % (voxel_size), grid_candidate_center, delimiter=";", fmt="%s")

def cloud_decimation(points, factor):   # YOUR CODE TO EXECUTE
   return decimated_points
