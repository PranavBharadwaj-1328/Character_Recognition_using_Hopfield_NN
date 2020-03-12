# 17MCME06 Assignment2

import random

# Hopfield Weight matrix estimation
def hopfield(A,B,C):
  a = convert(A)
  b = convert(B)
  c = convert(C)
  M = [] # weight matrix
  for i in range(0,100):
    x = []
    for j in range(0,100):
      d = a[i]*a[j] + b[i]*b[j] + c[i]*c[j]
      if(i == j):
        x.append(0)
      else:
        x.append(d)
    M.append(x)
  return M

# Method to convert an NxN matrix to an N^2x1 
def convert(X):
  O = []
  for i in range(0,10):
    for j in range(0,10):
      O.append(X[i][j])

  return(O)

# Method to print matrix
def printmatrix(X):
  
  for i in range(0,10):
    s = ""
    for j in range(0,10):
      if(X[i][j] == -1):
        s = s + " "
      else:
        s = s + "X"
    print(s)

  print("\n")
    

# Predict function which takes X shape matrix as input
def predict(A,B,C,X):
  print("Input:\n")
  printmatrix(X)
  a = convert(A)
  b = convert(B)
  c = convert(C)
  x = convert(X)
  W = hopfield(A,B,C)
  P = []
  for i in range(0,100):
    d = 0
    for j in range(0,100):
      d = d + (x[j]*W[i][j])
    if(d > 0):
      P.append(1)
    else:
      P.append(-1)
  if(P == a):   # when the prediction matrix is equal to A's matrix
    print("Converges to A\n")
    printmatrix(A)
  elif(P == b):  # when the prediction matrix is equal to B's matrix
    print("Converges to B\n")
    printmatrix(B)
  else:          # when the prediction matrix is equal to C's matrix
    print("Converges to C\n")
    printmatrix(C)


# shape matrices of A,B,C and X (input)
# X can be changed accordingly
A = [[-1,-1,-1,-1,1,1,-1,-1,-1,-1],[-1,-1,-1,-1,1,1,-1,-1,-1,-1],[-1,-1,-1,1,1,1,1,-1,-1,-1],[-1,-1,-1,1,-1,-1,1,-1,-1,-1],[-1,-1,1,1,-1,-1,1,1,-1,-1],[-1,-1,1,-1,-1,-1,-1,1,-1,-1],[-1,1,1,1,1,1,1,1,1,-1],[-1,1,1,1,1,1,1,1,1,-1],[1,1,-1,-1,-1,-1,-1,-1,1,1],[1,-1,-1,-1,-1,-1,-1,-1,-1,1]]

B = [[1,1,1,1,1,1,-1,-1,-1,-1],[1,1,1,1,1,1,1,-1,-1,-1],[1,1,-1,-1,-1,1,1,-1,-1,-1],[1,1,1,1,1,1,1,-1,-1,-1],[1,1,1,1,1,1,-1,-1,-1,-1],[1,1,-1,-1,-1,1,1,1,-1,-1],[1,1,-1,-1,1,1,1,-1,-1,-1],[1,1,-1,-1,-1,1,1,1,-1,-1],[1,1,1,1,1,1,1,-1,-1,-1],[1,1,1,1,1,1,-1,-1,-1,-1]]

C = [[-1,-1,-1,1,1,1,1,1,-1,-1],[-1,-1,1,1,1,1,1,1,-1,-1],[1,1,-1,-1,-1,-1,-1,-1,1,1],[1,1,-1,-1,-1,-1,-1,-1,-1,-1],[1,1,-1,-1,-1,-1,-1,-1,-1,-1],[1,1,-1,-1,-1,-1,-1,-1,-1,-1],[1,1,-1,-1,-1,-1,-1,-1,-1,-1],[1,1,-1,-1,-1,-1,-1,-1,1,1],[-1,-1,1,1,1,1,1,1,-1,-1],[-1,-1,-1,1,1,1,1,-1,-1,-1]]

# corrupted A
X1 = [[-1,-1,-1,-1,1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,1,-1,-1,-1,-1,-1],[-1,-1,-1,1,1,1,1,-1,-1,-1],[-1,-1,-1,1,-1,-1,1,-1,-1,-1],[-1,-1,1,1,-1,-1,1,1,-1,-1],[-1,-1,1,-1,-1,-1,-1,1,-1,-1],[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],[1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1]]

# corrupted B
X2 = [[1,1,1,1,-1,-1,-1,-1,-1,-1],[1,1,1,1,1,1,1,-1,-1,-1],[1,1,-1,1,1,1,-1,-1,-1,-1],[1,1,1,1,1,1,1,-1,-1,-1],[1,-1,-1,-1,1,1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,1,1,-1,-1,-1],[1,-1,-1,-1,1,-1,1,-1,-1,-1],[1,1,-1,-1,-1,-1,1,1,-1,-1],[1,1,1,-1,1,-1,1,-1,-1,-1],[-1,-1,-1,-1,1,1,-1,-1,-1,-1]]

# corrupted C
X3 = [[-1,-1,-1,1,1,1,1,1,1,1],[-1,-1,1,1,1,1,1,1,1,1],[1,1,-1,-1,-1,-1,-1,-1,1,1],[1,1,-1,-1,-1,-1,-1,-1,1,1],[1,1,-1,-1,-1,-1,-1,-1,1,1],[1,1,-1,-1,-1,-1,-1,-1,1,1],[1,1,-1,-1,-1,-1,-1,-1,1,1],[1,1,-1,-1,-1,-1,-1,-1,1,1],[-1,-1,1,1,1,1,1,1,1,1],[-1,-1,-1,1,1,1,1,-1,-1,-1]]


print("Corrupted A as input:\n")      
predict(A,B,C,X1)
print("Corrupted B as input:\n")      
predict(A,B,C,X2)
print("Corrupted C as input:\n")      
predict(A,B,C,X3)
