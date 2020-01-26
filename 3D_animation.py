"""
This script anmates N particles which have their xyz coordinates written in 
N data files. You need to name your data files in an initials+particle_number
format. For example:
particle0.dat
particle1.dat
particle2.dat
etc...

IMPORTANT: If you wish to save your animation uncomment lines 73, 74, and 103.

Author: Adnan Ali Ahmad
"""

import matplotlib.pyplot as plt
import numpy as np
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation

N = 3 #insert number of particles you wish to animate
direct = "" #insert directory
init = "" #insert file initial
ext = "" #insert file extension (.txt, .dat, etc...)

#Extracting data length from first file
f = open(direct+"/"+init+"0"+ext, "r")
f.seek(0,0)
lines = f.readlines()
f.close()

x = np.zeros([N,len(lines)])
y = np.zeros([N,len(lines)])
z = np.zeros([N,len(lines)])

#Extracting data:
for k in range(N):
    f = open(direct+"/"+init+str(k)+ext, "r")
    f.seek(0,0)
    lines = f.readlines()
    f.close()
    for i,line in enumerate(lines):
        x[k][i] = float(line.split()[0])
        y[k][i] = float(line.split()[1])
        z[k][i] = float(line.split()[2])

# Insert grid limits:
xmin = -5.2
ymin = -5.2
xmax = -xmin
ymax = -ymin
zmin = -5.2
zmax = -zmin

"""
Optional: for time elapsed display. Need to insert integrator timestep (dt)
and frequency of output (snapshot)
"""
t = 0.; dt = 89236.7; snapshot = 50
time = 0.

def update_anim(i, dataDots,dots) :
    
    time = round(i*snapshot*dt/(31557600.0),2)
    ax.set_xlabel('x (AU)\nt = ' + str(time)+ ' years')
    ax.set_ylabel('y (AU)\nt = ' + str(time)+ ' years')
    for dot, data in zip(dots, dataDots) :
            dot.set_data(data[0:2,i])
            dot.set_3d_properties(data[2,i])
        
    return dots

# Set up formatting for the movie files
#Writer = animation.writers['ffmpeg']
#writer = Writer(fps=24, metadata=dict(artist='Me'), bitrate=1800)

# Attaching 3D axis to the figure
fig = plt.figure()
ax = p3.Axes3D(fig)


data_list = []
for p in range(N):
    data_list.append([x[p],y[p],z[p]])

data = np.array(data_list)


dots = [ax.plot(dat[0, 0:1], dat[1, 0:1], dat[2, 0:1],'o',markersize=1,color='blue')[0] for i,dat in enumerate(data)]


# Setting the axes properties
ax.set_xlim3d([xmin, xmax])
ax.set_xlabel('x (AU)')
ax.set_ylim3d([ymin,ymax])
ax.set_ylabel('y (AU)')
ax.set_zlim3d([zmin,zmax])
ax.set_zlabel('z (AU)')

# Creating the Animation object
anim = animation.FuncAnimation(fig, update_anim, x[0].size, fargs=(data,dots),
                              interval=1, blit=False)

#anim.save('filename.mp4', writer=writer)

plt.show()
