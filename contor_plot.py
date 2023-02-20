
import matplotlib.pyplot as plt
import numpy as np


x = [1,2,3,4,5]
y = [6,7,8,9,10]

for i, valueX in enumerate(x):
    for j, valueY in enumerate(y):
        print(f"Z = : x{valueX} y{valueY}")


xlist = np.linspace(-3.0, 3.0, 100)
ylist = np.linspace(-3.0, 3.0, 100)
X, Y = np.meshgrid(xlist, ylist)
Z = np.sqrt(X**2 + Y**2)
fig,ax=plt.subplots(1,1)
cp = ax.contourf(X, Y, Z)
fig.colorbar(cp) # Add a colorbar to a plot
ax.set_title('Filled Contours Plot')
#ax.set_xlabel('x (cm)')
ax.set_ylabel('y (cm)')
plt.show()