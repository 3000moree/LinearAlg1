import numpy as np

u = np.array([[2], [-5], [-1]])
v = np.array([[3], [2], [-3]])

#T: 전치, item() : 숫자 하나 추출
u_dot_v = (u.T @ v).item()
v_dot_u = (v.T @ u).item()

print("u dot v =", u_dot_v)
print("v dot u =", v_dot_u)
print("교환볍칙 확인:", u_dot_v == v_dot_u)
