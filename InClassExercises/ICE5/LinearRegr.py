import numpy as np
import matplotlib.pyplot as plt

x = np.array([0,1,2,3,4,5,6,7,8,9])
y = np.array([1,3,2,5,7,8,8,9,10,12])

meanx = np.mean(x)
meany = np.mean(y)

#slope = b1
slope = np.sum((x-meanx)*(y-meany))/np.sum(np.square(x-meanx))

bo = meany - slope * meanx

abline_values = [slope * i + bo for i in x]

plt.scatter(x, y, color='orange')
plt.plot(x, abline_values)
plt.title(slope)
plt.show()