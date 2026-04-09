import numpy as np

# # * array fundamentals
# a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
# print(a[1, 0])

# # * array attributes
# print(a.ndim)  # --> number of axes of the array
# print(a.shape)  # --> tuple of number of elements stored along each dimension
# print(a.size)  # -> total no. of elements
# print(a.dtype)  # -> datatype of the homogeneous array


# # * creating a basic array
# print(np.zeros(2))
# print(np.ones(2))
# print(np.empty(2))
# print(np.arange(2, 9, 2))

# # * sorting
# arr = np.array([2, 1, 5, 3, 7, 4, 6, 8])
# print(np.sort(arr, kind="mergesort"))

# # * reshaping array
# a = np.arange(6)
# b = np.reshape(a, shape=(6, 1))
# print(b)

# # * convert 1D to 2D array
# a = np.array([1, 2, 3, 4, 5, 6])
# print(a.ndim)
# a2 = a[np.newaxis, :]  # -> inserts a new dimension in row and take everything for col
# b = np.expand_dims(a, axis=0)  # --> inserts new dimension at a specificed position
# print(b)

# # * indexing/slicing
# a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
# print(a[a < 5])
# print(a[(a > 2) & (a < 11)])
# print((a > 5) | (a == 5))

# # * create an array from existing data
# a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# print(a[3:8])

# a1 = np.array([[1, 1], [2, 2]])
# a2 = np.array([[3, 3], [4, 4]])
# print(np.vstack((a1, a2)))
# print(np.hstack((a1, a2)))

# x = np.arange(1, 25).reshape(2, 12)
# print(np.hsplit(x, 3))

# # * views -> new array object looking at the original array faster and saves memory
# # ! modifies the original array
# a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
# b1 = a[1, :]
# print(b1)  # -> take the first row [1,] and slice all of it [1, :]
# b1[0] = 99
# print(b1)
# print(a)

# # * a deep copy of the array and its data
# b2 = a.copy()

# # * basic array operations
# data = np.array([1, 2])
# ones = np.ones(2, dtype=int)
# print(data + ones)
# print(data - ones)
# print(data * data)
# print(data / data)

# b = np.array([[1, 1], [2, 2]])
# print(b.sum(axis=0))  # -> collapse rows aka sum cols (↓)
# print(b.sum(axis=1))  # -> collapse cols aka sum rows (→)

# # * brodcasting -> dimensions must be compatible if they're equal or one of them is 1
# data = np.array([1.0, 2.0])
# print(data * 1.6)

# # * more useful array operations
# data = np.array([1, 2, 3])
# print(data.max())
# print(data.min())
# print(data.sum())

# a = np.array(
#     [
#         [0.45053314, 0.17296777, 0.34376245, 0.5510652],
#         [0.54627315, 0.05093587, 0.40067661, 0.55645993],
#         [0.12697628, 0.82485143, 0.26590556, 0.56917101],
#     ]
# )

# print(a.min(axis=0))  # -> min of each col

# # * execrises
# scores = np.array([[85, 90, 78], [92, 88, 95], [70, 65, 80], [88, 92, 85]])

# print(scores.max(axis=1))  # 1. highest score each student
# print(scores.mean(axis=0))  # 2. avg score per subject
# print(scores[scores > 85])  # 3. all scoresa above 85
# print(np.nonzero(scores > 85))  # 4. indices of scores above 85
# print(scores[0:2,]) # 5. scores of the first 2 students
# print(scores[:, 2]) # 6. scores of all students in last subject
# print(scores[0:2, 1:3]) # 7. top-right 2x2 subgrid
# print(scores[::2]) # 8. every other student score (0, 2, 4, ..)

# # * generation random numbers
# rng = np.random.default_rng()
# print(rng.integers(5, size=(2,4)))

# # * shape manipulation
# a = np.array([[3., 7., 3., 4.], [1., 4., 2., 2.],[7., 2., 4., 9.]])
# print(a.ravel()) # -> array, flattend
# print(a.reshape(6, 2)) # -> returns the modifed shape
# print(a.T) # -> transposed
# # a.resize((2,6)) # -> modifies the array itself
# print(a.reshape(5, -1))

# * stacking and splitting
# a = np.array([4,2, 4, 5, 6, 7])
# b = np.array([3,8, 5 ,6, 8 , 10])

# print(np.vstack((a,b))) # -> combining datasets (add more samples)
# print(np.hstack((a,b))) # -> combining features (add more cols)

# c = np.vstack((a,b))
# print(np.hsplit(c, 3)) # -> splitting data into batches or train/test
# print(np.vsplit(c, 2))

# # * copy and views
# a = np.array([[ 0,  1,  2,  3],
#               [ 4,  5,  6,  7],
#               [ 8,  9, 10, 11]])
# b = a
# print(b is a) # -> no new object just a and b are 2 names for same ndarray object

# c = a.view() # -> new array object, same data. changing view changes original
# print(c is a)
# c = c.reshape((2,6)) # -> independent shapes,just looks at the same data differently
# print(a.shape)

# d = a.copy() # -> new array object with the new data
# d[0,0] = 999 # wont change
# print(a)
# a = np.arange(int(1e8))
# # slicing returns a view, so a wont get deleted if you dont copy since b points to a's data
# del a
# b = a[:100].copy()
# print(b)

# * indexing with arrays of indices
a = np.arange(12) ** 2
i = np.array([1, 1, 3, 8, 5])
print(a[i])

j = np.array([[3, 4], [9, 7]])
print(a[j])
