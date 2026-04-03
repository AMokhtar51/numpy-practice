import numpy as np

# * array fundamentals
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(a[1, 0])

# * array attributes
print(a.ndim)  # --> number of axes of the array
print(a.shape)  # --> tuple of number of elements stored along each dimension
print(a.size)  # -> total no. of elements
print(a.dtype)  # -> datatype of the homogeneous array


# * creating a basic array
print(np.zeros(2))
print(np.ones(2))
print(np.empty(2))
print(np.arange(2, 9, 2))

# * sorting
arr = np.array([2, 1, 5, 3, 7, 4, 6, 8])
print(np.sort(arr, kind="mergesort"))

# * reshaping array
a = np.arange(6)
b = np.reshape(a, shape=(6, 1))
print(b)

# * convert 1D to 2D array
a = np.array([1, 2, 3, 4, 5, 6])
print(a.ndim)
a2 = a[np.newaxis, :]  # -> inserts a new dimension in row and take everything for col
b = np.expand_dims(a, axis=0)  # --> inserts new dimension at a specificed position
print(b)

# * indexing/slicing
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(a[a < 5])
print(a[(a > 2) & (a < 11)])
print((a > 5) | (a == 5))

# * create an array from existing data
a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(a[3:8])

a1 = np.array([[1, 1], [2, 2]])
a2 = np.array([[3, 3], [4, 4]])
print(np.vstack((a1, a2)))
print(np.hstack((a1, a2)))

x = np.arange(1, 25).reshape(2, 12)
print(np.hsplit(x, 3))

# * views -> new array object looking at the original array faster and saves memory
# ! modifies the original array
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
b1 = a[1, :]
print(b1)  # -> take the first row [1,] and slice all of it [1, :]
b1[0] = 99
print(b1)
print(a)

# * a deep copy of the array and its data
b2 = a.copy()

# * basic array operations
data = np.array([1, 2])
ones = np.ones(2, dtype=int)
print(data + ones)
print(data - ones)
print(data * data)
print(data / data)

b = np.array([[1, 1], [2, 2]])
print(b.sum(axis=0))  # -> collapse rows aka sum cols (↓)
print(b.sum(axis=1))  # -> collapse cols aka sum rows (→)

# * brodcasting -> dimensions must be compatible if they're equal or one of them is 1
data = np.array([1.0, 2.0])
print(data * 1.6)

# * more useful array operations
data = np.array([1, 2, 3])
print(data.max())
print(data.min())
print(data.sum())

a = np.array(
    [
        [0.45053314, 0.17296777, 0.34376245, 0.5510652],
        [0.54627315, 0.05093587, 0.40067661, 0.55645993],
        [0.12697628, 0.82485143, 0.26590556, 0.56917101],
    ]
)

print(a.min(axis=0))  # -> min of each col
