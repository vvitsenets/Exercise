import numpy as np
import matplotlib.pyplot as plt
A=np.array([
     [5,8,2],
     [2,6,5],
     [4,21,35],
 ])
B=np.array([
     [6,2,3],
     [1,8,2],
     [12,0,1],
 ])
C=np.dot(A,B)
print(C)
print(np.var(C))
print(np.mean(C))
plt.plot(C)
plt.show()