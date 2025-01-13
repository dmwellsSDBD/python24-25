# import numpy
import numpy as np

# Title of section
print("\nCross Product of 2 Vectors")
print("--------------------------\n")

# Create input vector arrays
u = np.array([1, 0, 0])
v = np.array([0, 1, 0])
print("Vector u =", u)
print("Vector v =", v)

# The resulting cross product
result = np.cross(u, v)

print("The cross product of vector", u , "and vector", v , "is: ", result)

print("\n\n")

print("Norm of a Vector (Euclidean)")
print("----------------------------\n")

v = np.array([3, 4])
print("Vector v =", v)

result = np.linalg.norm(v)
print("The norm of vector", v , "is", result)

print("\n\n")

print("Binary Cross-Entropy (Special case)")
print("-----------------------------------\n")

y = np.array([1, 0])
y_hat = np.array([0.8, 0.2])

print("Our predicted probabilities are: ", y_hat)
print("Our true labels are", y)

bce = -np.mean(y * np.log(y_hat) + (1 - y) * np.log(1 - y_hat))

print("\nThe calculated Binary Cross-Entropy is:", bce)

print("\n\n")