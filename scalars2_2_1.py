import numpy as np
x = np.array(12)
print("\nThe values in the Numpy array are: " + str(x))
print("\nThe dimension of tensor/vector in this case is: " + str(x.ndim))

x = np.array([12, 3, 6, 14])
print("\nThe values in the Numpy array are: " + str(x))
print("\nThe dimension of tensor/vector in this case is: " + str(x.ndim))

x = np.array([[5, 78, 2, 34, 0],
             [6, 79, 3, 35, 1],
             [7, 80, 4, 36, 2]])
print("\nThe dimension of tensor/vector in this case is: " + str(x.ndim))

x = np.array([[[5, 78, 2, 34, 0],
             [6, 79, 3, 35, 1],
             [7, 80, 4, 36, 2]],
            [[5, 78, 2, 34, 0],
             [6, 79, 3, 35, 1],
             [7, 80, 4, 36, 2]],
            [[5, 78, 2, 34, 0],
             [6, 79, 3, 35, 1],
             [7, 80, 4, 36, 2]]])
print("\nThe dimension of tensor/vector in this case is: " + str(x.ndim))
