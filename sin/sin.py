import numpy as np
import matplotlib.pyplot as plt
def sin_function(A, f, xmin, xmax):
   x=np.linspace(xmin,xmax,100)
   y=A*np.sin(2*np.pi*f*x)
   #pic=plt.plot(x,y)
   #plt.show()
   return x, y
