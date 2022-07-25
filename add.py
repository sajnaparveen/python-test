import numpy as np
a = np.array([[1,2,3],
              [4,5,6]])

b = np.array([[10,11,12],
              [13,14,15]])
c = a + b
print(c)

a = np.array([[1,2,3],
              [4,5,6]])

b = 2*a
print("b =",b)
#Array re-dimensioning
a = np.array([x for x in range(27)])

o = a.reshape((3,3,3))
print(o)

#Convert a binary numpy array (containing only 0s and 1s) to a boolean numpy array
a = np.array([[1, 0, 0],
              [1, 1, 1],
              [0, 0, 0]])

o = a.astype('bool')

print(o)

# Custom Sequence Generation
o = np.arange(0, 101, 2)

print(o)
#elements of two arrays match
a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])

print("match elements = ",np.where(a == b))


num =  np.linspace(1,5,8)
print(num)