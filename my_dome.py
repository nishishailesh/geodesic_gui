#!/usr/bin/python3
import matplotlib.pyplot as plt
import os

from geodome.geodesic_dome import *
from geodome.tessellation import *
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

def find_nth(listt,n):
    x=[]
    for each in listt:
        x=x+[each[n],]
    return x
    

fh=open("output.txt",'w')

    
gd = GeodesicDome(2)

t=gd.get_triangles()
v=gd.get_vertices()

#print(v)
#print(t)
#nb=gd.find_neighbours_vertex(0,1)
#print(nb)
#exit(0)


#fig = plt.figure(figsize=(4,4))
fig = plt.figure()

ax = fig.add_subplot(111, projection='3d')

ax.scatter(v[:,0],v[:,1],v[:,2])

for each_data in t:
    #print(each_data)
    #print("{} {} {}".format(v[each_data[0]],v[each_data[1]],v[each_data[2]]))
    myt=[v[each_data[0]],] + [v[each_data[1]],] + [v[each_data[2]],]
    print(myt)
    #fh.write("{}\n".format(myt))
    fh.write("{},{},{}\n".format(v[each_data[0]][0],v[each_data[0]][1],v[each_data[0]][2],))
    fh.write("{},{},{}\n".format(v[each_data[1]][0],v[each_data[1]][1],v[each_data[1]][2],))
    fh.write("{},{},{}\n".format(v[each_data[2]][0],v[each_data[2]][1],v[each_data[2]][2],))
    fh.write("\n")
    print(find_nth(myt,0))
    ax.plot(find_nth(myt,0),find_nth(myt,1),find_nth(myt,2))
    
#ax.scatter(2,3,4) # plot the point (2,3,4) on the figure
#ax.scatter(2,3,5) # plot the point (2,3,4) on the figure
#ax.scatter(2,6,6) # plot the point (2,3,4) on the figure
#ax.scatter(2,7,7) # plot the point (2,3,4) on the figure
#ax.scatter(2,8,8) # plot the point (2,3,4) on the figure
#ax.scatter(2,3,8) # plot the point (2,3,4) on the figure


#srf = Poly3DCollection(t, alpha=.25, facecolor='#800000')
#@ 3. add polygon to the figure (current axes)
#plt.gca().add_collection3d(srf)

plt.show()
