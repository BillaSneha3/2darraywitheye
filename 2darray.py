import numpy as np
A=np.array([[1,2,3],[4,5,6],[7,8,9]])
B=np.eye(3,dtype=int)

add=A+B
print("Addition of two matrices is:/n",add)

mul=A*B
print("multiplication of two matrices is:/n",mul)