import numpy as np

arr1 = [1, 2, 3, 4, 5]

arr2 = np.array([1, 2, 3, 4, 5, 6])

# [1, 2, 3, 4, 5]
print('arr1:', arr1)

# <type 'list'>
print('arr1 type:', type(arr1))

# ----------------

# [1 2 3 4 5 6]
print('arr2:', arr2)

# (6,)
print('arr2 shape:', arr2.shape)

# <type 'numpy.ndarray'>
print('arr2 type:', type(arr2))

# ----------------

arr3 = np.array([[1, 5, 2], [4, 7, 4], [2, 0, 9]])

# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]
print('arr3:', arr3)

# (3, 3)
print('arr3 shape:', arr3.shape)

# ------matrix transpose----------
# [[1 4 7]
#  [2 5 8]
#  [3 6 9]]
print('arr3 transpose:', arr3.transpose())

# ------matrix determinant--------
# 0.0
print('arr3 det:', np.linalg.det(arr3))

# ------matrix inverse------------
# [[-0.6       ,  0.42857143, -0.05714286],
#  [ 0.26666667, -0.04761905, -0.03809524],
#  [ 0.13333333, -0.0952381 ,  0.12380952]]))
arr3_inv = np.linalg.inv(arr3)
print('arr3 inv:', arr3_inv)

# ------identity matrix------------
# [[ 1.00000000e+00, -8.32667268e-17,  1.66533454e-16],
#  [ 1.11022302e-16,  1.00000000e+00,  0.00000000e+00],
#  [ 5.55111512e-17, -1.38777878e-17,  1.00000000e+00]]
arr3_iden = np.dot(arr3, arr3_inv)
print('identity arr3:', arr3_iden)

# ------identity round matrix------
# [[1., 0., 0.],
#  [0., 1., 0.],
#  [0., 0., 1.]]
arr3_round = np.round(np.abs(arr3_iden))
print('identity round arr3:', arr3_round)