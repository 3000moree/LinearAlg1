import numpy as np

u = np.array([1, 1, 0], dtype = float)      #이때는 dtype 무조건 float로 바꿔야 함
v = np.array([0, 1, 1], dtype= float)

dot_product = np.dot(u, v)
norm_u = np.linalg.norm(u)
norm_v = np.linalg.norm(v)

# 두 벡터 사이 거리
distance = np.linalg.norm(u - v)

print(f"내벅 = {dot_product:.6f}")
print(f"거리 = {distance:.6f}")

# 두 벡터 사이 각도
if norm_u == 0 or norm_v == 0:
    print("영벡터 포함, 각도 정의 못함")
else:
    cos_theta = dot_product / ((norm_u * norm_v))
    cos_theta = np.clip(cos_theta, -1.0, 1.0)   
    #clip은 변수를 두 수 사이 범위로 자름 여기서는 -1 < cos_theta < 1

    theta_rad = np.arccos(cos_theta)
    theta_deg = np.degrees(theta_rad)

    print(f"cos(theta) = {cos_theta:.6f}")
    print(f"각도 = {theta_deg:.6f}")