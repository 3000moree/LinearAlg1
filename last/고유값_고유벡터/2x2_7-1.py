import numpy as np

A = np.array([
    [2, 3],
    [3, -6]
]
, dtype = float)

#고유값, 벡터 계산
eigenvalues, X = np.linalg.eig(A)

#matlab처럼 고유값을 정렬
order = np.argsort(eigenvalues)[::-1]
eigenvalues = eigenvalues[order]
X = X[:, order]

#고유값을 대각행렬로
lamda = np.diag(eigenvalues)

np.set_printoptions(precision=4, suppress=True, floatmode="fixed") 
#precision은 소수점 4자리까지 / suppress = True는 지수 표기법 안한다 / floatmode = "fixed"는 소수점 고정

X = np.real(X)
lamda = np.real(lamda)

print("X =")
print(X)
print("\nlamda =")
print(lamda)