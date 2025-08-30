import matplotlib.pyplot as plt
import numpy as np

x= np.linspace(-5,5,25)
y= np.linspace(-1,0,25)

x,y = np.meshgrid(x,y)

z= np.sin(np.sqrt(x**2 + y **2))

gig=plt.figure()

ax = gig.add_subplot(111, projection='3d')

ax.plot_surface(x,y,z, cmap='viridis')

plt.show()