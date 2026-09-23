import numpy as np
a=np.array([1,2,3,4,5])
# print(a)

b=np.array([[1,2,3,4],[5,6,7,8]])
# print(b)

c=np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(c)

# print(type(c))

# print(a.size)
# print(b.size)
# print(c.size)

# print(a.shape)    
# print(b.shape)
# print(c.shape)



# print(a.dtype)    
# print(b.dtype)
# print(c.dtype)



# print(b.transpose())


# x=np.ones((2,2))
# print(x)

# x=np.ones((2,3),dtype=int)
# print(x)

# x=np.ones((2,3),dtype=float)
# print(x)

# x=np.ones((2,3),dtype=str)
# print(x)

# x=np.ones((2,3),dtype=bool)
# print(x)

# x=np.zeros((2,3),dtype=int)
# print(x)

# x=np.zeros((4,4),dtype=float)
# print(x)

# x=np.zeros((4,4),dtype=str)
# print(x)

# x=np.zeros((4,4),bool)
# print(x)







# x=np.arange(10)
# print(x)

# x=np.arange(1,10)
# print(x)

# x=np.arange(1,10,2)
# print(x)







# y=np.array([1,2,3,4,5,6])
# z=y.reshape((3,2))
# print(z)

# z1=z.flatten()
# print(z1)

# z1=z.ravel()
# print(z1)


# a=np.array([[2,3],[5,2]])
# b=np.array([[2,3],[5,2]])

# c=np.dot(a,b)
# print(c)
# print(a@b)



# b=np.array([[2,3],[5,2],[2,5]])
# print(b[0,0])
# print(b[0])
# print(b[0::,1])
# print(b[:,:])
# print(b[:,1])
# print(b[:,1].dtype)



a=np.array([[1,2,3],[2,3,4],[5,6,7]])
b=np.array([[1,2,3],[2,3,4],[5,6,7]])

# print(a+b)
# x=np.add(a,b)
# print(x)
# print(a-b)
# x=np.subtract(a,b)
# print(x)
# print(a*b)
# print(np.multiply(a,b))
# print(a/b)
# print(np.divide(a,b))

# print(a.max())
# print(a.min())
# print(a.argmax())


# print(a@b)

x=np.sum(a,axis=0)
print(x)
x=np.sum(a,axis=1)
print(x)
print(np.mean(a))
print(np.sqrt(a))
print(np.std(a))
print(np.log(a))



