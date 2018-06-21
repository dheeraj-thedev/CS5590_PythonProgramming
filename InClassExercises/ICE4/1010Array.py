import numpy as np

a=np.random.random((10,10))
print("10*10 matrix is:")
#print(a)
print("min value is:")
print(a.min())
print("max value is:")
print(a.max())
print("minimum values from each row are :")
print(np.min(a,axis=1))