import numpy as np

X = np.random.rand(3, 2)
print(X)

# -1 indicates that no size is given to the row field given below
Y = X - X.mean(axis=1).reshape(-1,1)
z = X.mean(axis=1)

print(z)

print(z.reshape(-1,1))
print("-----")

print(Y)