import numpy as np

# Define the paramerts for intrinsic camera matrix:

f = 5/1000 # Focal length in mm
c = 4 # Optical center in mm

# Define the location of point on im plane strat from top left coner:

u = 0 # x location on img pline from top left cornrt of sesnor, not center in mm
v= 5.5 # y loction on img plane from top lerf corner

# Define the matrix A and output vector b

A = np.array([ [f, 0, c],
               [0, f, c],
               [0, 0, 1] ],)

b = np.array([u, v, 1])

# Solve the linear system using the lstsq function from NumPy
x, residuals, rank, singular_values = np.linalg.lstsq(A, b, rcond=None)

# Print the solution
print("Solution:", x[0], "mm and ", x[1], 'mm.')

