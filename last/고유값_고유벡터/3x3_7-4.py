#(1)
'''
import numpy as np

A = np.array([
    [0, 0, 0],
    [0, 2, 5],
    [0, 0, -1]
], dtype = float)

#고유값, 벡터 계산
eigenvalues, X = np.linalg.eig(A)

#matlab처럼 고유값을 정렬
order = np.argsort(eigenvalues)[::-1]
eigenvalues = eigenvalues[order]
X = X[:, order]

#고유값을 대각행렬로
lamda = np.diag(eigenvalues)

np.set_printoptions(precision=4, suppress=True, floatmode="fixed")

X = np.real(X)
lamda = np.real(lamda)

print("X =")
print(X)
print("\nlamda =")
print(lamda)

'''

#(2)

import numpy as np

A = np.array([
    [4, 0, 0],
    [0, 0, 0],
    [1, 0, -3]
], dtype = float)

#고유값, 벡터 계산
eigenvalues, X = np.linalg.eig(A)

#matlab처럼 고유값을 정렬
order = np.argsort(eigenvalues)[::-1]
eigenvalues = eigenvalues[order]
X = X[:, order]

#고유값을 대각행렬로
lamda = np.diag(eigenvalues)

np.set_printoptions(precision=4, suppress=True, floatmode="fixed")

X = np.real(X)
lamda = np.real(lamda)

print("X =")
print(X)
print("\nlamda =")
print(lamda)
